import json

ARCHIVO = "favoritos.json"   # Aquí se guardará la información en formato JSON

# ==============================
# FUNCIONES AUXILIARES
# ==============================

def cargar():
    """Carga los favoritos desde el archivo JSON o devuelve lista vacía"""
    try:
        # Abrimos el archivo en modo lectura
        f = open(ARCHIVO, "r")
        # Convertimos el contenido del JSON en lista/diccionario de Python
        datos = json.load(f)
        f.close()   # IMPORTANTE: siempre cerrar el archivo
        return datos
    except:
        # Si el archivo no existe o está vacío → devolvemos una lista vacía
        return []

def guardar(lista):
    """Guarda la lista de favoritos en el archivo JSON"""
    # Abrimos el archivo en modo escritura → esto sobreescribe lo anterior
    f = open(ARCHIVO, "w")
    # Guardamos la lista en formato JSON dentro del archivo
    json.dump(lista, f)
    f.close()   #   cerrar archivo para que se guarden los datos

# ==============================
# FUNCIONES DEL MENÚ
# ==============================

def agregar():
    # Primero cargamos la lista existente
    lista = cargar()
    # Pedimos los datos al usuario
    titulo = input("Titulo: ")
    url = input("URL: ")
    comentario = input("Comentario: ")
    # Creamos un diccionario con esos datos
    fav = {"titulo": titulo, "url": url, "comentario": comentario}
    # Agregamos el nuevo favorito al final de la lista
    lista.append(fav)
    # Guardamos la lista actualizada en el archivo
    guardar(lista)
    print("Agregado!")

def eliminar():
    lista = cargar()
    titulo = input("Titulo a eliminar: ")
    nueva = []
    # Recorremos la lista con un FOR
    #  El for se usa aquí para revisar favorito por favorito
    # y decidir si lo guardamos en la nueva lista o no
    for f in lista:
        if f["titulo"] != titulo:   # Si el título no coincide, lo conservamos
            nueva.append(f)
    # La lista nueva ya no contiene el favorito eliminado
    guardar(nueva)
    print(" Eliminado!")

def modificar():
    lista = cargar()
    titulo = input("Titulo a modificar: ")
    # FOR para recorrer toda la lista y encontrar el favorito con ese título
    for f in lista:
        if f["titulo"] == titulo:
            # Si lo encontramos → pedimos los nuevos datos
            f["titulo"] = input("Nuevo titulo: ")
            f["url"] = input("Nueva URL: ")
            f["comentario"] = input("Nuevo comentario: ")
    # Guardamos la lista actualizada
    guardar(lista)
    print("Modificado!")

def ver():
    lista = cargar()
    if len(lista) == 0:
        print(" No hay favoritos")
    else:
        print("\n=== LISTA DE FAVORITOS ===")
        #  FOR para recorrer la lista e imprimir cada favorito
        for f in lista:
            print("Titulo:", f["titulo"])
            print("URL:", f["url"])
            print("Comentario:", f["comentario"])
            print("----")   # Separador entre cada favorito

# ==============================
# MENÚ PRINCIPAL
# ==============================

def menu():
    while True:
        # Menú de opciones
        print("\n=== MENÚ DE FAVORITOS ===")
        print("1. Agregar favorito")
        print("2. Eliminar favorito")
        print("3. Modificar favorito")
        print("4. Ver favoritos")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        # Según lo que elija el usuario, llamamos a la función correspondiente
        if opcion == "1":
            agregar()
        elif opcion == "2":
            eliminar()
        elif opcion == "3":
            modificar()
        elif opcion == "4":
            ver()
        elif opcion == "5":
            print(" Saliendo del programa...")
            break
        else:
            
            print(" Opción inválida")

# Ejecutar el menú
menu()
