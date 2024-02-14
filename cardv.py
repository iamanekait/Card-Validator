def luhn_checksum(card_number):
    def digits_of(n):
        return [int(d) for d in str(n)]

    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d * 2))
    return checksum % 10

def is_luhn_valid(card_number):
    return luhn_checksum(card_number) == 0

def is_valid_card(card_number):
    if len(card_number) < 13 or len(card_number) > 19:
        return False
    try:
        int(card_number)
    except ValueError:
        return False
    return is_luhn_valid(card_number)

def main():
    card_number = input("Enter your card number: ").strip()
    if is_valid_card(card_number):
        print("Valid card number.")
    else:
        print("Invalid card number.")

if __name__ == "__main__":
    main()
