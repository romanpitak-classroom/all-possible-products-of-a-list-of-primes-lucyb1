

# 1st try: cycle inside a cycle ... inside definition of course

my_input_numbers_1 = [2, 3, 5, 11]
print my_input_numbers_1


def products(primes):
    my_output_1 = set()
    for x in primes:
        my_output_1.update(
            x * j
            for j in my_output_1.copy()
        )
        my_output_1.add(x)
    return sorted(my_output_1)

print products(my_input_numbers_1)

my_input_numbers_1 = [1, 2, 4, 8]
print my_input_numbers_1

print products(my_input_numbers_1)
