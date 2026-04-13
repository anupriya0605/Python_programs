def sum1(d):
    return sum(d.values())
n = int(input("Enter a number n: "))
my_dict = {}
for x in range(1, n + 1):
    my_dict[x] = x ** 2
print("Generated Dictionary:")
print(my_dict)
total = sum1(my_dict)
print("Sum of all values in dictionary:", total)
