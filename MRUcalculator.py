import tkinter as tk
from tkinter import messagebox

def calculate_distance():
    try:
        velocity = float(velocity_entry.get())
        time = float(time_entry.get())
        distance = velocity * time
        result_label.config(text=f"Distancia: {distance}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos.")

def clear_fields():
    velocity_entry.delete(0, tk.END)
    time_entry.delete(0, tk.END)
    result_label.config(text="Distancia: ")

# Crear la ventana principal
root = tk.Tk()
root.title("Calculadora de Distancia en MRU")

# Etiquetas y campos de entrada
tk.Label(root, text="Velocidad (m/s):").grid(row=0, column=0, padx=10, pady=5)
velocity_entry = tk.Entry(root)
velocity_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Tiempo (s):").grid(row=1, column=0, padx=10, pady=5)
time_entry = tk.Entry(root)
time_entry.grid(row=1, column=1, padx=10, pady=5)

# Etiqueta para el resultado
result_label = tk.Label(root, text="Distancia: ")
result_label.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

# Botones
calculate_button = tk.Button(root, text="Calcular", command=calculate_distance)
calculate_button.grid(row=3, column=0, padx=10, pady=10)

clear_button = tk.Button(root, text="Borrar", command=clear_fields)
clear_button.grid(row=3, column=1, padx=10, pady=10)

# Iniciar el loop de la aplicación
root.mainloop()