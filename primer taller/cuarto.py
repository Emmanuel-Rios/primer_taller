precio_producto:float = float(input("Ingrese el precio del pructo: "))
porcentaje_descuento:int = int(input("Ingrese el descuento: "))


descuento:float = precio_producto * (porcentaje_descuento/100)

precio_final:float = precio_producto - descuento

print(str(precio_final))