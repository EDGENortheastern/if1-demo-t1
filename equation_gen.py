import random

def equation_gen():
    '''
    here goes docstring
    '''
    unknown_x = random.randint(1, 10)
    coef_a = random.randint(1, 10)
    result = coef_a * unknown_x
    return str(coef_a) + ' * x = ' + str(result), unknown_x

print("solve the equation " + equation_gen()[0])
user_input = int(input("x = "))
print(type(user_input))
print(type(equation_gen()[1]))
if user_input == equation_gen()[1]:
    print("Correct!")
else:
    print("Incorrect!")

    

