ESTRUCTURA DEL PROYECTO

el proyecto se dividió en varios notebooks para, limpieza y mejor entenimiento de nuestros modelos
Notebooks.
	- Analisis Exploratorio
   		-data cleaning
		-feature engineering
		-visualización de datos
		-selección de caracteristicas significativas
		-división del dataset, en datos de entrenamiento, validación y pruebas		
	- SVM
		-Selección de hyperparamentros a base de experimentación.
		-Selección del mejor modelo en base a datos de validación.
		-Exportar modelo
	- Abol de Decision
		-Selección de hyperparamentros a base de experimentación.
		-Selección del mejor modelo en base a datos de validación
		-Exportar modelo
	- Naive Bayes
		-Modelos para algoritmo de naive bayes
		-Exportar función para el modelo elegido
	- Logistic Regression
		-Selección de hyperparametros
		-Regulaziación
		-Experimentación
		-Selección del mejor modelo para los datos de validación
		-Exportar sessión y grafo de tensorflow
	- Deployment
		-Prueba y validación final a travéz de métricas de todos los modelos anteriores, con el dataset de pruebas guardado
		 anteriormente
		-Ensemble Learning para votar y elegir el valor mas repetido entre las predicciones de los modelos
		-Simulación de deployment, importando los modelos guardados y realizando predicciones sobre los datos
		 de prueba, e inventados, tomando la desición. Mostrando salidas probabilisticas.
	- Conclusiones + Investigacion
		- contiene las investigaciones,conclusiones, problemas y experiencias realizando el proyecto

Otros archivos.py
Funciones globales para facilitar taréas globalFuncs.py
	-Mostrar y retornar matriz de confusión mas métricas del dataset de entrenamiento y validacion
	-Guardar en bitacora de excel correspondiente, las métricas de la experimentación de modelos

model_nb.py
model2_nb.py 
funciones que nos facilitan la obtención de predicciones para el modelo de nayve bayes ambos archivos
se encuentran en la subcarpeta llamada modelos.

Las bitacoras correspondientes se almacenan en la subcarpeta llamada bitacora
los modelos exportados, se almacenan en la subcarpeta llamada modelos