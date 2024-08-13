"""arg1: 0=hojas, flores y frutos. 1=?. 2=tronco
rg2: 0=hojas"""


def paletacolor(config1, config2):
    import random
    import ColorMixer as ck

    primercolor = "#ff0000"
    segundocolor = "#ffff00"
    tercercolor = "#00ff00"
    cuartocolor = "#00ffff"
    quintocolor = "#0000ff"
    sextocolor = "#ff00ff"
    septimocolor = "#ff0000"

    cuantos = 128  # usar para hojas
    listacolorpuro = []

    colores = ck.mxc(primercolor, segundocolor, cuantos)
    listacolorpuro.extend(colores)
    colores = ck.mxc(segundocolor, tercercolor, cuantos, True)
    listacolorpuro.extend(colores)
    colores = ck.mxc(tercercolor, cuartocolor, cuantos, True)
    listacolorpuro.extend(colores)
    colores = ck.mxc(cuartocolor, quintocolor, cuantos, True)
    listacolorpuro.extend(colores)
    colores = ck.mxc(quintocolor, sextocolor, cuantos, True)
    listacolorpuro.extend(colores)
    colores = ck.mxc(sextocolor, septimocolor, cuantos, True, True)
    listacolorpuro.extend(colores)

    indicespuros = {
        "indicerojo": listacolorpuro.index(primercolor.upper()),  # 0
        "indiceamarillo": listacolorpuro.index(segundocolor.upper()),  # 1
        "indiceverde": listacolorpuro.index(tercercolor.upper()),  # 2
        "indicecian": listacolorpuro.index(cuartocolor.upper()),  # 3
        "indiceazul": listacolorpuro.index(quintocolor.upper()),  # 4
        "indicemagenta": listacolorpuro.index(sextocolor.upper()),  # 5
        "indicerojof": listacolorpuro.index(septimocolor.upper()),  # 6?
    }

    if config1 == 0:
        rangopuroselc = listacolorpuro
    elif config1 == 1:
        rangoA = listacolorpuro[
            : int(
                list(indicespuros.values())[4] - list(indicespuros.values())[4] / 3.5
            )  # f00-00ff7f (aproximado)
        ]

        rangoB = listacolorpuro[
            : int(
                list(indicespuros.values())[4] + list(indicespuros.values())[3] / 6
            ) : -1  # 8000ff-ff0000 (aproximado)
        ]
        rangoB = rangoB[::-1]
        rangopuroselc = rangoA + rangoB  # ADAPTARRLOOOO

    elif config1 == 2:
        rangoA = listacolorpuro[
            : int(
                list(indicespuros.values())[3] - list(indicespuros.values())[3] / 3.5
            )  # f00-00ff7f (aproximado)
        ]

        rangoB = listacolorpuro[
            : int(
                list(indicespuros.values())[5] + list(indicespuros.values())[2] / 6
            ) : -1  # 8000ff-ff0000 (aproximado)
        ]
        rangoB = rangoB[::-1]
        rangopuroselc = rangoA + rangoB  # mejorarlo

    prcolorseleccionado = random.choice(rangopuroselc)

    tonosgrisaceos = []

    primercolor = "#ffffff"
    segundocolor = "#000000"

    lista = ck.mxc(primercolor, segundocolor, 63)
    tonosgrisaceos.extend(lista)

    if config2 == 0:
        grisrangoselc = tonosgrisaceos[
            int(len(tonosgrisaceos) / 8) : int(len(tonosgrisaceos) * 3 / 4)
        ]

    grcolorseleccionado = random.choice(grisrangoselc)

    gradofinal = ck.mxc(prcolorseleccionado, grcolorseleccionado, int(cuantos / 2))

    rangoselc = gradofinal[int(len(gradofinal) / 4) : int(len(gradofinal) * 3 / 4)]

    def colorrandom(crrranpuro, crrangris):
        """Acá se selecciona un colorr aleatorio, el cual cumple con las reglas dadas."""
        rangoselcpr = random.choice(crrranpuro)  # color aleatorio tipo puro
        rangoselcgr = random.choice(crrangris)  # color aleatorio tipo gris
        colorf = ck.mxc(
            rangoselcpr, rangoselcgr, 32
        )  # se mezclan con una cantidad de 64
        indicef = colorf.index(colorf[-1])  # indice del ultimo elemento
        rangocolor = colorf[
            1 : int(indicef / 4)
        ]  # se usa un slice para obtener un rango en específico y asi no tener colores tan fuera de contexto
        indicerm = rangocolor.index(
            rangocolor[-1]
        )  # indice del ultimo elemento de la lista con slice
        indicef = random.randint(
            1, indicerm
        )  # indice al azar dentro del rango de indice 1 al ultimo elemento de la lista modificada
        colorf = colorf[indicef]  # seleccionar color especifico con el indice
        colorf = str(colorf)  # transformar colorf a str para mayor comodidad
        return colorf

    listafinalmodif = []

    # colorrd = "#814bA3"

    decision = random.choice([0, 1])

    if decision == 0:
        valorelec = colorrandom(listacolorpuro, tonosgrisaceos)
    elif decision == 1:
        valorelec = 1

    # valorelec = 0

    testindex = random.randint(4, 7)  # 2-7
    testindex = 7
    for color in rangoselc:
        if valorelec == 1:
            valorelec = ck.cpl(color)
        rangofinal = ck.mxc(color, valorelec, 32)
        rangofinalmodif = rangofinal[: int(32 / 2)]  # 32/4
        colorfinal = rangofinalmodif[testindex]
        listafinalmodif.append(colorfinal)

    return listafinalmodif


def modelos():
    print("2, 0: hojas")
