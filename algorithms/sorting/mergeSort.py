def merge_sort(canvas, data, draw, operations, left=0, right=None):
    if right is None:
        right = len(data) - 1

    if left < right:
        mid = (left + right) // 2
        # Llamada recursiva para ordenar la mitad izquierda
        yield from merge_sort(canvas, data, draw, operations, left, mid)
        # Llamada recursiva para ordenar la mitad derecha
        yield from merge_sort(canvas, data, draw, operations, mid + 1, right)
        # Combinar las dos mitades
        yield from merge(canvas, data, draw, operations, left, mid, right)

    # Cuando termina todo, dibujamos la lista ordenada
    if right == len(data) - 1:
        draw(canvas, data, [], True)
        yield
    else:
        draw(canvas, data, [], False)
        yield

def merge(canvas, data, draw, operations, left, mid, right):
    # Crear los subarreglos
    left_subarray = data[left:mid + 1]
    right_subarray = data[mid + 1:right + 1]

    i = j = 0
    k = left

    # Resaltar las sublistas que se están combinando
    draw(canvas, data, list(range(left, right + 1)), False)
    yield

    # Mezclar las dos sublistas
    while i < len(left_subarray) and j < len(right_subarray):
        operations[0] += 1  # Cuenta la comparación
        if left_subarray[i] <= right_subarray[j]:
            data[k] = left_subarray[i]
            i += 1
        else:
            data[k] = right_subarray[j]
            j += 1
        k += 1
        draw(canvas, data, list(range(left, right + 1)), False)
        yield

    # Si quedan elementos en la sublista izquierda
    while i < len(left_subarray):
        operations[0] += 1  # Cuenta la asignación
        data[k] = left_subarray[i]
        i += 1
        k += 1
        draw(canvas, data, list(range(left, right + 1)), False)
        yield

    # Si quedan elementos en la sublista derecha
    while j < len(right_subarray):
        operations[0] += 1  # Cuenta la asignación
        data[k] = right_subarray[j]
        j += 1
        k += 1
        draw(canvas, data, list(range(left, right + 1)), False)
        yield

    # Cuando se ha terminado de mezclar, podemos marcar como completado
    draw(canvas, data, [], False)
    yield