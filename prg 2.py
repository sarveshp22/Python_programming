def is_obtained_from_first_string(first_str, second_str):
    for char in second_str:
        if char not in first_str:
            return False
    return True

# Get the two strings from the user
first_str = input("Enter the first string: ")
second_str = input("Enter the second string: ")

# Check if the second string can be obtained from the first string
if is_obtained_from_first_string(first_str, second_str):
    print("YES")
else:
    print("NO")
