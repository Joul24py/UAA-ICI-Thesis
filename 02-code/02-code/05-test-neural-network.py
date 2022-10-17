import numpy as np
import tensorflow as tf

celsius = np.array([-40, -10, 0, 8, 15, 22, 38], dtype=float)
farenheit = np.array([-40, 14, 32, 46, 59, 72, 100], dtype=float)

#capa = tf.keras.layers.Dense(units=1, input_shape=[1])
#modelo = tf.keras.Sequential([capa])
oculta1 = tf.keras.layers.Dense(units=3, input_shape=[1])
oculta2 = tf.keras.layers.Dense(units=3)
salida = tf.keras.layers.Dense(units=1)
modelo = tf.keras.Sequential([oculta1, oculta2, salida])

modelo.compile(optimizer=tf.keras.optimizers.Adam(0.1), loss='mean_squared_error')

print("Training...")
historial = modelo.fit(celsius, farenheit, epochs= 200, verbose=False)
print("Trained")

resultado = modelo.predict([100.0])
print("Resultado: " + str(resultado))

print("Pesos de oculta1: " + str(oculta1.get_weights()))
print("Pesos de oculta2: " + str(oculta2.get_weights()))
print("Pesos de salida: " + str(salida.get_weights()))