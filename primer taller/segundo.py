year_user = int(input("Introduce un año: "))

if (year_user % 4 == 0 and year_user % 100 != 0) or (year_user % 400 == 0):
    print(f"El año {year_user} es bisiesto.")
else:
    print(f"El año {year_user} no es bisiesto.")




    