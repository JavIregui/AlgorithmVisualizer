def bubble_sort(canvas, data, draw):
    n = len(data)

    for i in range(n):
        for j in range(n - i - 1):
            draw(canvas, data, [j, j+1], False)
            yield
            
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                draw(canvas, data, [j, j+1], False)
                yield

    draw(canvas, data, [], True)
    yield