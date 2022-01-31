def buble_sort(arr):
    """
    Функция сортирует массив от наименьшего к наибольшему элементу
    :param arr - список из элементов, которые требуется отсортировать
    """
    
    L = len(arr)
    for i in range(L - 1):
        for j in range(L - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr 
# Проверяем, что оно работает
random_list_of_nums = [12, 8, 3, 20, 11]  
buble_sort(random_list_of_nums)  
print(random_list_of_nums)
