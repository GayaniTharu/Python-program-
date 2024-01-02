def perform_arithmetic_operations(a, b):
    add_result = a + b
    sub_result = a - b
    mul_result = a * b
    div_result = a / b
    mod_result = a % b
    exp_result = a ** b

    print("Addition:", add_result)
    print("Subtraction:", sub_result)
    print("Multiplication:", mul_result)
    print("Division:", div_result)
    print("Modulus:", mod_result)
    print("Exponentiation:", exp_result)

if __name__ == "__main__":
    # You can change the values of a and b as needed
    a = 10
    b = 3
    perform_arithmetic_operations(a, b)
