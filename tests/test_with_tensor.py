import unittest
import tensorflow as tf
import numpy as np

def crear_modelo():
    model = tf.keras.Sequential([
        tf.keras.layers.Input(shape=(1,)),  # Añadir una capa de entrada explícita
        tf.keras.layers.Dense(units=1)
    ])
    model.compile(optimizer='sgd', loss='mean_squared_error')
    return model

class TestModeloTensorFlow(unittest.TestCase):
    def test_prediccion(self):
        modelo = crear_modelo()
        entrada = np.array([[10.0]])  # Usar numpy array en lugar de lista
        prediccion = modelo.predict(entrada)
        self.assertIsNotNone(prediccion)

if __name__ == '__main__':
    unittest.main()

"""
Una capa de entrada explícita en un modelo de TensorFlow/Keras es una forma de definir de manera explícita la forma y el tipo de datos que el modelo recibirá como entrada. Esto se hace utilizando la clase Input de Keras, la cual especifica la forma de los datos de entrada.

¿Por qué usar una capa de entrada explícita?
Claridad y robustez: Define claramente qué tipo de datos el modelo espera, lo que ayuda a evitar errores y hace que el modelo sea más fácil de entender.
Flexibilidad: Permite definir entradas más complejas, como múltiples entradas o entradas con formas no triviales.
Compatibilidad: Es necesario para ciertos tipos de arquitecturas de modelos o para utilizar ciertas funcionalidades avanzadas de Keras.

¿Cuándo usar una capa de entrada explícita?
Modelos complejos: Cuando se tiene una arquitectura de modelo más compleja, como modelos con múltiples entradas.
Claridad en la definición: Para hacer más clara la definición del modelo.
Compatibilidad con ciertas funcionalidades: Algunas funcionalidades avanzadas de Keras requieren el uso de capas de entrada explícitas.
"""