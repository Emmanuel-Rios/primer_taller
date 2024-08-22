ladoUno = float(input("Ingrese el lado uno: "))
ladoDos = float(input("Ingrese el lado dos"))
ladoTres = float(input("Ingrese el lado tres"))


if ladoUno == ladoDos == ladoTres:
        print("Es equilatero")
elif ladoUno == ladoDos or ladoUno == ladoTres or ladoDos == ladoTres:
        print("Es isoceles")
else:
    print("Es escaleno")