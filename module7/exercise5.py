original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def filter_even_numbers(list_of_integers):
    even_numbers = []
    for n in list_of_integers:
        if n % 2 == 0:
            even_numbers.append(n)
    return even_numbers

filtered_list = filter_even_numbers(original_list)
print("Original list:", original_list)
print("List with even numbers only:", filtered_list)