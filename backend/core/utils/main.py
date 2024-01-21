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


def is_name_similar(
        shop_name: str,
        existing_shop_names: list,
        similarity_threshold=75) -> list:
    similar_names = []

    for existing_name in existing_shop_names:
        if existing_name.lower() != shop_name.lower():
            similarity = fuzz.ratio(shop_name.lower(), existing_name.lower())
            if similarity >= similarity_threshold:
                similar_names.append({
                    shop_name: {
                        existing_name: similarity
                    }})
    return similar_names
