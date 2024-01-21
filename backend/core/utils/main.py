from fuzzywuzzy import fuzz


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


def is_name_similar(shop_name, existing_shop_names, similarity_threshold=90):
    for existing_name in existing_shop_names:
        if fuzz.ratio(shop_name.lower(), existing_name.lower()) >= similarity_threshold:
            return True
    return False