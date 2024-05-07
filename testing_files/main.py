def run_test (funcName, inputs, funcOutput, expectedOutput, testNumber):
    print(f"[Testing {funcName} - Test {testNumber}] --------------")
    if funcOutput == expectedOutput:
        print(f"\t+ Passed +")
    else:
        print(f"\t- Failed -")
    print("Expected Output:", expectedOutput)
    print("Actual Output:", funcOutput)
    print("Inputs:", inputs)
    print("---------------------------------")


def heapify(to_heapify, size, index):
    largest = index
    left = 2 * index + 1
    right = 2 * index + 2

    if left < size and to_heapify[left] > to_heapify[largest]:
        largest = left

    if right < size and to_heapify[right] > to_heapify[largest]:
        largest = right
    
    if largest != index:
        temp = to_heapify[index]
        to_heapify[index] = to_heapify[largest]
        to_heapify[largest] = temp

        heapify(to_heapify, size, largest)



def heap_sort(to_sort):
    size = len(to_sort)

    for i in range(size//2 - 1, -1, -1):
        heapify(to_sort, size, i)
    
    for i in range(size - 1, 0, -1):
        temp = to_sort[i]
        to_sort[i] = to_sort[0]
        to_sort[0] = temp
        heapify(to_sort, i, 0)
    
    return to_sort # Since python's memory layout lets you manipulate this same array, maybe you don't need to return it? But I think it's usually expected.



def main():
    L1 = [5, 1, 3] # Basic tree
    L2 = [5, 1, 3, 10, 7] # Tests Larger right tree | Unique values
    L3 = [5, 1, 3, 4, 5, 10, 7] # Tests when a value is not unique
    L4 = [10, 6, 3, 4, 7, 1, 2, 5, 9, 8]
    L5 = [1, 5, 3]
    L7 = [1, 3, 5]
    L6 = [3, 1, 5]
    L8 = [5, 1, 10, 4, 5, 3, 7]
    L9 = [9, 3, 6, 1, 7]
    L10 = [25, 11, 36, 8, 17]

    run_test("heap_sort", (L1.copy()), heap_sort(L1), [1, 3, 5], 1)
    

if __name__ == "__main__":
    main()