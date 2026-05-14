# TP Gestión Colaborativa, Control de Versiones y Organización Empresarial

Trabajo práctico de Organización Empresarial realizado por Leandro Nicolas Acuña.

## Escenario elegido

Elegí el escenario A, análisis de datos climáticos. La idea fue trabajar con un dataset público de Buenos Aires y generar indicadores simples de temperatura y precipitaciones.

## Dataset usado

El archivo principal es `datos/clima_buenos_aires_2024.csv`.

Fuente: Open-Meteo Historical Weather API  
https://open-meteo.com/

El dataset contiene registros diarios de temperatura media, temperatura máxima, temperatura mínima y precipitaciones para Buenos Aires durante 2024.

## Estructura del repositorio

```text
datos/
  clima_buenos_aires_2024.csv
scripts/
  analisis_clima.py
resultados/
  resumen_clima.csv
  resumen_mensual_clima.csv
  grafico_temperatura_buenos_aires.svg
  grafico_temperatura_buenos_aires.png
README.md
.gitignore
```

## Cómo ejecutar el proyecto

Desde Google Colab o desde una terminal con Python:

```bash
python scripts/analisis_clima.py
```

El script lee el CSV desde `datos/`, calcula indicadores generales y guarda los resultados en `resultados/`.

## Resultados esperados

El análisis genera:

- un resumen de indicadores climáticos;
- una tabla mensual con temperatura y precipitaciones;
- un gráfico de evolución del clima en Buenos Aires.

## Trabajo con Jira y GitHub

Como el trabajo lo realicé de forma individual, asumí los tres roles pedidos en la consigna:

- P1: organización del repositorio, carpetas y README.
- P2: desarrollo del script de análisis en Python.
- P3: revisión, seguridad, documentación y control final.

Los commits deben respetar el formato indicado por la cátedra:

```text
ID-JIRA: descripción del cambio
```

Ejemplo:

```text
TP2-1: crear estructura inicial del repositorio
TP2-2: agregar script de análisis climático
TP2-3: documentar resultados y buenas prácticas
```

## Seguridad

No se suben tokens ni claves al repositorio. El Personal Access Token de GitHub se usa solo para autenticar el push desde Colab y no debe quedar escrito en celdas públicas.
