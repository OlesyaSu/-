def merge_sort(M):
    if len(M) > 1:
        mid = len(M)//2 # определяем середину листа
        right = M[mid:] # разрезаем на половины
        left = M[:mid]

        merge_sort(right) # рекурсивно продолжаем разбивать до Len(list) = 1
        merge_sort(left)

        i, j, k = 0, 0, 0
        while i < len(right) and j < len(left): # начинаем объединять половины в один лист
            if left[j] > right[i]:
                M[k] = right[i]
                i += 1
            else:
                M[k] = left[j]
                j += 1
            k += 1

        while i < len(right): # добавляем остатки листа в конец списка
            M[k] = right[i]
            i += 1
            k += 1

        while j < len(left): # добавляем остатки листа в конец списка
            M[k] = left[j]
            j += 1
            k += 1
    return M
# Проверяем, что оно работает
random_list_of_nums = [12, 8, 3, 20, 11]  
merge_sort(random_list_of_nums)  
print(random_list_of_nums)
