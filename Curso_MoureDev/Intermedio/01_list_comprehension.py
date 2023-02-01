### List Comprehension ###

my_original_list = [30, 35, 24, 62, 52, 17]
my_list = [i for i in my_original_list]
print(my_list)

my_list = [i for i in range(8)]
print(my_list)

my_range = range(8)
print(my_range)
print(list(my_range))


def sum_five(number):
    return number + 5


my_list = [sum_five(i) for i in range(8)]
print(my_list)
