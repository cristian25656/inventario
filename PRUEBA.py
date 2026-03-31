nombres = []

while True:
    opcion = int(input("ELIGE OPCION"))
    if opcion == 1:
        nuevo = {}
        nuevo["nombre"] = input("Ingrese el nombre: ")
        nombres.append(nuevo["nombre"])
    elif opcion == 2:
        for i in nombres: 
            print(f"hola como estas {i}")
    elif opcion == 3:
          print("gracias por usar el programa")
          exit()
          

    elif opcion == 4:
        for nombre, valor in nuevo.items():
            print("buenos dias", nombre, valor)