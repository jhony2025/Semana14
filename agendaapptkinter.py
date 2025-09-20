# -----------------------------------------------
# AGENDA PERSONAL - TAREA UNIDAD 4
# Autor: [Johnny Vera]
# Descripción:
# Aplicación GUI con Tkinter para gestionar eventos
# Permite agregar, visualizar y eliminar eventos.
# -----------------------------------------------

import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry   # Debes instalarlo con: pip install tkcalendar

# ---------------- Funciones ----------------
def agregar_evento():
    """Agrega un evento a la lista (TreeView)"""
    fecha = entry_fecha.get()
    hora = entry_hora.get()
    descripcion = entry_desc.get()

    if not fecha or not hora or not descripcion:
        messagebox.showwarning("Campos vacíos", "Por favor, complete todos los campos.")
        return

    tree.insert("", "end", values=(fecha, hora, descripcion))

    # Limpiar campos
    entry_hora.delete(0, tk.END)
    entry_desc.delete(0, tk.END)

def eliminar_evento():
    """Elimina el evento seleccionado del TreeView"""
    seleccionado = tree.selection()
    if not seleccionado:
        messagebox.showwarning("Selección vacía", "Por favor, seleccione un evento para eliminar.")
        return
    
    confirmacion = messagebox.askyesno("Confirmar eliminación", "¿Está seguro de eliminar este evento?")
    if confirmacion:
        for item in seleccionado:
            tree.delete(item)

def salir():
    """Cierra la aplicación"""
    root.quit()

# ---------------- Ventana principal ----------------
root = tk.Tk()
root.title("Agenda Personal")
root.geometry("700x500")

# ---------------- Frame: Visualización (TreeView) ----------------
frame_tree = tk.Frame(root, borderwidth=2, relief="groove", bg="lightblue")
frame_tree.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

lbl_tree = tk.Label(frame_tree, text="Eventos Programados", bg="lightblue", font=("Arial", 12, "bold"))
lbl_tree.pack(side=tk.TOP, pady=5)

# Scrollbar + Treeview
tree_scroll = ttk.Scrollbar(frame_tree)
tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)

tree = ttk.Treeview(frame_tree, yscrollcommand=tree_scroll.set, selectmode="browse")
tree.pack(fill=tk.BOTH, expand=True)
tree_scroll.config(command=tree.yview)

# Configurar columnas
tree['columns'] = ("Fecha", "Hora", "Descripción")
tree.column("#0", width=0, stretch=tk.NO)  # Columna fantasma
tree.column("Fecha", anchor=tk.CENTER, width=100)
tree.column("Hora", anchor=tk.CENTER, width=80)
tree.column("Descripción", anchor=tk.W, width=400)

tree.heading("#0", text="", anchor=tk.W)
tree.heading("Fecha", text="Fecha", anchor=tk.CENTER)
tree.heading("Hora", text="Hora", anchor=tk.CENTER)
tree.heading("Descripción", text="Descripción", anchor=tk.W)

# ---------------- Frame: Entrada de datos ----------------
frame_inputs = tk.Frame(root, borderwidth=2, relief="groove", bg="lightgray")
frame_inputs.pack(padx=10, pady=5, fill=tk.X)

lbl_inputs = tk.Label(frame_inputs, text="Nuevo Evento", bg="lightgray", font=("Arial", 11, "bold"))
lbl_inputs.grid(row=0, column=0, columnspan=2, pady=5)

# Campo Fecha (DatePicker)
tk.Label(frame_inputs, text="Fecha:", bg="lightgray").grid(row=1, column=0, sticky="e", padx=5, pady=5)
entry_fecha = DateEntry(frame_inputs, width=12, background='darkblue', foreground='white', borderwidth=2)
entry_fecha.grid(row=1, column=1, sticky="w", padx=5, pady=5)

# Campo Hora
tk.Label(frame_inputs, text="Hora:", bg="lightgray").grid(row=2, column=0, sticky="e", padx=5, pady=5)
entry_hora = tk.Entry(frame_inputs, width=15)
entry_hora.grid(row=2, column=1, sticky="w", padx=5, pady=5)

# Campo Descripción
tk.Label(frame_inputs, text="Descripción:", bg="lightgray").grid(row=3, column=0, sticky="e", padx=5, pady=5)
entry_desc = tk.Entry(frame_inputs, width=50)
entry_desc.grid(row=3, column=1, sticky="w", padx=5, pady=5)

# ---------------- Frame: Botones ----------------
frame_buttons = tk.Frame(root, borderwidth=2, relief="groove", bg="lightgreen")
frame_buttons.pack(padx=10, pady=10, fill=tk.X)

btn_agregar = tk.Button(frame_buttons, text="Agregar Evento", command=agregar_evento, bg="white")
btn_agregar.pack(side=tk.LEFT, padx=10, pady=5)

btn_eliminar = tk.Button(frame_buttons, text="Eliminar Evento Seleccionado", command=eliminar_evento, bg="white")
btn_eliminar.pack(side=tk.LEFT, padx=10, pady=5)

btn_salir = tk.Button(frame_buttons, text="Salir", command=salir, bg="white")
btn_salir.pack(side=tk.RIGHT, padx=10, pady=5)

# ---------------- Iniciar aplicación ----------------
root.mainloop()