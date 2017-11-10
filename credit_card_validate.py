print("We accept Visa, Mastercard, and Discovery.")
card_string = input("Please enter your card number: ")

card_string = card_string.replace(" ","")
card_string = card_string.replace("-","")
card = card_string

def card_check(card):
    if len(card) == 16:
        if card[0] == '4':
            if luhn_check(card) != 0:
                return("INVALID CARD")
            else:
                return("Valid card. Thank you!")

        elif card[0] == '5':
            if luhn_check(card) != 0:
                return("INVALID CARD")
            else:
                return("Valid card. Thank you!")

        elif card[0] == '6':
            if luhn_check(card) != 0:
                return("INVALID CARD")
            else:
                return("Valid card. Thank you!")
        else:
            return("Wrong starting number!")

    else:
        return("Wrong card length!")

def num_digits(card):
    return[int(i) for i in card]

def luhn_check(card):
    digits = num_digits(card)
    even_digits = digits[0::2]
    odd_digits = digits[1::2]

    for digits in card:
        sum_digits = 0
        sum_digits += sum(even_digits)
        for i in odd_digits:
            sum_digits += sum(odd_digits*2)
            return sum_digits % 10

print(card_check(card_string))
