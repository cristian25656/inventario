#Semana 2
iterador = 1 #este lo utilizo para dar inicio al bucle y final. usando la condicion que sea diferente a 0, asi me aseguro que no se vaya a cerrar hasta que el cliente de salir.
inventario = [] 
precio = 0
cantidad = 0
can = 0
# son variables que creo para que me ayuden con el conteo (iteraciones) de las repeticiones. sirven para saber por ejermplo, cuantas veces se repitio o se coloco un precio con (can += 1)dentro del bucle y del condicional.
print("""  
Bienvenido.
Que accion desea realizar:
1.Agregar producto
2.Mostrar el inventario
3.calcular estadisticas
4.salir      
""") #utilizo los print afuera para que no aparezcan aparatozamente cada que el usuario elige una opcion.
while iterador != 0:
    try:   #el try/except lo utilizo para que mi programa no se detenga cuando el usuario coloque una letra donde va un int y le vuelva a saltar el input.
        opcion = int(input("Digite la opcion correspondiente: "))
        if opcion == 1:
            nuevo_producto = {}
            nuevo_producto["nombre"]= str(input("Digite el nombre del producto a agregar: ")) 
            can += 1
            nuevo_producto["precio"] = float(input("Digite el precio del producto: "))

            nuevo_producto["cantidad"] = int(input("Digite la cantidad del producto: "))
            inventario.append(nuevo_producto)
            print(nuevo_producto)
            precio += nuevo_producto["precio"] * nuevo_producto["cantidad"]        
        elif opcion == 2:
            if not inventario:
                print("inventario vacio")
            else:
                for i in inventario:
                    print(i)
        elif opcion == 3:
            valor_total = precio
            print(f"El valor total de todo el inventario contando todos los productos es {valor_total}")
            print(f"cantidad total de productos es {can}")
        elif opcion == 4:
            print("Que tenga buen resto de dia, lo esperamos pronto")
            iterador = 0
        else:
            print("Opcion no es valida")

    except ValueError:
        print("Error. Digite un valor valido")