# Convert takes an integer and returns a string rain sound that it represents based on the factors 3, 5, and 7.
# If there are no factors then return the number itself.
def convert(number: int) -> str:
    # If the number is less than zero factor it into positive and negative numbers, check for 3, 5, or 7 rain sounds.
    # If the number is zero, it can be considered to have infinite factors, and thus all rain sounds.
    # If the number is greater than zero check if 3, 5, or 7 rain sounds.
    # http://mathforum.org/library/drmath/view/68272.html

    # Build up rain sound result based on the factors of the input.
    result = ""
    if number % 3 == 0:
        result += "Pling"
    if number % 5 == 0:
        result += "Plang"
    if number % 7 == 0:
        result += "Plong"

    # If there were no factors result will be empty and return the input number.
    if len(result) == 0:
        return str(number)
    return result
