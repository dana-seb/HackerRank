

# n = 9
# signed_int = 9
# size = sys.getsizeof(n)
# print(size)
# unsigned_int = signed_int + (2**-32)
# print(unsigned_int)
# print(2**-32)

n = 32

""" r = n - (len(str(t)))
string = str(0*r) + str(t)
print(string)
print("{:.32f}".format(int(string))) """




# x = 0
# z = 1

# x, z = z, x

t = '1001'
string = t.zfill(28)
# string = print("{:029d}".format(t))
string_one = []
for x in string:
    if x == str(0):
        string_one.append(1)
    elif x == str(1):
        string_one.append(0)
string_t = str(string_one)
string_two = string_t.replace(',', '')
print(int(string_two))
