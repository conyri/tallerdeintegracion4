# Paso 1: importamos la librería numérica NumPy
import numpy as np
from sklearn.linear_model import LogisticRegression

# Paso 2: preparamos los datos
X = np.array([0.5, 0.75, 1, 1.25, 1.5, 1.75, 1.75, 2, 2.25, 2.5, 2.75, 3, 3.25, 3.5, 4, 4.25, 4.5, 4.75, 5, 5.5]).reshape(-1,1)
y = np.array([0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1])
# Paso 3: importamos la clase LogisticRegresion de scikit-learn

# Paso 4: Creamos una instancia de la Regresión Logística
regresion_logistica = LogisticRegression()

# Paso 5: Entrena la regresión logística con los datos de entrenamiento
regresion_logistica.fit(X,y)
X_nuevo = np.array([1, 2, 3, 4, 5, 6]).reshape(-1,1)

# Paso 6: Usa el modelo entrenado para obtener las predicciones con datos nuevos
prediccion = regresion_logistica.predict(X_nuevo)
print(prediccion)
# produce el resultado: [0 0 1 1 1 1]
# Paso 7: Opcionalmente, obtén las probabilidades de la predicción
probabilidades_prediccion = regresion_logistica.predict_proba(X_nuevo)
print(probabilidades_prediccion)

# produce el siguiente resultado (la primera columna es 
# la probabilidad de suspender y la segunda columna es
# la probabilidad de aprobar)
# [[0.6801015  0.3198985 ]
#  [0.53568295 0.46431705]
#  [0.38502138 0.61497862]
#  [0.25359079 0.74640921]
#  [0.15566862 0.84433138]
#  [0.09095092 0.90904908]]

# Como seguramente estamos más interesados en la probabilidad de aprobar,
# podemos centrarnos en la segunda columna
print(probabilidades_prediccion[:,1])

# produce el resultado: [0.3198985  0.46431705 0.61497862 0.74640921 0.84433138 0.90904908]