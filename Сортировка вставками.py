def insertion_sort(N):
    """
    Функция сортирукт массив от наименьшего к наибольшему элементу
    :param N - список из элементов, которые требуется отсортировать
    """
    for i in range(1, len(N)):
        currentValue = N[i]
        pos = i
        while pos > 0 and N [pos-1] > currentValue:
            N[pos] = N[pos-1]
            pos = pos -1
        N[pos] = currentValue
    return N
# Проверяем, что оно работает
random_list_of_nums = [12, 8, 3, 20, 11]  
insertion_sort(random_list_of_nums)  
print(random_list_of_nums)
