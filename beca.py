print("programa becas")
distancia_escuela=int (input("a que distancia vive de la escuela en km   "))
print(distancia_escuela)

cantidad_hermanos=int(input("introduzca cantidad hermanos con los que vive   "))
print(cantidad_hermanos)

ingresos_familiar_mensual=int (input("cual es el ingreso familiar mensual   "))
print(ingresos_familiar_mensual)

if distancia_escuela>20 and cantidad_hermanos>3 or ingresos_familiar_mensual<50000:
    print("corresponde beca 100%")
else:
    print("no corresponde beca")