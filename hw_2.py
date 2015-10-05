

# 1st try: cycle inside a cycle ... inside definition of course

my_input_numbers_1 = [2, 3, 5, 11]
print my_input_numbers_1


def products(primes):
    my_output_1 = []
    for i in range(len(primes)):
        x = primes[i]
        if x not in my_output_1:
            my_output_1.append(x)
            self_const = 1
        else:
            self_const = 0

        my_output_1 += [
            x * my_output_1[j]
            for j in range(len(my_output_1) - self_const)
            if not x*my_output_1[j] in my_output_1
        ]
    return sorted(my_output_1)

print products(my_input_numbers_1)

my_input_numbers_1 = [1, 2, 4, 8]
print my_input_numbers_1

print products(my_input_numbers_1)
