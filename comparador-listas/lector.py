def listador_de_instagrams(path) -> list:
    with open(path, encoding = "UTF-8") as archivo_txt:

        lista_instagrams = archivo_txt.readlines()
        
    lista_instagrams = list(map(lambda instagram:instagram.split("\n"), lista_instagrams))

    lista_nombres_ig = []

    for i in range(len(lista_instagrams)):

        for j in range(len(lista_instagrams[i])):
            lista_nombres_ig.append(lista_instagrams[i][j])

    return lista_nombres_ig

lista_seguidores = listador_de_instagrams("comparador-listas/Seguidores.txt")
lista_seguidos = listador_de_instagrams("comparador-listas/Seguidos.txt")

lista_no_me_siguen = []

for i in range(len(lista_seguidos)):
    encontrado = False
    for j in range(len(lista_seguidores)):
        if lista_seguidos[i] == lista_seguidores[j]:
            encontrado = True
            break

    if encontrado == False:
        lista_no_me_siguen.append(lista_seguidos[i])

for instagram in lista_no_me_siguen:
    print("___________________________________")
    print(instagram)

print("___________________________________")
print("\n-----------------------------------")

cantidad_personas_sin_seguirme = len(lista_no_me_siguen)
if cantidad_personas_sin_seguirme != 1:
    cuenta = "cuentas"
else:
    cuenta = "cuenta"

print(f"No te siguen: {cantidad_personas_sin_seguirme} {cuenta}")
print("-----------------------------------\n")