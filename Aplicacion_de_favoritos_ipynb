import json

ARCHIVO = "favoritos.json"

# ==============================
# FUNCIONES AUXILIARES
# ==============================

def cargar():
    """Carga los favoritos desde el archivo JSON o devuelve lista vacía"""
    try:
        f = open(ARCHIVO, "r")
        datos = json.load(f)
        f.close()
        return datos
    except:
        return []

def guardar(lista):
    """Guarda la lista de favoritos en el archivo JSON"""
    f = open(ARCHIVO, "w")
    json.dump(lista, f)
    f.close()

# ==============================
# FUNCIONES DEL MENÚ
# ==============================

def agregar():
    lista = cargar()
    titulo = input("Titulo: ")
    url = input("URL: ")
    comentario = input("Comentario: ")
    fav = {"titulo": titulo, "url": url, "comentario": comentario}
    lista.append(fav)
    guardar(lista)
    print("Agregado!")


            print(" Opción inválida")

# Ejecutar el menú
menu()
