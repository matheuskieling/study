def main():
    card = input("Number: ")

    # American Express uses 15-digit numbers
    # All American Express numbers start with 34 or 37
    if len(card) == 15 and card.startswith("34") or card.startswith("37"):
        if validate(card):
            print("AMEX")
        else:
            print("INVALID")

    # MasterCard uses 16-digit numbers
    # Most MasterCard numbers start with 51, 52, 53, 54, or 55
    elif (
        len(card) == 16
        and card.startswith("51")
        or card.startswith("52")
        or card.startswith("53")
        or card.startswith("54")
        or card.startswith("55")
    ):
        if validate(card):
            print("MASTERCARD")
        else:
            print("INVALID")

    # Visa uses 13- and 16-digit numbers
    # all Visa numbers start with 4
    elif card.startswith("4") and len(card) == 13 or len(card) == 16:
        if validate(card):
            print("VISA")
        else:
            print("INVALID")

    else:
        print("INVALID")


def validate(card):
    """
    Luhn's Algo

    1. Multiply every other digit by 2, starting with the numbers
        second-to-last digit(odds), and then add those products digits together.

    2. Add the sum to the sum of the digits that werent multiplied by 2.

    If the totals last digit is 0 (or, put more formally, if the total
        modulo 10 is congruent to 0), the number is valid!
    """
    # iniciate variables
    even_num = []
    odd_num = []
    sum = 0

    # invert card number
    card = card[::-1]
    # for index and number in the card
    for index, number in enumerate(card):
        if (index + 1) % 2 == 0:
            # append number to even list
            even_num.append(number)
        else:
            # append number to odd list
            odd_num.append(number)
    # perform calculation of algorithm
    for number in odd_num:
        sum += int(number)
    for number in even_num:
        new_n = int(number) * 2
        for digit in str(new_n):
            sum += int(digit)
    return sum % 10 == 0


if __name__ == "__main__":
    main()
