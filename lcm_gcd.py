import math

def lcm_and_gcd(a, b):
    gcd_val = math.gcd(a, b)
    lcm_val = abs(a * b) // gcd_val
    return lcm_val, gcd_val

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
lcm, gcd = lcm_and_gcd(a, b)
print(f"LCM: {lcm}, GCD: {gcd}")