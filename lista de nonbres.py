
# Lista de Nombres

nombres = []  # Lista donde se guardan los nombres


def agregar():
    nombre = input("Ingresa un nombre: ")
    nombres.append(nombre)
    print(f"'{nombre}' agregado correctamente.")


def mostrar():
    if len(nombres) == 0:
        print("La lista está vacía.")
    else:
        print("Nombres guardados:")
        for i, nombre in enumerate(nombres, start=1):
            print(f"  {i}. {nombre}")


def buscar():
    nombre = input("¿Qué nombre quieres buscar? ")
    if nombre in nombres:
        print(f" '{nombre}' SÍ está en la lista.")
    else:
        print(f" '{nombre}' NO está en la lista.")


def eliminar():
    mostrar()
    nombre = input("¿Qué nombre quieres eliminar? ")
    if nombre in nombres:
        nombres.remove(nombre)
        print(f"'{nombre}' eliminado.")
    else:
        print("Ese nombre no existe en la lista.")


# Menú principal
print("=== Lista de Nombres ===")

while True:
    print("\n1. Agregar nombre")
    print("2. Mostrar nombres")
    print("3. Buscar nombre")
    print("4. Eliminar nombre")
    print("5. Salir")

    opcion = input("\nElige una opción: ")

    if opcion == "1":
        agregar()
    elif opcion == "2":
        mostrar()
    elif opcion == "3":
        buscar()
    elif opcion == "4":
        eliminar()
    elif opcion == "5":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida, intenta de nuevo.")
