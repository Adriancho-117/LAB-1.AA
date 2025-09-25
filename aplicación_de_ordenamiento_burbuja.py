# ==============================
# APLICACION DE ORDENAMIENTO BURBUJA
# ==============================

def burbuja(lista, ascendente=True):
    """
    Parámetros:
        lista (list): Lista de números a ordenar.
        ascendente (bool): 
            - True -> ordena de menor a mayor (ascendente).
            - False -> ordena de mayor a menor (descendente).
    
    devuelve:
        list: La lista ordenada.
    """
    n = len(lista)
    for i in range(n-1):            # Número de pasadas
        for j in range(n-i-1):      # Comparaciones en cada pasada
            # Intercambiar según el orden elegido
            if (ascendente and lista[j] > lista[j+1]) or \
               (not ascendente and lista[j] < lista[j+1]):
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista




# Pedir tamaño de la lista
n = int(input("Tamaño de la lista: "))

# Llenar la lista con valores del usuario
lista = [int(input(f"Valor {i+1}: ")) for i in range(n)]

print("\nLista original:", lista)

# Orden ascendente (se pasa una copia para no modificar la lista original)
asc = burbuja(lista[:], True)   
print("Orden ascendente:", asc)

# Orden descendente
desc = burbuja(lista[:], False) 
print("Orden descendente:", desc)
