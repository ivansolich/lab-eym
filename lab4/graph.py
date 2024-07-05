import os
import matplotlib.pyplot as plt

# Define la ruta base donde se encuentran los archivos
ruta_base = 'datos'

nombre_archivo = 'data7.txt'
ruta_archivo = os.path.join(ruta_base, nombre_archivo)

# Abre el archivo para lectura
with open(ruta_archivo, 'r') as file:
    # Inicializa dos listas vacías
    lista1 = []
    lista2 = []

    # Lee el archivo línea por línea
    for linea in file:
        # Imprime la línea para depuración
        print(f"Línea original: '{linea}'")

        # Separa la línea en dos valores usando uno o más espacios como separador
        valores = linea.split()

        # Imprime los valores separados para depuración
        print(f"Valores separados: {valores}")

        # Asegúrate de que hay exactamente dos valores
        if len(valores) == 2:
            try:
                # Convierte los valores a float después de eliminar espacios en blanco
                valor1 = float(valores[0].strip())
                valor2 = float(valores[1].strip())

                # Añade los valores a las listas
                lista1.append(valor1)
                lista2.append(valor2)
            except ValueError:
                print(f"Error de conversión de valores: {valores}")

# Imprime las listas para verificar los resultados
print("Lista 1:", lista1)
print("Lista 2:", lista2)

# Encuentra el índice del primer 0.0 en lista1
indice_corte = lista1.index(0.0)

# Elimina los elementos anteriores al índice de corte en ambas listas
lista1 = lista1[indice_corte:]
lista2 = lista2[indice_corte:]

# Imprime las listas para verificar los resultados
print("Lista 1:", lista1)
print("Lista 2:", lista2)


fig, ax = plt.subplots()

#ax.scatter(lista1, lista2)
ax.plot(lista1, lista2, color='red',alpha=0.5)

#ax.set_ylim(max(lista2) - 0.45, max(lista2) + 0.45)

posMax = lista2.index(max(lista2))
print(max(lista2), posMax)

#ax.set_xlim(data_list_1[posMax]-0.1, data_list_1[posMax]+0.1)

plt.show()