def is_armstrong_number(number):
    num_digit = len(str(number))
    result =0 
    for n in str(number):
        result += int(n) ** int(num_digit)
    return result == number

f = is_armstrong_number(153)
print(f)
# the number of digits in the number can be calculated using len function 
# iterate though the number 
