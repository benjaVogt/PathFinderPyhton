from collections import deque

def is_walkable(matrix, x_position, y_position):
    size = len(matrix)

    inside_map = 0 <= x_position < size and 0 <= y_position < size
    if not inside_map:
        return False

    return matrix[x_position][y_position] != "#"


def get_neighbours(matrix, x_position, y_position):
    possible_directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]  # norte, sur, este, oeste

    neighbours = []
    for x_direction, y_direction in possible_directions:
        x_neighbour = x_position + x_direction
        y_neighbour = y_position + y_direction

        if is_walkable(matrix, x_neighbour, y_neighbour):
            neighbours.append((x_neighbour, y_neighbour))

    return neighbours


def reconstruct_path(parent_of, target_coordinates):
    path = []
    current_coordinates = target_coordinates

    while current_coordinates is not None:
        path.append(current_coordinates)
        current_coordinates = parent_of[current_coordinates]

    path.reverse()
    return path


def breadth_first_search(matrix, start_coordinates, target_coordinates, on_step=None):
    pending_coordinates = deque([start_coordinates])  # cola FIFO
    visited_coordinates = {start_coordinates}
    parent_of = {start_coordinates: None}
    exploration_order = [start_coordinates]

    while pending_coordinates:
        current_coordinates = pending_coordinates.popleft()  # saca del frente
        x_position, y_position = current_coordinates

        if on_step is not None:
            on_step(current_coordinates, visited_coordinates, pending_coordinates)

        if current_coordinates == target_coordinates:
            return reconstruct_path(parent_of, target_coordinates), visited_coordinates, exploration_order

        for neighbour_coordinates in get_neighbours(matrix, x_position, y_position):
            if neighbour_coordinates not in visited_coordinates:
                visited_coordinates.add(neighbour_coordinates)
                parent_of[neighbour_coordinates] = current_coordinates
                pending_coordinates.append(neighbour_coordinates)  # agrega al final
                exploration_order.append(neighbour_coordinates)

    return None, visited_coordinates, exploration_order


def depth_first_search(matrix, start_coordinates, target_coordinates, on_step=None):
    pending_coordinates = [start_coordinates]  # pila LIFO
    visited_coordinates = {start_coordinates}
    parent_of = {start_coordinates: None}
    exploration_order = [start_coordinates]

    while pending_coordinates:
        current_coordinates = pending_coordinates.pop()  # saca del tope
        x_position, y_position = current_coordinates

        if on_step is not None:
            on_step(current_coordinates, visited_coordinates, pending_coordinates)

        if current_coordinates == target_coordinates:
            return reconstruct_path(parent_of, target_coordinates), visited_coordinates, exploration_order

        for neighbour_coordinates in get_neighbours(matrix, x_position, y_position):
            if neighbour_coordinates not in visited_coordinates:
                visited_coordinates.add(neighbour_coordinates)
                parent_of[neighbour_coordinates] = current_coordinates
                pending_coordinates.append(neighbour_coordinates)  # agrega al tope
                exploration_order.append(neighbour_coordinates)

    return None, visited_coordinates, exploration_order