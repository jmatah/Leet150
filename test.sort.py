#https://towardsdatascience.com/sorting-algorithms-with-python-4ec7081d78a1

def insertionSort(array):
    for i in range(1, len(array)):
        j = i-1
        while array[j] > array[i] and j >= 0:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = array[i]
    return array