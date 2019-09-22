#!/usr/bin/python3
def roman_to_int(roman_string):
    dicc_rom = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500,
                'M': 1000}
    rom = 0
    result = 0
    parameter = roman_string
    if type(parameter) is not str or len(parameter) is 0:
        return 0
    for i in parameter:
        if i in dicc_rom:
            value = dicc_rom[i]
        else:
            raise ValueError(
                "roman_string contains illegal character: " + parameter)

        if rom is 0:
            rom += value
            result += 1
            continue
        if i == 'L' or i == 'C':
            if parameter[result - 1] == 'X':
                value -= 20
        elif i == 'D' or i == 'M':
            if parameter[result - 1] == 'C':
                value -= 200
        elif i == 'V' or i == 'X':
            if parameter[result - 1] == 'I':
                value -= 2
        rom += value
        result += 1
    return rom
