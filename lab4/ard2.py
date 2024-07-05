import os
import serial
import time
import matplotlib.pyplot as plt

# Función para obtener un nombre de archivo que no exista
def obtener_nombre_archivo(base):
    i = 0
    archivo = f'{base}.txt'
    while os.path.exists(archivo):
        i += 1
        archivo = f'{base}{i}.txt'
    return archivo

# Obtener el nombre del archivo de salida
archivo_salida = obtener_nombre_archivo('data')

# Cambia '/dev/ttyUSB0' al puerto serial correspondiente en tu sistema
ser = serial.Serial('/dev/ttyACM0', 9600)

time.sleep(2)

data_list_1 = []  # Lista para almacenar el primer valor de cada línea
data_list_2 = []  # Lista para almacenar el segundo valor de cada línea

with open(archivo_salida, 'w') as file:
    try:
        while True:
            if ser.in_waiting > 0:
                line = ser.readline().decode('utf-8', errors='ignore').rstrip()
                print(line, 'V')
                file.write(f'{line}\n')
                values = line.split()  # Dividir la línea en dos valores
                if len(values) == 2:  # Asegurarse de que hay exactamente dos valores
                    # Convertir a float y asegurarse de que ambas listas se llenen desde 0.0
                    value1 = float(values[0])
                    value2 = float(values[1])

                    if len(data_list_1) == 0 and len(data_list_2) == 0:
                        data_list_1.append(value1)
                        data_list_2.append(value2)
                    else:
                        if value1 == 0.0 and value2 == 0.0:
                            data_list_1 = [value1]
                            data_list_2 = [value2]
                        else:
                            data_list_1.append(value1)
                            data_list_2.append(value2)
    except KeyboardInterrupt:
        print('Interrupted')
        print('Data List 1:', data_list_1)  # Imprimir la primera lista de datos cuando se interrumpe el script
        print('Data List 2:', data_list_2)  # Imprimir la segunda lista de datos cuando se interrumpe el script
    finally:
        ser.close()

fig, ax = plt.subplots()

ax.plot(data_list_1, data_list_2)
ax.set_ylim(max(data_list_2) - 0.3, max(data_list_2) + 0.2)

posMax = data_list_2.index(max(data_list_2))
print(max(data_list_2), posMax)

#ax.set_xlim(data_list_1[posMax]-0.1, data_list_1[posMax]+0.1)

plt.show()
