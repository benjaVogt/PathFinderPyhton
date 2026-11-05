Numpy:

Importar: import numpy as np


Creación de Arrays:

	np.array([1, 2, 3]): Crea un array desde una lista.
	np.zeros((3, 3)): Genera una matriz de ceros.
	np.ones((2, 4)): Genera una matriz de unos.
	np.arange(0, 10, 2): Crea un array con valores espaciados uniformemente (inicio, fin, paso).
	np.linspace(0, 1, 5): Crea un array con 5 valores equidistantes entre 0 y 1.
	np.random.rand(3, 3): Genera una matriz de números aleatorios entre 0 y 1.


Acceso y Manipulación

	arr[0] o arr[1, 2]: Accede a elementos por índice (unidimensional o multidimensional).
	arr.shape: Devuelve las dimensiones del array (filas, columnas, etc.).
	arr.reshape(2, 3): Cambia la forma del array sin cambiar sus datos.
	np.append(arr, [4, 5]): Añade elementos al final del array.
	np.insert(arr, 1, 99): Inserta el valor 99 en el índice 1.
	np.delete(arr, 1): Elimina el elemento en el índice 1. 


Operaciones Matemáticas

	arr + 1, arr * 2: Operaciones elemento a elemento.
	np.sum(arr): Suma todos los elementos.
	np.mean(arr): Calcula el promedio.
	np.max(arr) / np.min(arr): Encuentra el valor máximo o mínimo.
	np.sin(arr), np.cos(arr), np.exp(arr): Funciones trigonométricas y exponenciales aplicadas a cada elemento




Deque:

	Importar: from collections import deque



Operaciones básicas de inserción y eliminación:

	append(x): Agrega el elemento x al extremo derecho. 
	appendleft(x): Agrega el elemento x al extremo izquierdo. 
	pop(): Elimina y retorna el elemento del extremo derecho. 
	popleft(): Elimina y retorna el elemento del extremo izquierdo. 
	extend(iterable): Agrega múltiples elementos al extremo derecho desde un iterable. 
	extendleft(iterable): Agrega múltiples elementos al extremo izquierdo (en orden invertido). 
	clear(): Elimina todos los elementos, dejando el deque vacío. 
	

Acceso y manipulación adicional:

	index(x): Retorna la posición de la primera ocurrencia de x. 
	count(x): Cuenta el número de veces que aparece x. 
	rotate(n): Rota los elementos n pasos a la derecha (si n es positivo) o a la izquierda (si es negativo). 
	reverse(): Invierte el orden de los elementos in-place. 
	insert(i, x): Inserta x en el índice i (menos eficiente que en los extremos).





Random:

importar: import random


Funciones basicas:
	
	random.random(): Genera un número decimal (float) aleatorio entre 0.0 y 1.0. 
	random.randint(a, b): Devuelve un número entero aleatorio entre a y b (ambos incluidos). 
	random.choice(secuencia): Selecciona un elemento aleatorio de una lista, tupla o cadena. 
	random.shuffle(lista): Mezcla los elementos de una lista en un orden aleatorio (modifica la lista original). 
	random.seed(n): Establece una semilla inicial para que la secuencia de números sea reproducible en ejecuciones posteriores. 