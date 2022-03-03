first_capital = float(input('Inversion de la primera persona \n'))
second_capital = float(input('Inversion de la segunda persona \n'))
third_capital = float(input('Inversion de la tercera persona \n'))

total = first_capital + second_capital + third_capital

first_percentage = first_capital / total
second_percentage = second_capital / total
third_percentage = third_capital / total

print(f'Porcentage primer inversionista {first_percentage}')
print(f'Porcentage segundo inversionista {second_percentage}')
print(f'Porcentage tercer inversionista {third_percentage}')
