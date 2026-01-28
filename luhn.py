def check_luhn(number):
    number = number.replace(" ", "").replace("-", "")
    digits = [int(d) for d in number]

    for i in range(len(number)-2, -1, -2):
        digits[i] *= 2

        if digits[i] > 9:
            digits[i] -= 9

    total = sum(digits)

    return total % 10 == 0
