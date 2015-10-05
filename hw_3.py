
# 3rd try: recursion

my_input_numbers_3 = [2, 3, 5, 11]
print my_input_numbers_3


def check_output(given_list):
    if given_list is None:
        return []
    else:
        return given_list


def products(primes, m_o_3=None):

    my_output_3 = check_output(m_o_3)
    x = primes[0]

    if x not in my_output_3:
        my_output_3.append(x)
        self_const = 1
    else:
        self_const = 0

    for i in range(len(my_output_3)-self_const):
        if not x*my_output_3[i] in my_output_3:
            my_output_3.append(x*my_output_3[i])

    if len(primes) > 1:
        products(primes[1:], my_output_3)

    return sorted(my_output_3)

print products(my_input_numbers_3)

my_input_numbers_1 = [1, 2, 4, 8]
print my_input_numbers_1

print products(my_input_numbers_1)
