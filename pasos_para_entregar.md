# Pasos para terminar la entrega

Estos son los pasos que tenés que hacer para que quede evidencia en Jira, GitHub y Colab.

## 1. Jira

Crear un proyecto en Jira. Si te deja elegir clave, podés usar `TP2`.

Crear estas tareas:

| Issue | Título | Descripción |
|---|---|---|
| TP2-1 | Crear repositorio y estructura inicial | Armar carpetas `/datos`, `/scripts`, `/resultados`, README y `.gitignore`. |
| TP2-2 | Desarrollar análisis climático en Python | Crear el script que lee el dataset, calcula indicadores y genera resultados. |
| TP2-3 | Revisar documentación y seguridad | Revisar que no haya tokens, mejorar README y controlar que el proyecto se pueda reproducir. |

Estados sugeridos:

1. Pasar `TP2-1` de Pendiente a En curso y después a Finalizado.
2. Hacer lo mismo con `TP2-2`.
3. Hacer lo mismo con `TP2-3` al final.

## 2. GitHub y commits

Desde Colab, después de clonar tu repo, los commits tendrían que quedar así:

```bash
git add README.md .gitignore datos/ scripts/
git commit -m "TP2-1: crear estructura inicial del repositorio"

python scripts/analisis_clima.py

git add resultados/ scripts/analisis_clima.py
git commit -m "TP2-2: agregar análisis climático en Python"

git add README.md pasos_para_entregar.md
git commit -m "TP2-3: documentar revisión y buenas prácticas"
```

## 3. Rama y Pull Request

Para cumplir el flujo con branch y PR:

```bash
git checkout -b feature/analisis-clima
git push origin feature/analisis-clima
```

En GitHub crear un Pull Request desde `feature/analisis-clima` hacia `main`.

Como lo hacés solo, podés dejar dos comentarios técnicos en el PR, por ejemplo:

1. "Revisé que el script use rutas relativas para que funcione en Colab sin depender de mi computadora."
2. "Controlé que el token de GitHub no quede guardado en el repositorio y que el .gitignore cubra archivos temporales."

Después hacer merge del PR.

## 4. Google Colab

Configurar identidad:

```python
!git config --global user.email "tu.email@ejemplo.com"
!git config --global user.name "Leandro Nicolas Acuna"
```

Clonar:

```python
!git clone https://github.com/Leanmucho/TP-2-Gesti-n-Colaborativa-Control-de-Versiones-y-Organizaci-n-Empresarial.git
```

Entrar al repo y ejecutar:

```python
%cd TP-2-Gesti-n-Colaborativa-Control-de-Versiones-y-Organizaci-n-Empresarial
!python scripts/analisis_clima.py
```

Para subir cambios desde Colab, usar PAT sin dejarlo escrito en una celda pública.

## 5. Checklist según la rúbrica

Antes de entregar, controlar esto:

- Jira: tiene que haber 3 issues (`TP2-1`, `TP2-2`, `TP2-3`) y tienen que estar actualizados a Finalizado.
- Trazabilidad: todos los commits tienen que empezar con el ID de Jira, por ejemplo `TP2-2: agregar análisis climático en Python`.
- GitHub: trabajar con una rama `feature/analisis-clima`, no hacer todo directo en `main`.
- Pull Request: crear un PR hacia `main` y dejar al menos 2 comentarios técnicos antes del merge.
- Colab: ejecutar el proyecto desde Colab y, si podés, guardar captura de la configuración de Git y de la ejecución del script.
- Seguridad: no subir ningún token, clave o archivo `.env`.
- Reproducibilidad: revisar que estén las carpetas `datos/`, `scripts/` y `resultados/`.
- Informe: entregar el PDF final, no fotos ni capturas sueltas como entrega principal.

Lo más importante para no perder puntos es que el historial de GitHub coincida con Jira. Si Jira dice `TP2-2`, el commit también tiene que decir `TP2-2`.
