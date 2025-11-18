def decimal_to_binary(decimal_num):
    """
    Converts a positive integer from decimal to binary.
    """
    if decimal_num == 0:
        return "0"

    binary_result = ""
    while decimal_num > 0:
        remainder = decimal_num % 2

        binary_result = str(remainder) + binary_result

        decimal_num = decimal_num // 2

    return binary_result

try:
    decimal_input = input("Enter a positive whole number (decimal): ")

    number = int(decimal_input)

    if number < 0:
        print("Please enter a positive whole number.")
    else:

        binary_output = decimal_to_binary(number)
        print(f"The decimal number {number} is {binary_output} in binary.")

except ValueError:
    print("Invalid input. Please enter a valid whole number.")