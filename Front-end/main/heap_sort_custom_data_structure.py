# from ...PokeTypeAdvantage.main.Move import Move
import sys
sys.path.insert(0, '../../PokeTypeAdvantage/PokeTypeAdvantage')
import Move




def heapify(to_heapify: list[Move], size, index):
    largest = index
    left = 2 * index + 1
    right = 2 * index + 2

    # largest_value = to_heapify[largest]
    # left_value = to_heapify[left]
    # right_value = to_heapify[right]

    # if to_heapify[largest] == None:
    #     largest_value = 0
    # if to_heapify[left] == None:
    #     left_value = 0
    # if to_heapify[right] == None:
    #     right_value = 0


    if left < size and __true_power(to_heapify, left) > __true_power(to_heapify, largest):
        largest = left

    if right < size and __true_power(to_heapify, right) > __true_power(to_heapify, largest):
        largest = right
    
    if largest != index:
        temp = to_heapify[index]
        to_heapify[index] = to_heapify[largest]
        to_heapify[largest] = temp

        heapify(to_heapify, size, largest)

def __true_power(to_heapify: list[Move], index: int):
    if to_heapify[index].power == None:
        return 0
    else:
        return to_heapify[index].power


def heap_sort_custom(moves_to_sort: list[dict[list[Move]]]):
    for pokemon_moves in moves_to_sort:
        for efficacy in pokemon_moves.values():
            heap_sort(efficacy)

    return moves_to_sort

    
    
def heap_sort(to_sort: list[Move]):
    size = len(to_sort)

    for i in range(size//2 - 1, -1, -1):
        heapify(to_sort, size, i)
    
    for i in range(size - 1, 0, -1):
        temp = to_sort[i]
        to_sort[i] = to_sort[0]
        to_sort[0] = temp
        heapify(to_sort, i, 0)