def insertion_sort(canvas, data, draw, operations):
    n = len(data)
    
    for i in range(1, n):
        key = data[i]
        j = i - 1
        
        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            j -= 1
            operations[0] += 1
            draw(canvas, data, [j], False)
            yield
            
        data[j + 1] = key
        operations[0] += 1
        draw(canvas, data, [j + 1], False)
        yield
    
    draw(canvas, data, [], True)
    yield