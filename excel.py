from openpyxl import Workbook

x1 = [-0.4, -0.3, -0.2, -0.2, -0.1, 0, 0, 0, 0, -0.2, -0.3]
y1 = [-6, -5, -3, -2, -1, 0, 1, 2, 3, 5, 6]

x2 = [2.5, 2.3, 2.1, 1.8, 1.9, 2, 2, 2.1, 2.2, 2.4, 2.5]
y2 = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]

x3 = [-2.7, -2.3, -2.2, -2.2, -2, -2, -2.1, -2.2, -2.4, -2.7]
y3 = [-5, -3, -2, -1, 0, 1, 2, 3, 4, 5]

x4 = [-4.6, -4.4, -4.2, -4, -4, -4.1, -4.2, -4.2, -4.5]
y4 = [-4, -3, -2, -1, 0, 1, 2, 3, 4]

x5 = [-1.3, -1.2, -1.1, -1.1, -1.1, -1, -1, -1, -1.1, -1.2, -1.4]
y5 = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]

x6 = [1.4, 1.3, 1.1, 1, 0.9, 1, 1.1, 1.2, 1.3, 1.3, 1.3]
y6 = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]

wb = Workbook()
ruta = 'salida.xlsx'

hoja = wb.active
hoja.title = "Fecha-Valor"

fila = 1 #Fila donde empezamos
col_x = 1 #Columna donde guardamos las fechas
col_y = 2 #Columna donde guardamos el dato asociados a cada fecha

for x, y in zip(x1, x1):
    hoja.cell(column=col_x, row=fila, value=x)
    hoja.cell(column=col_y, row=fila, value=y)
    fila+=1

wb.save(filename = ruta)