#Primera parte
iterador = 1
while iterador != 0:
#se usa la variable para abrir el bucle y crearle una condicion, en este caso, que el iterador sea diferente de 0, para que el bucle se ejecute con normalidad.
    try:
        name = str(input("Enter the product name: "))
        price = float(input("Enter the price: "))
        amount = int(input("Enter the quantity: "))
        iterador = 0
    except ValueError:
        print("Error, digite un dato valido")

total_cost = price * amount
print(f"Producto: {name} | Precio: {price} | Cantidad: {amount} | Total: {total_cost} ")

#Esta es la primera parte del proyecto. Aqui el proyecto solo toma datos str(cadena de texto) int(enteros) y float(numeros flotantes).
#Pide el nombre de un producto que precio tiene y cuantas unidades se llevaran.
#Al final, se multiplica el precio por la cantidad para dar un resultado con "print".
#while junto a try/except los utilizo para que si el usuario digita un valor invalido se repita la pregunta.
 