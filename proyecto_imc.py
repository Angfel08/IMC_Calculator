import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import winsound

def calcular_imc():
    try:
        peso = float(peso_entry.get())
        altura = float(altura_entry.get())

        if peso <= 0 or altura <= 0:
            raise ValueError

        imc = peso / (altura ** 2)

        if imc < 18.5:
            resultado_imc.config(text="Tu IMC es: {:.2f}".format(imc), foreground="blue")
        elif imc >= 25:
            resultado_imc.config(text="Tu IMC es: {:.2f}".format(imc), foreground="red")
        else:
            resultado_imc.config(text="Tu IMC es: {:.2f}".format(imc), foreground="black")

    except ValueError:
        resultado_imc.config(text="Error: Ingresa valores válidos")

    # Reproducir sonido
    winsound.PlaySound("sonido_calcular.wav", winsound.SND_ASYNC)


def resetear_campos():
    peso_entry.delete(0, tk.END)
    altura_entry.delete(0, tk.END)
    resultado_imc.config(text="")

# Crear la ventana principal
window = tk.Tk()
window.title("Calculadora de IMC")

# Cargar y redimensionar la imagen del logo
logo = Image.open("logo.png")
logo = logo.resize((100, 100))
logo = ImageTk.PhotoImage(logo)

# Crear estilo para los widgets
style = ttk.Style(window)
style.configure("TButton", font=("Arial", 12), padding=10)
style.configure("TLabel", font=("Arial", 12))

# Crear contenedor para el contenido
container = ttk.Frame(window)
container.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

# Agregar el logo
logo_label = ttk.Label(container, image=logo)
logo_label.pack(pady=10)

# Crear campos de entrada
peso_label = ttk.Label(container, text="Peso (kg):")
peso_label.pack(pady=10)

peso_entry = ttk.Entry(container)
peso_entry.pack()

altura_label = ttk.Label(container, text="Altura (m):")
altura_label.pack(pady=10)

altura_entry = ttk.Entry(container)
altura_entry.pack()

# Crear botones
button_frame = ttk.Frame(container)
button_frame.pack(pady=10)

calcular_button = ttk.Button(button_frame, text="Calcular", command=calcular_imc)
calcular_button.pack(side=tk.LEFT)

reset_button = ttk.Button(button_frame, text="Reiniciar", command=resetear_campos)
reset_button.pack(side=tk.LEFT, padx=10)

# Crear etiqueta para mostrar el resultado del IMC
resultado_imc = ttk.Label(container, font=("Arial", 12))
resultado_imc.pack()

# Configurar el comportamiento de redimensionamiento de la ventana
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

# Ejecutar el bucle principal de la ventana
window.mainloop()
