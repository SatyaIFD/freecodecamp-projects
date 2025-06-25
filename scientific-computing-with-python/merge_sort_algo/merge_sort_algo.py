def merge_sort(array):
    # Base case: If the array has one or no elements, it's already sorted
    if len(array) <= 1:
        return

    # Step 1: Divide the array into two halves
    middle_point = len(array) // 2
    left_part = array[:middle_point]
    right_part = array[middle_point:]

    # Step 2: Recursively sort both halves
    merge_sort(left_part)
    merge_sort(right_part)

    # Step 3: Merge the sorted halves
    left_array_index = 0
    right_array_index = 0
    sorted_index = 0

    # Compare elements from both halves and merge them in sorted order
    while left_array_index < len(left_part) and right_array_index < len(right_part):
        if left_part[left_array_index] < right_part[right_array_index]:
            array[sorted_index] = left_part[left_array_index]
            left_array_index += 1
        else:
            array[sorted_index] = right_part[right_array_index]
            right_array_index += 1
        sorted_index += 1

    # Copy any remaining elements from left_part
    while left_array_index < len(left_part):
        array[sorted_index] = left_part[left_array_index]
        left_array_index += 1
        sorted_index += 1

    # Copy any remaining elements from right_part
    while right_array_index < len(right_part):
        array[sorted_index] = right_part[right_array_index]
        right_array_index += 1
        sorted_index += 1


# Entry point of the program
if __name__ == '__main__':
    numbers = [4, 10, 6, 14, 2, 1, 8, 5]
    print('Unsorted array: ')
    print(numbers)
    
    merge_sort(numbers)  # Sort the list using merge sort
    
    print('Sorted array: ' + str(numbers))
