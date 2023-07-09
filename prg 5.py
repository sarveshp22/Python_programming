def is_subset(set_a, set_b):
    for element in set_a:
        if element not in set_b:
            return False
    return True

set_a = {1, 2, 3, 4}
set_b = {1, 2, 3}

result = is_subset(set_a, set_b)

print(result)
