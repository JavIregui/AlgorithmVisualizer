def quick_sort(canvas, data, draw, operations, low=0, high=None):
    if high is None:
        high = len(data) - 1

    if low < high:
        pivot_index = yield from partition(canvas, data, draw, operations, low, high)
        yield from quick_sort(canvas, data, draw, operations, low, pivot_index - 1)
        yield from quick_sort(canvas, data, draw, operations, pivot_index + 1, high)

    if high == len(data) - 1:
        draw(canvas, data, [], True)
        yield
    else:
        draw(canvas, data, [], False)
        yield


def partition(canvas, data, draw, operations, low, high):
    pivot = data[high]
    draw(canvas, data, [high], False)
    yield

    i = low - 1

    for j in range(low, high):
        operations[0] += 1
        draw(canvas, data, [j, high], False)
        yield

        if data[j] < pivot:
            i += 1
            data[i], data[j] = data[j], data[i]
            operations[0] += 1
            draw(canvas, data, [i, j, high], False)
            yield

    data[i + 1], data[high] = data[high], data[i + 1]
    operations[0] += 1
    draw(canvas, data, [i + 1, high], False)
    yield

    return i + 1