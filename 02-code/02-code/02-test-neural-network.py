import numpy as np
import tensorflow as tf

celsius = np.array([-40, -10, 0, 8, 15, 22, 38], dtype=float)
farenheit = np.array([-40, 14, 32, 46, 59, 72, 100], dtype=float)

capa = tf.keras.layers.Dense(units=1, input_shape=[1])
modelo = tf.keras.Sequential([capa])

modelo.compile(optimizer=tf.keras.optimizers.Adam(0.1), loss='mean_squared_error')

print("Training...")
historial = modelo.fit(celsius, farenheit, epochs= 800, verbose=False)
print("Trained")

resultado = modelo.predict([100.0])
print("Resultado: " + str(resultado))