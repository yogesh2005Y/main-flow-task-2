def sum_of_digits(n):
    return sum(int(d) for d in str(abs(n)))

n = int(input("Enter a number: "))
print("Sum of digits:", sum_of_digits(n))