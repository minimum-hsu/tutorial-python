#!/usr/bin/env python3

def remove_element(array: list[str], element: str) -> list[str]:
    '''Remove all occurrences of element from array.'''

    # Using list comprehension to create a new list without the specified element
    return [item for item in array if item != element]

def del_element(array: list[str], element: str) -> list[str]:
    '''Remove all occurrences of element from array using del statement.'''

    # Find all indices of the element to be removed
    indices_to_remove = [i for i, item in enumerate(array) if item == element]

    # Remove elements in reverse order to avoid index shifting
    for index in reversed(indices_to_remove):
        print("Removing element at index:", index)
        del array[index]
    return array

if __name__ == '__main__':
    sample_array = ['apple', 'banana', 'orange', 'banana', 'grape']
    element_to_remove = 'banana'

    print("Original array:", sample_array)

    new_array = remove_element(sample_array.copy(), element_to_remove)
    print("Array after remove_element:", new_array)

    modified_array = del_element(sample_array.copy(), element_to_remove)
    print("Array after del_element:", modified_array)