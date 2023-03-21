def merge(l1, l2):
    result = []
    i = 0
    j = 0
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            result.append(l1[i])
            i += 1
        else:
            result.append(l2[j])
            j += 1
    result += l1[i:]
    result += l2[j:]
    return result

print(merge([1, 2, 3, 8], [1, 3, 4, 5, 6, 7, 8, 9]))