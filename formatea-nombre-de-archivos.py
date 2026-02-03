import os
import unicodedata
import tkinter as tk
from tkinter import filedialog, messagebox

def limpiar_nombre(texto):
    # Pasar a minúsculas y quitar acentos
    texto = texto.lower()
    texto = unicodedata.normalize('NFKD', texto).encode('ascii', 'ignore').decode('ascii')
    # Reemplazar espacios por guiones
    texto = texto.replace(" ", "-")
    return texto

def procesar_carpeta():
    ruta = filedialog.askdirectory()
    if not ruta:
        return

    contador = 0
    archivos_modificados = []
    for archivo in os.listdir(ruta):
        nombre_nuevo = limpiar_nombre(archivo)
        if archivo != nombre_nuevo:
            try:
                os.rename(os.path.join(ruta, archivo), os.path.join(ruta, nombre_nuevo))
                contador += 1
                archivos_modificados.append(nombre_nuevo)
            except Exception as e:
                print(f"Error con {archivo}: {e}")
        else:
            archivos_modificados.append(nombre_nuevo)

    if archivos_modificados:
        with open(os.path.join(ruta, "archivos_modificados.txt"), "w", encoding="utf-8") as f:
            for nombre in archivos_modificados:
                f.write(f"{nombre}\n")

    messagebox.showinfo("Finalizado", f"Se han renombrado {contador} archivos con éxito.")

# Configuración de la Ventana
ventana = tk.Tk()
ventana.title("Formatea nombre de archivos")
ventana.geometry("700x150")

label = tk.Label(ventana, text="Selecciona una carpeta para formatear nombres de archivos\n(Cambia mayúsculas por minúsculas, quita los acentos, y reemplaza los espacios por guiones)", pady=20)
label.pack()

boton = tk.Button(ventana, text="Elegir Carpeta", command=procesar_carpeta, bg="#4CAF50", fg="white", padx=10)
boton.pack()

ventana.mainloop()