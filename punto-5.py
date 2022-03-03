net_students = int(input('Estudiantes en redes \n'))
design_students = int(input('Estudiantes en diseño \n'))
contability_students = int(input('Estudiantes en contabilidad \n'))

total = net_students + design_students + contability_students

net_percentage = (net_students / total) * 100
design_percentage = (design_students / total) * 100
contability_percentage = (contability_students / total) * 100

print(f'Porcentage en redes {net_percentage}%')
print(f'Porcentage en diseño {design_percentage}%')
print(f'Porcentage en contabilidad {contability_percentage}%')
