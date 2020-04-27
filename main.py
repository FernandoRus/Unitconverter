user_name = input("Porfavor, introduzca su nombre: ")
print("Bienvenido al conversor de kilometros a millas, " + user_name + "!")

while True:
    print("Introduzca el número de kilómetros que desea convertir a millas. ¡Utilice únicamente un número!: ")

    km = input("Kilómetros: ")

    km = float(km.replace(",", "."))  # Cambia las comas por puntos en caso de que el usuario introduzca las comas.

    milles = km * 0.621371

    print("{0} kilometros is {1} milles.".format(km, milles))

    choice = input("¿Desea realizar otra conversión? (y/n): ")

    if choice.lower() != "y" and choice.lower() != "yes":
        print("¡ Vuelva Pronto !")
        break