
def main():
    digit_list = ['2','3','4','5','6','7','8','9']
    alpha_phone_number = ''
    num_phone_number = ''
    alpha_phone_number = input('Enter the telephone ' \
                               'number in the format' \
                               ' XXX-XXX-XXXX: ')
    for ch in alpha_phone_number:
        if ch.isalpha():
            ch = ch.upper()
            if ch == 'A' or ch == 'B' or ch == 'C':
                index = 0
            elif ch == 'D' or ch == 'E' or ch == 'F':
                index = 1
            elif ch == 'G' or ch == 'H' or ch == 'I':
                index = 2
            elif ch == 'J' or ch == 'K' or ch == 'L':
                index = 3
            elif ch == 'M' or ch == 'N' or ch == 'O':
                index = 4
            elif ch == 'P' or ch == 'Q' or ch == 'R' or ch == 'S':
                index = 5
            elif ch == 'T' or ch == 'U' or ch == 'V':
                index = 6
            elif ch == 'W' or ch == 'X' or ch == 'Y' or ch == 'Z':
                index = 7
            ch = digit_list[index]
        num_phone_number = num_phone_number + ch
    print('The phone number is ', num_phone_number)
main()

