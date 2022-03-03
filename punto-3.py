base_salary = float(input('Ingrese su sueldo \n'))
monthly_total = float(input('Ingrese su venta del mes \n'))

earned = monthly_total * 0.15

print(f'Su comisión es de {earned}')
print(f'Su pago de este mes es de  {earned + base_salary}')
