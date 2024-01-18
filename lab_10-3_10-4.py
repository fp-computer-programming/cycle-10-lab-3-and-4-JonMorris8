"""

Create a Python file named lab_10-3.py
*** You must write a comment for every chunk of code you write from now on along with your author tag***

Write a program that contains a function called double_stuff. The function should take a list as its only parameter.
When a list is passed as an argument to the function, the function should double each value in the list, regardless of its type
Write test cases to confirm that your function works when passed a list that:
Contains only integers
Contains integer and float values
Contains a combination of integer, string, and float values
"""

#author Jon Morris 

def double_stuff(input_list):
    """
    Double each value in the given list, regardless of its type.
    """
    doubled_list = [2 * item for item in input_list]
    return doubled_list

# Test case 1 List contains only integers
int_list = [1, 2, 3, 4]
result_int = double_stuff(int_list)
print(f"Original List: {int_list}")
print(f"Doubled List: {result_int}")
print()

# Test case 2 List contains integer and float values
mixed_list = [1, 2.5, 3, 4.8]
result_mixed = double_stuff(mixed_list)
print(f"Original List: {mixed_list}")
print(f"Doubled List: {result_mixed}")
print()

# Test case 3 List contains a combination of integer, string, and float values
mixed_types_list = [1, 'hello', 3.5, 4, 'world']
result_mixed_types = double_stuff(mixed_types_list)
print(f"Original List: {mixed_types_list}")
print(f"Doubled List: {result_mixed_types}")


_____________________________________________________________________________________________________________
"""
Create a Python file named lab_10-4.py

Write a program that contains a function called indexed_names. 
The function should take a list of names as its only parameter.
When a list is passed as an argument to the function,
the function should return a new list where each value is replaced by the index, 
followed by a color, space, and the original value
i.e. passing through ["John", "Jane", "Bob"] 
would return ["0: John", "1: Jane", "2: Bob"]
Write 2 test cases to confirm that your function works when passed a list that:
"""
#Author Jon Morris 
def indexed_names(names_list):

    #Replace each value in the given list with its index, followed by a color and the original value.
    
    indexed_list = [f"{index}: {name}" for index, name in enumerate(names_list)]
    return indexed_list

# Test case 1 List of names
names_list_1 = ["John", "Jane", "Bob"]
result_1 = indexed_names(names_list_1)
print(f"Original List: {names_list_1}")
print(f"Indexed List: {result_1}")
print()

# Test case 2 Another list of names
names_list_2 = ["Jon", "Naz", "Sean"]
result_2 = indexed_names(names_list_2)
print(f"Original List: {names_list_2}")
print(f"Indexed List: {result_2}")
