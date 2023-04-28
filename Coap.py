from tkinter import *
from coapthon.client.helperclient import HelperClient

import random

# Configura el cliente CoAP
client = HelperClient(server=('localhost', 5683))


# Función para obtener la temperatura y humedad de manera aleatoria
# Función para obtener la temperatura y humedad de manera aleatoria
def obtener_datos():
    # Genera un número aleatorio entre 0 y 100 para la temperatura y humedad
    temperatura = random.randint(0, 100)
    humedad = random.randint(0, 100)

    # Envía una solicitud CoAP para actualizar los datos en el servidor
    payload = 'temperatura={}, humedad={}'.format(temperatura, humedad)
    try:
        response = client.put(path='/temperatura_humedad', payload=payload, timeout=5)
    except Exception as e:
        print('Error al enviar la solicitud CoAP:', e)

    # Actualiza las etiquetas de temperatura y humedad en la GUI
    lbl_temperatura.config(text='Temperatura: {}°C'.format(temperatura))
    lbl_humedad.config(text='Humedad: {}%'.format(humedad))

    # Repite la función cada 5 segundos
    root.after(5000, obtener_datos)


# Crea la ventana GUI
root = Tk()
root.title('Temperatura y Humedad')

# Crea etiquetas para la temperatura y humedad
lbl_temperatura = Label(root, font=('Arial', 24))
lbl_temperatura.pack()
lbl_humedad = Label(root, font=('Arial', 24))
lbl_humedad.pack()

# Inicia la función para obtener datos de manera aleatoria
obtener_datos()

# Inicia la aplicación
root.mainloop()
