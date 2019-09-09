nom = int(input('Задай номер - '))
def factorial(nomer):
    if nomer == 0:
       return 1
    else:
       return nomer * factorial(nomer - 1)
print(factorial(nom))