# Define the merge_sort function that takes an array as input
def merge_sort(array):
    # Base case: If the array is of length 0 or 1, it's already sorted
    if len(array) <= 1:
        return
    
    # Find the middle point to divide the array into left and right parts
    middle_point = len(array) // 2
    left_part = array[:middle_point]
    right_part = array[middle_point:]

    # Recursively sort the left and right parts
    merge_sort(left_part)
    merge_sort(right_part)

    # Initialize pointers for the left part, right part, and the sorted part
    left_array_index = 0
    right_array_index = 0
    sorted_index = 0

    # Merge the two halves by comparing their elements and putting them in order
    while left_array_index < len(left_part) and right_array_index < len(right_part):
        if left_part[left_array_index] < right_part[right_array_index]:
            # If the left part's element is smaller, add it to the sorted part
            array[sorted_index] = left_part[left_array_index]
            left_array_index += 1
        else:
            # Otherwise, add the right part's element to the sorted part
            array[sorted_index] = right_part[right_array_index]
            right_array_index += 1
        sorted_index += 1

    # If there are remaining elements in the left part, add them to the sorted part
    while left_array_index < len(left_part):
        array[sorted_index] = left_part[left_array_index]
        left_array_index += 1
        sorted_index += 1
    
    # If there are remaining elements in the right part, add them to the sorted part
    while right_array_index < len(right_part):
        array[sorted_index] = right_part[right_array_index]
        right_array_index += 1
        sorted_index += 1

# This part executes if the script is run directly (not imported as a module)
if __name__ == '__main__':
    # Example usage of the merge_sort function
    numbers = [4, 10, 6, 14, 2, 1, 8, 5]  # Unsorted array
    print('Unsorted array: ')
    print(numbers)
    merge_sort(numbers)  # Sort the array
    print('Sorted array: ' + str(numbers))  # Print the sorted array
