import re

def string_calculator(string):

    if re.match('-[0-9]+', string):
        print("negatives not allowed")
    separators = ',', '\\n'
    if "//" in string:
        sep_info = re.findall('//.+\n', string)[0]
        separators = sep_info.replace('//','').replace('\\n','')
        string = string.replace(sep_info, '')
    if not string:
        return 0
    if not any(separator in string for separator in separators):
        return int(string)
    return sum(int(number) for number in re.split('|'.join(separators), string))

print(string_calculator('1,2'))