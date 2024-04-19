def merge_sort(arr):
    # Verificar se a lista tem tamanho 1 ou menos
    if len(arr) <= 1:
        return arr
    # Dividir a lista ao meio
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)
    # Lista para armazenar o resultado final
def merge(left, right):
    result = []
    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result.extend(left[left_index:])
    result.extend(right[right_index:])

    return result
    # resultado final, onde uso da lista
if __name__ == "__main__":
    input_string = input("Digite os números inteiros separados por vírgula: ")
    lista = [int(num) for num in input_string.split(',')]

    print("Lista original:", lista)
    lista_ordenada = merge_sort(lista)
    print("Lista ordenada:", lista_ordenada)
