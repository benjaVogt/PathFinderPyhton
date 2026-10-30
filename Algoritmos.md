Algoritmos de búsqueda:
Vamos a implementar principalmente los algoritmos BFS y DFS para tener un contraste entre ambos y poder compararlos (además para que haya variedad en el proyecto). 

BFS: este algoritmo lo que hace es, en vez de explorar a ciegas hacia adelante, se va expandiendo de forma concéntrica y uniforme desde el Spawnpoint (S), como si fuera una gota de tinta cayendo en agua limpia. Se divide esencialmente en dos características: una Cola (Queue) de tipo FIFO (First-In, First-Out) y un diccionario o conjunto de Nodos Visitados. Este sería más o menos su funcionamiento paso a paso:

Inicialización: el spawnpoint es introducido a la Cola y es marcado como Visitado.
Bucle Principal: mientras la cola no esté vacía, BFS hace esto: 
Saca el primer nodo que esté al frente de la cola (lo llamaremos Nodo Actual)
¿Es la meta? Básicamente consultar si el Nodo Actual es igual al Endpoint (E). En caso de que sea verdadero, el algoritmo se detiene inmediatamente (encontró la ruta de forma exitosa).
Exploración de vecinos. En caso de que no sea la meta, simplemente mira las 4 casillas adyacentes y continúa en alguna de ellas de 


DFS: Este algoritmo lo que hace es crear un nodo raiz, y explorar lo mas profundo posible en cada rama antes de retroceder
Pasos Basicos: 
Visitar el nodo actual y marcarlo como visitado (para evitar bucles infinitos).
Exlporar exhaustivamente cada uno de los nodos adyacentes que no fueron visitados aun.
Retroceder cuando ya no queden vecinos sin visitar en esa rama para explorar otras.
Estructura de datos:
Utiliza una pila (“stack”) que funciona con un sistema LIFO (Last In First Out).
Formula:
	O(V + E)
	O: Es el encargado de medir como crece el tiempo a medida que el grafo se hace mas grande
	V: Representa el número total de nodos (círculos o puntos).
	E: Representa el número total de conexiones o líneas entre los nodos