def number_to_letter_mapping(number):
    """
    # Example usage:
    for i in range(1, 27):
    print(f"{i} = {number_to_letter_mapping(i)}")
    """
    if 1 <= number <= 26:
        return chr(number + 64)  # Convert to ASCII value of 'A' (65) - 1
    else:
        return "Invalid"


