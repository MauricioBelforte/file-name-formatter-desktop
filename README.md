# Normalizador de Nombres de Archivos

Herramienta sencilla en Python para normalizar nombres de archivos masivamente. Convierte a minúsculas, elimina acentos y reemplaza espacios por guiones, generando automáticamente un reporte `.txt` con los resultados.

## Características

*   **Interfaz Gráfica:** Selección de carpeta sencilla mediante ventana de diálogo.
*   **Normalización:**
    *   Convierte todo el nombre a minúsculas.
    *   Elimina acentos y caracteres especiales (normalización NFKD ASCII).
    *   Reemplaza espacios en blanco por guiones (`-`).
*   **Reporte:** Genera un archivo `archivos_modificados.txt` dentro de la carpeta procesada con la lista de los nombres resultantes.

## Requisitos

*   Python 3.x
*   Librería estándar `tkinter` (generalmente incluida con Python).

## Uso

1.  Ejecuta el script:
    ```bash
    python formatea-nombre-de-archivos.py
    ```
2.  Haz clic en el botón **"Elegir Carpeta"**.
3.  Selecciona el directorio que contiene los archivos que deseas renombrar.
4.  El programa procesará los archivos y mostrará un mensaje de confirmación al finalizar.

## Crear Ejecutable (Opcional)

Si deseas compilarlo como ejecutable para Windows, puedes usar PyInstaller:

```bash
pyinstaller --onefile --windowed formatea-nombre-de-archivos.py
```