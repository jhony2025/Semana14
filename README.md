# Semana14
Agenda Personal, Desarrollar aplicación GUI utilizando Tkinter 

Institución: Universidad Estatal Amazónica (UEA)
Carrera: Ingeniería en Tecnologías de la Información y Comunicación
Asignatura: Programación Orientada a Objetos 2525-UEA-L-UFB-030-D
Estudiante: Johnny Vera 

Agenda Personal - Aplicación GUI con Tkinter
## Descripción

Esta aplicación es una Agenda Personal desarrollada en Python utilizando la librería Tkinter y el componente adicional tkcalendar.
El programa permite:

Agregar eventos con fecha, hora y descripción.

Visualizar eventos en un listado tipo tabla (TreeView).

Eliminar eventos seleccionados con confirmación.

Salir de la aplicación desde la interfaz gráfica.

Es una práctica de la Unidad 4: Interfaces Gráficas en Python, con el objetivo de comprender el manejo de componentes, contenedores y eventos en aplicaciones GUI.

## Requisitos

Antes de ejecutar la aplicación, asegúrate de tener instalado:

Python 3.10+

Librerías necesarias:

pip install tkcalendar


## tkcalendar es un módulo externo que provee el widget DateEntry para seleccionar fechas de manera más intuitiva.

# Ejecución

Clonar el repositorio o guardar el archivo agendaAPPtkinter.py en tu equipo.
Luego, ejecuta:

python agendaAPPtkinter.py


Esto abrirá la ventana de la aplicación.

## Interfaz Gráfica

La aplicación está organizada en tres secciones principales:

## Lista de eventos (TreeView)

Ubicada en la parte superior.

Muestra los eventos programados con sus tres columnas:

Fecha

Hora

Descripción

Incluye scrollbar vertical para manejar grandes cantidades de eventos.

## Entrada de datos (Frame de inputs)

Aquí el usuario puede introducir la información del nuevo evento:

Fecha: seleccionada con un DateEntry de tkcalendar.

Hora: campo de texto donde el usuario escribe la hora (ejemplo: 14:30).

Descripción: campo de texto libre para detallar el evento.

## Botones de acción

En la parte inferior se encuentran los botones:

Agregar Evento: añade un nuevo evento a la lista.

Eliminar Evento Seleccionado: elimina el evento marcado en la lista, tras una confirmación.

Salir: cierra la aplicación.

## Funcionalidades del código
# agregar_evento()

Toma los valores ingresados en los campos fecha, hora y descripción.

Valida que no estén vacíos.

Inserta los datos en el TreeView.

Limpia los campos para permitir un nuevo registro.

 ## eliminar_evento()

Detecta qué evento está seleccionado en el TreeView.

Si no hay selección, muestra una advertencia.

Si hay selección, pide confirmación antes de eliminar.

## salir()

Cierra de forma segura la aplicación al presionar el botón Salir.

## Organización del código

El archivo está organizado en bloques:

Encabezado con autor y descripción.

Importación de librerías.

Definición de funciones (agregar, eliminar, salir).

Configuración de la ventana principal.

Creación de los Frames:

TreeView de eventos.

Entradas de datos (fecha, hora, descripción).

Botones de acción.

Ejecución del root.mainloop() para mantener abierta la interfaz.

 ## Ejemplo de uso

Selecciona una fecha con el calendario.

Escribe la hora en el campo correspondiente.

Añade una descripción breve del evento.

Haz clic en Agregar Evento → aparecerá en la lista.

Para eliminarlo, selecciónalo y haz clic en Eliminar Evento Seleccionado.

## Conclusión

Este proyecto permite practicar:

Manejo de Tkinter en Python.

Uso de Frames para organizar la interfaz.

Integración de un componente externo (tkcalendar).

Programación orientada a eventos con botones y acciones.

La aplicación es sencilla, pero representa una base sólida para sistemas más complejos de gestión de información.
