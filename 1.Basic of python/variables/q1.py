## swap the value of two variables

a = int(input("Enter the value of a :"))
print(a);
b = int(input("Enter the value of b :"))
print(b);

print("\nBefore Swapping")
print("a =", a)
print("b =", b)

a, b = b, a

print("\nAfter Swapping")
print("a =", a)
print("b =", b)