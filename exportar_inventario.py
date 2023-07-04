from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

from data_productos import *
from main import inventario

print(inventario)
def exportar_inventario():
    # Convertir la lista de diccionarios en una lista de listas
    data = [list(inventario_general[0].keys())] + [list(item.values()) for item in inventario_general]

    # Agregar el símbolo 'S/.' a las columnas 'precio_u' y 'costo_p'
    precio_u_index = data[0].index('precio_u')
    costo_p_index = data[0].index('costo_p')
    for row in data[1:]:
        row[precio_u_index] = f'S/. {row[precio_u_index]}'
        row[costo_p_index] = f'S/. {row[costo_p_index]}'

    # Crear un archivo PDF con ReportLab
    doc = SimpleDocTemplate("inventario.pdf", pagesize=letter)
    elements = []

    # Crear una tabla en ReportLab con la información de la lista de listas
    table = Table(data)

    # Agregar estilo a la tabla (opcional)
    # La función setStyle toma como argumento un objeto TableStyle que define el estilo de la tabla.
    # (x,y)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (5, 0), '#d5dae6'), # establece el color de fondo de la primera fila, color hexadecimal.
        ('TEXTCOLOR', (0, 0), (5, 0), '#1e1e2d'), # establece el color del texto de la primera fila, color hexadecimal.
        ('ALIGN', (0, 0), (0, -1), 'CENTER'), # centra el contenido de todas las celdas.
        ('ALIGN', (0, 0), (5,0), 'CENTER'),
        ('ALIGN', (2, 0), (2, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (5, 0), 'Helvetica-Bold'), # establece la fuente de la primera fila.
        ('FONTSIZE', (0, 0), (5, 0), 14), # establece el tamaño de fuente de la primera fila en 14.
        ('BOTTOMPADDING', (0, 0), (5, 0), 12), #agrega un relleno inferior de 12 a la primera fila.
        ('BACKGROUND', (0, 1), (-1, -1), '#f7f7f9'), #  establece el color de fondo de todas las filas excepto la primera
        ('GRID', (0, 0), (-1, -1), 1, '#d5dae6'), # agrega una cuadrícula de ancho 1 y color a todas las celdas.
    ]))

    # Agregar la tabla al archivo PDF
    elements.append(table)
    doc.build(elements)

