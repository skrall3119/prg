def translator(number):
    parts = number.split('-')
    new_num = ''
    for item in parts:
        for char in item:
            if char.isalpha():
                if char in 'ABC':
                    new_num += '2'
                if char in 'DEF':
                    new_num += '3'
                if char in 'GHI':
                    new_num += '4'
                if char in 'JKL':
                    new_num += '5'
                if char in 'MNOP':
                    new_num += '6'
                if char in 'QRS':
                    new_num += '7'
                if char in 'TUV':
                    new_num += '8'
                if char in 'WXYZ':
                    new_num += '9'
            elif char.isdigit():
                new_num += str(char)
    print(new_num)
translator('AFI-KIT-XHTW')
