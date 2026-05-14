from collections import defaultdict
from csv import reader, writer
from datetime import datetime
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[1]
DATOS = BASE_DIR / "datos" / "clima_buenos_aires_2024.csv"
RESULTADOS = BASE_DIR / "resultados"


def leer_datos():
    with DATOS.open("r", encoding="utf-8-sig", newline="") as archivo:
        filas = list(reader(archivo))

    # El CSV de Open-Meteo trae primero dos filas de metadata y despues la tabla.
    filas_datos = [fila for fila in filas[3:] if fila]
    registros = []
    for fila in filas_datos[1:]:
        fecha = datetime.strptime(fila[0], "%Y-%m-%d")
        registros.append(
            {
                "fecha": fecha,
                "temp_media": float(fila[1]),
                "temp_max": float(fila[2]),
                "temp_min": float(fila[3]),
                "precipitacion": float(fila[4]),
            }
        )
    return registros


def guardar_resumen_general(registros):
    promedio_temp = sum(r["temp_media"] for r in registros) / len(registros)
    temp_maxima = max(r["temp_max"] for r in registros)
    temp_minima = min(r["temp_min"] for r in registros)
    promedio_precipitacion = sum(r["precipitacion"] for r in registros) / len(registros)
    total_precipitacion = sum(r["precipitacion"] for r in registros)

    resumen = [
        ("Temperatura promedio", f"{promedio_temp:.2f} C"),
        ("Temperatura maxima", f"{temp_maxima:.2f} C"),
        ("Temperatura minima", f"{temp_minima:.2f} C"),
        ("Promedio diario de precipitacion", f"{promedio_precipitacion:.2f} mm"),
        ("Precipitacion total anual", f"{total_precipitacion:.2f} mm"),
    ]

    with (RESULTADOS / "resumen_clima.csv").open("w", encoding="utf-8", newline="") as archivo:
        salida = writer(archivo)
        salida.writerow(["indicador", "valor"])
        salida.writerows(resumen)

    return resumen


def guardar_resumen_mensual(registros):
    por_mes = defaultdict(list)
    for registro in registros:
        por_mes[registro["fecha"].strftime("%Y-%m")].append(registro)

    resumen_mensual = []
    for mes, items in sorted(por_mes.items()):
        resumen_mensual.append(
            {
                "mes": mes,
                "temp_media": sum(r["temp_media"] for r in items) / len(items),
                "temp_max": max(r["temp_max"] for r in items),
                "temp_min": min(r["temp_min"] for r in items),
                "precipitacion": sum(r["precipitacion"] for r in items),
            }
        )

    with (RESULTADOS / "resumen_mensual_clima.csv").open(
        "w", encoding="utf-8", newline=""
    ) as archivo:
        salida = writer(archivo)
        salida.writerow(["mes", "temp_media", "temp_max", "temp_min", "precipitacion"])
        for fila in resumen_mensual:
            salida.writerow(
                [
                    fila["mes"],
                    f"{fila['temp_media']:.2f}",
                    f"{fila['temp_max']:.2f}",
                    f"{fila['temp_min']:.2f}",
                    f"{fila['precipitacion']:.2f}",
                ]
            )

    return resumen_mensual


def escala(valor, minimo, maximo, salida_min, salida_max):
    if maximo == minimo:
        return (salida_min + salida_max) / 2
    proporcion = (valor - minimo) / (maximo - minimo)
    return salida_max - proporcion * (salida_max - salida_min)


def generar_grafico_svg(resumen_mensual):
    ancho, alto = 900, 460
    margen_izq, margen_der, margen_sup, margen_inf = 70, 35, 45, 70
    area_ancho = ancho - margen_izq - margen_der
    area_alto = alto - margen_sup - margen_inf

    temps = [fila["temp_media"] for fila in resumen_mensual]
    lluvias = [fila["precipitacion"] for fila in resumen_mensual]
    temp_min, temp_max = min(temps) - 1, max(temps) + 1
    lluvia_max = max(lluvias) or 1

    puntos = []
    barras = []
    etiquetas = []

    for i, fila in enumerate(resumen_mensual):
        x = margen_izq + (area_ancho / (len(resumen_mensual) - 1)) * i
        y_temp = escala(fila["temp_media"], temp_min, temp_max, margen_sup, margen_sup + area_alto)
        puntos.append(f"{x:.1f},{y_temp:.1f}")

        barra_alto = (fila["precipitacion"] / lluvia_max) * (area_alto * 0.45)
        barra_x = x - 16
        barra_y = margen_sup + area_alto - barra_alto
        barras.append(
            f'<rect x="{barra_x:.1f}" y="{barra_y:.1f}" width="32" height="{barra_alto:.1f}" fill="#9bc3d4" opacity="0.75" />'
        )

        mes = fila["mes"][5:]
        etiquetas.append(
            f'<text x="{x:.1f}" y="{alto - 35}" text-anchor="middle" font-size="13" fill="#333">{mes}</text>'
        )

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{ancho}" height="{alto}" viewBox="0 0 {ancho} {alto}">
  <rect width="100%" height="100%" fill="#ffffff"/>
  <text x="{ancho / 2}" y="28" text-anchor="middle" font-family="Arial" font-size="20" font-weight="bold" fill="#1d3f4f">Clima de Buenos Aires durante 2024</text>
  <text x="{ancho / 2}" y="52" text-anchor="middle" font-family="Arial" font-size="13" fill="#555">Temperatura media mensual y precipitacion acumulada</text>
  <line x1="{margen_izq}" y1="{margen_sup + area_alto}" x2="{ancho - margen_der}" y2="{margen_sup + area_alto}" stroke="#444"/>
  <line x1="{margen_izq}" y1="{margen_sup}" x2="{margen_izq}" y2="{margen_sup + area_alto}" stroke="#444"/>
  {"".join(barras)}
  <polyline points="{' '.join(puntos)}" fill="none" stroke="#d05a37" stroke-width="4"/>
  {"".join(f'<circle cx="{p.split(",")[0]}" cy="{p.split(",")[1]}" r="4" fill="#d05a37"/>' for p in puntos)}
  {"".join(etiquetas)}
  <text x="{margen_izq}" y="{alto - 12}" font-family="Arial" font-size="12" fill="#555">Meses de 2024</text>
  <text x="18" y="{margen_sup + 15}" font-family="Arial" font-size="12" fill="#d05a37" transform="rotate(-90 18,{margen_sup + 15})">Temperatura media</text>
  <text x="{ancho - 230}" y="{margen_sup + 20}" font-family="Arial" font-size="13" fill="#333">Linea: temperatura media | Barras: precipitacion</text>
</svg>'''

    (RESULTADOS / "grafico_temperatura_buenos_aires.svg").write_text(
        svg, encoding="utf-8"
    )


def generar_grafico_png(resumen_mensual):
    try:
        from PIL import Image, ImageDraw
    except ImportError:
        return

    ancho, alto = 900, 460
    margen_izq, margen_der, margen_sup, margen_inf = 70, 35, 55, 70
    area_ancho = ancho - margen_izq - margen_der
    area_alto = alto - margen_sup - margen_inf

    temps = [fila["temp_media"] for fila in resumen_mensual]
    lluvias = [fila["precipitacion"] for fila in resumen_mensual]
    temp_min, temp_max = min(temps) - 1, max(temps) + 1
    lluvia_max = max(lluvias) or 1

    imagen = Image.new("RGB", (ancho, alto), "white")
    dibujo = ImageDraw.Draw(imagen)

    dibujo.text((ancho // 2 - 150, 18), "Clima de Buenos Aires durante 2024", fill=(29, 63, 79))
    dibujo.text((ancho // 2 - 190, 38), "Temperatura media mensual y precipitacion acumulada", fill=(85, 85, 85))
    dibujo.line((margen_izq, margen_sup + area_alto, ancho - margen_der, margen_sup + area_alto), fill=(68, 68, 68))
    dibujo.line((margen_izq, margen_sup, margen_izq, margen_sup + area_alto), fill=(68, 68, 68))

    puntos = []
    for i, fila in enumerate(resumen_mensual):
        x = margen_izq + (area_ancho / (len(resumen_mensual) - 1)) * i
        y_temp = escala(fila["temp_media"], temp_min, temp_max, margen_sup, margen_sup + area_alto)
        puntos.append((x, y_temp))

        barra_alto = (fila["precipitacion"] / lluvia_max) * (area_alto * 0.45)
        dibujo.rectangle(
            (x - 16, margen_sup + area_alto - barra_alto, x + 16, margen_sup + area_alto),
            fill=(155, 195, 212),
        )
        dibujo.text((x - 8, alto - 40), fila["mes"][5:], fill=(51, 51, 51))

    for inicio, fin in zip(puntos, puntos[1:]):
        dibujo.line((inicio[0], inicio[1], fin[0], fin[1]), fill=(208, 90, 55), width=4)
    for x, y in puntos:
        dibujo.ellipse((x - 4, y - 4, x + 4, y + 4), fill=(208, 90, 55))

    dibujo.text((ancho - 260, margen_sup + 10), "Linea: temperatura | Barras: lluvia", fill=(51, 51, 51))
    imagen.save(RESULTADOS / "grafico_temperatura_buenos_aires.png")


def main():
    RESULTADOS.mkdir(exist_ok=True)
    registros = leer_datos()
    resumen = guardar_resumen_general(registros)
    resumen_mensual = guardar_resumen_mensual(registros)
    generar_grafico_svg(resumen_mensual)
    generar_grafico_png(resumen_mensual)

    print("Analisis finalizado. Archivos generados en la carpeta resultados.")
    for indicador, valor in resumen:
        print(f"- {indicador}: {valor}")


if __name__ == "__main__":
    main()
