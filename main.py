def comma(number):
    type = True
    if int(number) < 0:
        type = False
    number = abs(int(number))
    commas = 0
    number_list = list(str(number)[::-1])
    for i in range(1, len(number_list)+1):
        if (i%3==0) and i!=len(number_list)-commas:
            number_list.insert(commas+i, ',')
            commas+=1
    number = "".join(number_list)[::-1]
    if type == False:
        return('-' + number)
    else:
        return(number)

def clean(value):
    for character in value:
        if character == " ":
            value = value.replace(character, "")
    return value

try:
    test_number = int(clean(input("Please enter an integer to see it's factors: ").strip()))
except (ValueError, NameError):
    print("Exiting program since a valid integer was not entered...\n")
    exit()

numbers = []
if test_number > 0:
    for i in range(-test_number, test_number):
        if i != 0 and test_number % i == 0:
            if (i not in numbers) and ((test_number/i) not in numbers):
                numbers.append(i)
                numbers.append(test_number/i)
    print('Factors of {number}:'.format(number=test_number))

else:
    for i in range(test_number, -test_number):
        if i != 0 and test_number % i == 0:
            if (abs(i) not in numbers) and ((abs(test_number/i)) not in numbers):
                numbers.append(i)
                numbers.append(test_number/i)
    print('The negative sign (-) can go in either of the two numbers.')
    print('Factors of {number}: '.format(number=test_number))

for i in range(len(numbers)):
    if i % 2 == 0:
        print("     {original_number} = {number_one} x {number_two} ".format(number_one = comma(int(numbers[i])), number_two = comma(int(numbers[i+1])), original_number = comma(test_number)))
print('\n')
