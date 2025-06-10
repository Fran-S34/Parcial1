# Busqueda recursiva
def esta_capitan_america(lista, indice=0):
    """
    Devuelve True si 'Capitan America' está en la lista, sino False.
    """
    # recorro la lista y no lo encuentro
    if indice == len(lista):
        return False

    # Si lo encuentro, corto el ciclo
    if lista[indice] == "Capitan America":
        return True

    return esta_capitan_america(lista, indice + 1)


# Listado recursivo
def listar_superheroes(lista, indice=0):
    """
    Imprime todos los superhéroes de forma recursiva.
    """
    # recorrí toda la lista
    if indice == len(lista):
        return

    # muestro el héroe actual
    print(lista[indice])

    listar_superheroes(lista, indice + 1)


# Lista
if __name__ == "__main__":
    heroes = [
        "Iron Man", "Hulk", "Thor", "Viuda Negra", "Capitan America",
        "Spider-Man", "Pantera Negra", "Doctor Strange", "Bruja Escarlata",
        "Vision", "Ant-Man", "Wasp", "Capitana Marvel", "Falcon", "Soldado del Invierno"
    ]

    # 1) ¿Está Capitán América?
    if esta_capitan_america(heroes):
        print(" Capitán América está en la lista")
    else:
        print(" Capitán América no está en la lista")

    # 2) Listar todos los héroes
    print("\nListado completo:")
    listar_superheroes(heroes)
