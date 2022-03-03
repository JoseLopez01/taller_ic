first_work = float(input('Nota de su primer taller \n'))
second_work = float(input('Nota de su segundo taller \n'))
third_work = float(input('Nota de su tercer taller \n'))

test = float(input('Nota de su examen \n'))
final_work = float(input('Nota de su proyecto final \n'))

works_prom = (first_work + second_work + third_work) / 3

final_degree = (works_prom * 0.5) + (test * 0.3) + (final_work * 0.2)

print(f'Su nota final es {final_degree}')
