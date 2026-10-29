PATH FIELDING
Algoritmos: BFS y DFS (Implementados en Python puro)
1. Generación del Mapa (Procedural)
Técnica: Se utiliza el algoritmo Random Walk implementado completamente en Python puro con la ayuda de la librería nativa random.

Parámetro complexity: Define el comportamiento del caminante aleatorio.

Si complexity es bajo, el mapa es simple y directo (pocos giros, caminos más rectos).

Si complexity es alto, aumentan los giros abruptos y la cantidad de pasos, generando laberintos más enredados y llenos de paredes.

Estructura del mapa: Se maneja como una matriz (lista de listas), donde:

0 = Pared

1 = Camino transitable

2 = Salida o Meta

2. Algoritmos de Búsqueda (Encontrar la salida)
Los algoritmos están programados desde cero usando Python puro y estructuras nativas para garantizar el aprendizaje y el control total de la lógica:

BFS (Breadth-First Search / Amplitud):

Utiliza una cola FIFO con collections.deque.

Explora el mapa nivel por nivel, lo que le permite encontrar siempre el camino más corto hacia la salida.

DFS (Depth-First Search / Profundidad):

Utiliza una pila LIFO con las listas nativas de Python (.append() y .pop()).

Explora los pasillos hasta el fondo aplicando backtracking (retroceso) cada vez que choca con una pared.

3. ¿Por qué Python puro?
Cero dependencias externas: No requiere instalar librerías pesadas, lo que hace que el código sea fácil de ejecutar en cualquier entorno.

Control absoluto: Permite manipular libremente las coordenadas del mapa y ajustar el parámetro complexity exactamente como se desee sin las restricciones de librerías de terceros.