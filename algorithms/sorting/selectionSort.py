def selection_sort(canvas, data, draw, operations):
    n = len(data)

    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            operations[0] += 1
            draw(canvas, data, [j, min_index], False)
            yield

            if data[j] < data[min_index]:
                min_index = j

        if min_index != i:
            data[i], data[min_index] = data[min_index], data[i]
            operations[0] += 1
            draw(canvas, data, [i, min_index], False)
            yield

    draw(canvas, data, [], True)
    yield