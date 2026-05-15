# TP Gestion Colaborativa, Control de Versiones y Organizacion Empresarial

Trabajo practico de Organizacion Empresarial realizado por Leandro Nicolas Acuna.

## Escenario elegido

Elegi el escenario A, analisis de datos climaticos. La idea fue trabajar con un dataset publico de Buenos Aires y generar indicadores simples de temperatura y precipitaciones.

## Dataset usado

El archivo principal es `datos/clima_buenos_aires_2024.csv`.

Fuente: Open-Meteo Historical Weather API  
https://open-meteo.com/

El dataset contiene registros diarios de temperatura media, temperatura maxima, temperatura minima y precipitaciones para Buenos Aires durante 2024.

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

## Como ejecutar el proyecto

Desde Google Colab o desde una terminal con Python:

```bash
python scripts/analisis_clima.py
```

El script lee el CSV desde `datos/`, calcula indicadores generales y guarda los resultados en `resultados/`.

## Resultados esperados

El analisis genera:

- un resumen de indicadores climaticos;
- una tabla mensual con temperatura y precipitaciones;
- un grafico de evolucion del clima en Buenos Aires.

## Trabajo con Jira y GitHub

Como el trabajo lo realice de forma individual, asumi los tres roles pedidos en la consigna:

- P1: organizacion del repositorio, carpetas y README.
- P2: desarrollo del script de analisis en Python.
- P3: revision, seguridad, documentacion y control final.

Los commits deben respetar el formato indicado por la catedra:

```text
ID-JIRA: descripcion del cambio
```

Historial de commits del proyecto:

```text
TP2-1: crear estructura inicial del repositorio
TP2-2: agregar analisis climatico en Python
TP2-3: documentar informe final y buenas practicas
TP2-4: agregar notebook de Colab y corregir codificacion
TP2-5: quitar acentos para evitar errores de codificacion
```

## Seguridad

No se suben tokens ni claves al repositorio. El Personal Access Token de GitHub se usa solo para autenticar el push desde Colab y no debe quedar escrito en celdas publicas.
