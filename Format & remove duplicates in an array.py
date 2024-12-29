input_array = ["Panasonic ", " pensonic", "panasonic  ", " Haier", "electrolux", "Electrolux"]

# function to format data values
def normalize(array):
    nor_value = []
    for s in array:
        # trim space
        s = s.strip()
        # upercase the first character
        s = s.capitalize()
        # append s to nor_value list
        nor_value.append(s)
    return nor_value

# function to remove duplicate
def remove_duplicate(array):
    # for loop to access unique value
    unique_array = []
    for s in array:
        if s not in unique_array:
            unique_array.append(s)
    return unique_array
      
normalized_array = normalize(input_array)
unique_array = remove_duplicate(normalized_array)
unique_array = sorted(unique_array)
print(unique_array)