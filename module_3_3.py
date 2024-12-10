def print_params(a=1, b='str', c=True):
    print(a, b, c)


values_list = [1, 2, 'str']
values_dict = {'a': 1, 'b': True, 'c': 345}
values_list_2 = [1, 'args']
print_params()
print_params(a=2, b='string', c=bool)
print_params(b=25)
print_params(c=[1, 2, 3])
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)
print_params('string',*values_list_2)