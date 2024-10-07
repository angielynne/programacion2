import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from productos import productos

class Venta:
    def __init__(self, producto, cantidad):
        self.producto = producto
        self.cantidad = cantidad
        self.total = producto.preunitario * cantidad
        self.fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

ventas_historial = []

def update_price(event):
    seleccionado = dropdown_producto.get()
    for producto in productos:
        if producto.nombre == seleccionado:
            entry_unit_price.config(state='normal')
            entry_unit_price.delete(0, tk.END)
            entry_unit_price.insert(0, producto.preunitario)
            entry_stock.config(state='normal')
            entry_stock.delete(0, tk.END)
            entry_stock.insert(0, producto.stock)
            break

def calculate_total():
    try:
        cantidad = int(entry_quantity.get())
        unit_price = float(entry_unit_price.get())
        total = cantidad * unit_price
        entry_total.config(state='normal')
        entry_total.delete(0, tk.END)
        entry_total.insert(0, total)
        entry_total.config(state='readonly')
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese una cantidad válida")

def save_sale():
    seleccionado = dropdown_producto.get()
    try:
        cantidad = int(entry_quantity.get())
        for producto in productos:
            if producto.nombre == seleccionado:
                if cantidad > producto.stock:
                    messagebox.showerror("Error", "No es posible realizar la venta porque no hay suficiente stock")
                else:
                    venta = Venta(producto, cantidad)
                    producto.stock -= cantidad
                    ventas_historial.append(venta)
                    entry_receipt.insert(tk.END, f"Fecha: {venta.fecha}\n"
                                                   f"Producto: {venta.producto.nombre}\n"
                                                   f"Cantidad: {venta.cantidad}\n"
                                                   f"Precio Unitario: {venta.producto.preunitario}\n"
                                                   f"Total: {venta.total}\n"
                                                   f"Stock Restante: {producto.stock}\n\n")
                    entry_quantity.delete(0, tk.END)
                    entry_total.delete(0, tk.END)
                    update_price(event=None)
                break
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese una cantidad válida")

def show_history():
    entry_history.delete(1.0, tk.END)  # Clear previous history
    for venta in ventas_historial:
        entry_history.insert(tk.END, f"Fecha: {venta.fecha}\n"
                                      f"Producto: {venta.producto.nombre}\n"
                                      f"Cantidad: {venta.cantidad}\n"
                                      f"Total: {venta.total}\n"
                                      f"-----------------------\n")

def reset_fields():
    dropdown_producto.set('')
    entry_quantity.delete(0, tk.END)
    entry_total.delete(0, tk.END)
    entry_receipt.delete(1.0, tk.END)  # Clear receipt
    entry_history.delete(1.0, tk.END)  # Clear history
    entry_unit_price.config(state='normal')
    entry_stock.config(state='normal')

root = tk.Tk()
root.title("Interfaz de Venta")
root.configure(bg="#f0f0f0")

frame_product = tk.Frame(root, bg="#f0f0f0")
frame_product.pack(pady=10)

tk.Label(frame_product, text="Producto:", bg="#f0f0f0").grid(row=0, column=0, padx=10, pady=5)
dropdown_producto = ttk.Combobox(frame_product, values=[producto.nombre for producto in productos])
dropdown_producto.grid(row=0, column=1, padx=10, pady=5)
dropdown_producto.bind("<<ComboboxSelected>>", update_price)

tk.Label(frame_product, text="Cantidad:", bg="#f0f0f0").grid(row=1, column=0, padx=10, pady=5)
entry_quantity = tk.Entry(frame_product)
entry_quantity.grid(row=1, column=1, padx=10, pady=5)

tk.Label(frame_product, text="Precio Unitario:", bg="#f0f0f0").grid(row=2, column=0, padx=10, pady=5)
entry_unit_price = tk.Entry(frame_product)  # Make editable
entry_unit_price.grid(row=2, column=1, padx=10, pady=5)

tk.Label(frame_product, text="Stock Disponible:", bg="#f0f0f0").grid(row=3, column=0, padx=10, pady=5)
entry_stock = tk.Entry(frame_product)  # Make editable
entry_stock.grid(row=3, column=1, padx=10, pady=5)

frame_actions = tk.Frame(root, bg="#f0f0f0")
frame_actions.pack(pady=10)

tk.Button(frame_actions, text="Calcular Total", command=calculate_total, bg="#4CAF50", fg="white").grid(row=0, column=0, padx=10, pady=10)
tk.Label(frame_actions, text="Total de Venta:", bg="#f0f0f0").grid(row=0, column=1, padx=10, pady=5)
entry_total = tk.Entry(frame_actions, state='readonly')  # Total should remain read-only
entry_total.grid(row=0, column=2, padx=10, pady=5)

tk.Button(frame_actions, text="Guardar Venta", command=save_sale, bg="#008CBA", fg="white").grid(row=1, column=0, columnspan=2, padx=10, pady=10)
tk.Button(frame_actions, text="Mostrar Historial", command=show_history, bg="#FFC107").grid(row=1, column=2, padx=10, pady=10)
tk.Button(frame_actions, text="Resetear", command=reset_fields, bg="#f44336", fg="white").grid(row=1, column=3, padx=10, pady=10)

frame_receipt = tk.Frame(root, bg="#f0f0f0")
frame_receipt.pack(pady=10)

tk.Label(frame_receipt, text="Recibo:", bg="#f0f0f0").grid(row=0, column=0, padx=10, pady=5)
entry_receipt = tk.Text(frame_receipt, height=10, width=50)  # Text area for receipt
entry_receipt.grid(row=1, column=0, padx=10, pady=5)

frame_history = tk.Frame(root, bg="#f0f0f0")
frame_history.pack(pady=10)

tk.Label(frame_history, text="Historial de Ventas:", bg="#f0f0f0").grid(row=0, column=0, padx=10, pady=5)
entry_history = tk.Text(frame_history, height=10, width=50)  # Text area for history
entry_history.grid(row=1, column=0, padx=10, pady=5)

root.mainloop()
