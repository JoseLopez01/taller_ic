donation = float(input('Ingrese la donación \n'))

administration = donation * 0.35
systems = administration * 0.25
telecomunications = systems * 0.1
contability = donation - (administration + systems + telecomunications)

print(f'Presupuesto de administración {administration}')
print(f'Presupuesto de sistemas {systems}')
print(f'Presupuesto de telecomunicaciones {telecomunications}')
print(f'Presupuesto de contabilidad {contability}')
