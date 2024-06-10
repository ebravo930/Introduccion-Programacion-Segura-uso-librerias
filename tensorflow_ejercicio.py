# Importamos TensorFlow y submódulos necesarios de Keras.
import tensorflow as tf
from tensorflow.keras import datasets, layers, models

# Cargamos el conjunto de datos MNIST y dividimos en conjuntos de entrenamiento y prueba.
# El dataset MNIST es el considerado "Hello World" de la visión artificial.
(train_images, train_labels), (test_images, test_labels) = datasets.mnist.load_data()

# Normalizamos los valores de los píxeles de las imágenes para que estén en el rango [0, 1] para mejorar el entrenamiento.
train_images, test_images = train_images / 255.0, test_images / 255.0

# Creación del modelo utilizando la API Sequential de Keras.
# La API Sequential es adecuada para una pila simple de capas donde cada capa tiene exactamente un tensor de entrada y un tensor de salida.
model = models.Sequential([
    layers.Flatten(input_shape=(28, 28)),  # Transforma la matriz 2D de 28x28 en un vector 1D de 784 píxeles.
    layers.Dense(128, activation='relu'),  # Capa densa con 128 neuronas y función de activación ReLU.
    layers.Dense(10)  # Capa de salida con 10 neuronas, una por cada clase de dígito (0-9).
])

# Compilación del modelo: definimos el optimizador, la función de pérdida y las métricas para monitorizar.
model.compile(optimizer='adam',  # Optimizador Adam, eficiente para este tipo de tareas.
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),  # Usamos crossentropy para clasificación multiclase.
              metrics=['accuracy'])  # La métrica de precisión es útil para evaluar la clasificación.

# Entrenamos el modelo con los datos de entrenamiento. 
model.fit(train_images, train_labels, epochs=10)  # Ejecutamos el entrenamiento durante 10 épocas.

# Comentarios adicionales:
# Escala de los Datos: Normalizar los datos de imagen a un rango de 0 a 1 es una práctica común que ayuda a acelerar la convergencia durante el entrenamiento al reducir la variabilidad de los datos de entrada.
# Modelo:
# Flatten: Se usa para convertir las imágenes 2D en vectores 1D, lo que permite que los datos se ingresen en una capa densa.
# Dense: Las capas densas son las capas neuronales completamente conectadas. relu (unidad lineal rectificada) es la función de activación más común en redes neuronales debido a su eficiencia.
# La última capa densa no tiene una función de activación especificada porque se utiliza from_logits=True en la función de pérdida. Esto significa que la función de pérdida esperará que las salidas sean logits sin escalar.
# Compilación:
# Optimizador Adam: Este optimizador ajusta automáticamente la tasa de aprendizaje y es efectivo en una amplia gama de problemas.
# Crossentropy: Adecuada para problemas de clasificación, esta función de pérdida mide el desempeño del modelo cuyas salidas son probabilidades de una clasificación multiclase.
# Entrenamiento:
# Epochs: El número de épocas es una hiperparámetro que define el número de veces que el algoritmo de aprendizaje trabajará a través de todo el conjunto de datos de entrenamiento. Aquí, se ha configurado para 10 iteraciones a través del conjunto completo.

