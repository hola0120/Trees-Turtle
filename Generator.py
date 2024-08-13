import turtle
import random
import string
import paletagen as p

#I'm so sorry for this mess. Please, ignore it

# random.seed(123123123123) 

def set_seed(semilla=None):
    if semilla is None:
        semilla=random.randint(0,99999999999)
        random.seed()
    
    else:
        random.seed(semilla)
    
    return semilla

semillaconstante= set_seed() #Select a random int number as seed


t = turtle.Turtle()
v = turtle.Screen()
v.tracer(0)
t.penup()
t.goto(0, -150) #250
t.pendown()


def probrl(probl, probr):

    probl = probl / 100
    probr = probr / 100
    ciento = random.uniform(0, 1)
    if probr == 0:
        return "l"
    elif ciento < probl:
        return "l"
    elif probr == 0:
        pass
    elif ciento > probr:
        return "r"
    else:
        pass

def colortallo():
    colorlista = []
    with open("coloresext.txt", "r") as colortxt:
        for color in colortxt:
            colorlista.append(color.strip())
        color = random.choice(colorlista)
    
    return color

def coloreshojas(x, pkclrnd):
    paletahoja=p.paletacolor(0,0)
    return paletahoja


def modeloshojas(config, paletacolor, sentido, grosor, radio, cantidad, sector):
    """Acá se definen las formas y diseños de las hojas"""
    t.setheading(sentido)
    t.width(grosor)
    longitudcolor=len(paletacolor)
    indicex = random.randint(5, longitudcolor-1)
    indicey = indicex - 5

    if config == 0:  # predeterminado/circulo
        t.begin_fill()
        t.circle(random.randint(0, 5))
        t.fillcolor(paletacolor[indicex])
        t.end_fill()
    
    elif config == 1: #HOJAS aleatorias c/u
        t.setheading(sentido - 45)
        t.pencolor(paletacolor[indicex])
        cantidad = random.randint(1, 5)
        for _ in range(cantidad):
            for _ in range(2):
                t.begin_fill()
                t.circle(radio, 90)
                t.left(90)
                t.fillcolor(paletacolor[indicey])
                t.end_fill()
            t.left(random.randint(0, 180) / cantidad)

    elif config == 2:  # limon
        t.setheading(sentido - 45)
        t.pencolor(paletacolor[indicex])
        t.begin_fill()
        for _ in range(2):
            t.circle(radio, 90)
            t.left(90)
        t.fillcolor(paletacolor[indicey])
        t.end_fill()

    elif config == 3: #practicamente la 1, pero no aleatoria
        t.setheading(sentido - 45)
        t.pencolor(paletacolor[indicex])
        for _ in range(cantidad):
            for _ in range(2):
                t.begin_fill()
                t.circle(radio, 90)
                t.left(90)
                t.fillcolor(paletacolor[indicey])
                t.end_fill()
            t.left(sector / cantidad)



def coloresflor():
    """Acá se define la paleta de colores de las flores"""
    with open("coloresflor.txt", "r") as archivo:
        colores = []
        for linea in archivo:
            colores.append(linea.strip().split())

        indiceb = colores.index(["botones:"])

        revisarboton = colores[indiceb + 1 :]

    with open("coloresflor.txt", "r") as archivo:
        revisarpetalos = []
        for linea in archivo:
            if linea.startswith("botones:"):
                break
            revisarpetalos.append(linea.strip().split())
        revisarpetalos = revisarpetalos[1:]

        print(revisarboton)
        print(revisarpetalos)
    return revisarboton, revisarpetalos

def coloresfruto(x, pkclrnd): #https://hihayk.github.io/scale/#6/6/20/60/40/0/10/14/b1ba74/177/186/116/white (plantilla)
    """Acá se define la paleta de colores de los frutos"""

    with open("coloresfruto.txt", "r") as archivo:  # , encoding="utf-8"
        colores = []
        cantidadlineas = []
        for linea in archivo:
            colores.append(linea.strip().split())
            cantidadlineas.append(1)

        cantidadlineas = len(cantidadlineas)
        if pkclrnd:
            x = random.randint(0, cantidadlineas - 1)

        print(x)

        a = colores[x]
        listacolores = []
        for unidad in a:
            listacolores.append(unidad)

        return listacolores


def flor(
    num,
    radpetal,
    radio,
    color_boton,
    color_petalos,
    poso,
    config,
    b,
    h,
    ang_paral,
    grosor,
): #angleflower,
    """Acá se definen las formas y diseños de las floreS"""
    t.penup()
    t.goto(poso[0], poso[1] - radio * 1.05)
    t.setheading(random.randint(0, 360))
    t.pendown()
    t.width(grosor)  # 1.5, predeterminado = radio/2
    t.pencolor(color_petalos[1])
    if config == 0:  # predeterminado/anillo relleno/moneda
        grosor = grosor * 1.75
        t.pencolor(color_petalos[2])
        t.begin_fill()
        t.circle(radio * 3)  # 3
        t.fillcolor(color_boton[2])
        t.end_fill()
    elif config == 1:  # trebol
        for _ in range(num):
            t.begin_fill()
            for _ in range(3):
                t.circle(radpetal, 60)
                t.left(60)

            t.fillcolor(color_petalos[2])
            t.end_fill()
            t.left(360 / num)

        t.penup()
        t.goto(poso[0], poso[1] - radio)
        t.pendown()

        t.pencolor(color_boton[1])
        t.begin_fill()
        t.circle(radio)
        t.fillcolor(color_boton[2])
        t.end_fill()

    elif config == 2:  # trebol cuadrado
        for _ in range(num):
            t.begin_fill()
            for _ in range(4):
                t.circle(radpetal, 45)
                t.left(45)

            t.fillcolor(color_petalos[2])
            t.end_fill()
            t.left(360 / num)

        t.penup()
        t.goto(poso[0], poso[1] - radio)
        t.pendown()

        t.pencolor(color_boton[1])
        t.begin_fill()
        t.circle(radio)
        t.fillcolor(color_boton[2])
        t.end_fill()
    elif config == 3:  # trebol pentagonal
        for _ in range(num):
            t.begin_fill()
            for _ in range(5):
                t.circle(radpetal, 36)
                t.left(36)

            t.fillcolor(color_petalos[2])
            t.end_fill()
            t.left(360 / num)

        t.penup()
        t.goto(poso[0], poso[1] - radio)
        t.pendown()

        t.pencolor(color_boton[1])
        t.begin_fill()
        t.circle(radio)
        t.fillcolor(color_boton[2])
        t.end_fill()

    elif config == 4:  # "vainilla"

        for _ in range(num):
            t.begin_fill()
            for _ in range(2):
                t.circle(radpetal, 90)
                t.left(90)

            t.fillcolor(color_petalos[2])
            t.end_fill()
            t.left(360 / num)

        t.penup()
        t.goto(poso[0], poso[1] - radio)
        t.pendown()

        t.pencolor(color_boton[1])
        t.begin_fill()
        t.circle(radio)
        t.fillcolor(color_boton[2])
        t.end_fill()

    elif config == 5:  # genérica
        for _ in range(num):
            t.begin_fill()
            t.circle(radpetal * 0.75)
            t.left(360 / num)

            t.fillcolor(color_petalos[2])
            t.end_fill()

        t.penup()
        t.goto(poso[0], poso[1] - radio)
        t.pendown()

        t.pencolor(color_boton[1])
        t.begin_fill()
        t.circle(radio * 0.5)
        t.fillcolor(color_boton[2])
        t.end_fill()
    elif config == 6:  # rectangulo
        for _ in range(num):
            t.begin_fill()
            for _ in range(2):
                t.forward(b)
                t.left(90)
                t.forward(h)
                t.left(90)

            t.fillcolor(color_petalos[2])
            t.end_fill()
            t.left(360 / num)

        t.penup()
        t.goto(poso[0] + radio / 1.5, poso[1] - radio)
        t.pendown()

        t.pencolor(color_boton[1])
        t.begin_fill()
        t.circle(radio)
        t.fillcolor(color_boton[2])
        t.end_fill()

    elif config == 7:  # paralelogramo
        for _ in range(num):
            t.begin_fill()
            for _ in range(2):
                t.forward(b)
                t.left(ang_paral)
                t.forward(h)
                t.left(180 - ang_paral)

            t.fillcolor(color_petalos[2])
            t.end_fill()
            t.left(360 / num)

        t.penup()
        t.goto(poso[0] + radio / 1.5, poso[1] - radio)
        t.pendown()

        t.pencolor(color_boton[1])
        t.begin_fill()
        t.circle(radio)
        t.fillcolor(color_boton[2])
        t.end_fill()

    elif config == 8:  # triángulo interior
        for _ in range(num):
            t.begin_fill()
            for _ in range(3):
                t.circle(radpetal, 60)
                t.left(180)

            t.fillcolor(color_petalos[2])
            t.end_fill()
            t.left(360 / num)

        t.penup()
        t.goto(poso[0], poso[1] - radio)
        t.pendown()

        t.pencolor(color_boton[1])
        t.begin_fill()
        t.circle(radio)
        t.fillcolor(color_boton[2])
        t.end_fill()

    elif config == 9:  # hexagono
        for _ in range(num):
            t.begin_fill()
            for _ in range(6):
                t.circle(radpetal, 30)
                t.left(30)

            t.fillcolor(color_petalos[2])
            t.end_fill()
            t.left(360 / num)

        t.penup()
        t.goto(poso[0], poso[1] - radio)
        t.pendown()

        t.pencolor(color_boton[1])
        t.begin_fill()
        t.circle(radio)
        t.fillcolor(color_boton[2])
        t.end_fill()

def fruto(angulo,grosor,rad, paletacolor, posicion, config):
    """Acá se definen las formas y diseños de los frutos"""

    indicex=2

    colorA = paletacolor[indicex]
    colorB=paletacolor[indicex-1]

    t.penup()
    t.goto(posicion[0], posicion[1]-rad*1.05)
    t.pendown()
    t.setheading(angulo)
    radiomodif = random.uniform(0.25, 0.75)
    temppos = t.pos()
    if config == 0:  # Circulo
        t.pencolor(colorA)
        t.dot(rad)
        t.pencolor(colorB)
        t.dot(rad - rad * 0.25)

    if config == 1:  # pera
        t.pencolor(colorA)
        t.dot(rad)
        t.pencolor(colorB)
        t.dot(rad - rad * 0.25)

        t.forward(rad - rad * random.uniform(0.25, 0.75))
        t.pencolor(colorA)
        t.dot(rad * 0.75)
        t.pencolor(colorB)
        t.dot(rad * 0.75 - rad * 0.25)

    if config == 2:  # pera doble
        t.pencolor(colorA)
        t.dot(rad)
        t.pencolor(colorB)
        t.dot(rad - rad * 0.25)

        t.forward(rad - rad * radiomodif)
        t.pencolor(colorA)
        t.dot(rad * 0.75)
        t.pencolor(colorB)
        t.dot(rad * 0.75 - rad * 0.25)

    if config == 3:  # pera doble
        t.pencolor(colorA)
        t.dot(rad)
        t.pencolor(colorB)
        t.dot(rad - rad * 0.25)

        t.forward(rad - rad * radiomodif)
        t.pencolor(colorA)
        t.dot(rad * 0.75)
        t.pencolor(colorB)
        t.dot(rad * 0.75 - rad * 0.25)

        t.backward((rad - rad * radiomodif) * 2)
        t.pencolor(colorA)
        t.dot(rad * 0.75)
        t.pencolor(colorB)
        t.dot(rad * 0.75 - rad * 0.25)


def nombrecientifico():
    """Acá se genera el nombre científico"""
    c = "bcdfghjklmnpqrstvwxyz"
    c2 = "bcdfghjklmnpqrstvwxyz"
    v = "aeiou"
    v2 = "aeiou"

    def prefijo():
        # s = [letra + ". " for letra in string.ascii_uppercase]
        # s1 = random.choice(s)
        largo = random.randint(1, 4)
        letras = string.ascii_lowercase
        nombreprefijo = []
        for _ in range(largo):
            prelisto = random.choice(letras)
            nombreprefijo.append(prelisto)
        prefijolisto = "".join(nombreprefijo) + ". "
        return prefijolisto.capitalize()

    def sufijo():  # no estoy seguro si se llama "sufijo", pero es la segunda parte de un nombre cientifico
        largo = random.randint(3, 6)
        palabra = []

        # m = modelo de "silaba" (silaba en "" porque a veces no forma silaba, pero ya que)
        for _ in range(largo):
            sc = random.choice(c)
            sc2 = random.choice(c2)
            sv = random.choice(v)
            sv2 = random.choice(v2)
            silaba = [
                sc + sv + sv2,
                sv + sc + sv2,
                sc + sv + sc2,
                sv + sc,
                sc + sv,
                sv + sv2 + sc,
                sc + sv,
                sv + sv2,
                sv + sv,
                sv + sc + sc,
                sc + sc2 + sv,
            ]
            palabra.append(random.choice(silaba))

        return "".join(palabra).capitalize()

    return prefijo() + sufijo()

def tallo(ancho,color, modif, rangoangulo,rangoangulomayor,longitudrango,longitudrangocu):
    """Acá se comienza el árbol"""
    posinicial = []
    nodorama = []
    

    t.width(ancho)
    t.pencolor(color)
    t.setheading(90)
    angulo = random.randint(*rangoangulo)
    if modif:
        angulo = random.randint(*rangoangulomayor)
    longitud = random.randint(*longitudrango)
    posinicial.append(t.pos())
    print(posinicial)
    for _ in range(longitud):
        posi = []
        posi.append(t.pos())
        t.penup()
        t.goto(posi[0])
        t.setheading(random.randint(angulo - 15, angulo + 15))
        t.pendown()
        t.forward(longitudrangocu)
    nodorama.append(t.pos())
    return nodorama, posinicial

def rama1(nodos, ancho,divididonum,angulorango,longitudrango,longitudrangocu):
    """Acá empiezan las ramas"""
    sethr = []
    nodr = []
    print(nodos)
    t.width(ancho / divididonum)
    dividido = random.randint(1, 5)
    for _ in range(dividido):
        angulo = random.randint(*angulorango)
        t.penup()
        t.goto(nodos[0])
        t.pendown()
        longitud = random.randint(*longitudrango)
        for _ in range(longitud):
            t.penup()
            t.setheading(random.randint(angulo - 15, angulo + 15))
            t.pendown()
            t.forward(longitudrangocu)
            a = probrl(40, 60)
            if a == "l":
                nodr.append(t.pos())
                sethr.append(t.heading())
    return nodr, sethr

def rama2(nodos, ancho, facep,dividido,angulosumadorango,longitudrango,setheadingrango,longitudrangocu
):
    """Acá empiezan las ramificaciones"""
    sethr = []
    nodr = []
    print(facep)
    print(nodos)
    t.width(ancho / dividido)
    posnodo = 0
    for nodorama in nodos:
        # angulo = random.randint(50, 140)
        angulo = facep[posnodo]
        t.penup()
        angulo = angulo + random.randint(*angulosumadorango)
        t.setheading(angulo)
        t.goto(nodorama[0], nodorama[1])
        t.pendown()
        longitud = random.randint(*longitudrango)
        for _ in range(longitud):
            t.penup()
            t.setheading(angulo + random.randint(*setheadingrango))
            t.pendown()
            t.forward(longitudrangocu)
            a = probrl(40, 60)
            if a == "l":
                nodr.append(t.pos())
                sethr.append(t.heading())
        posnodo += 1
    return nodr, sethr

def rama3(nodos, ancho, facep,dividido,angulosumadorango,longitudrango,setheadingrango,longitudrangocu):
    """Acá terminan las ramificaciones"""
    sethr = []
    nodr = []
    print(facep)
    print(nodos)
    t.width(ancho / dividido)
    posnodo = 0
    for nodorama in nodos:
        angulo = facep[posnodo]
        t.penup()
        angulo = angulo + random.randint(*angulosumadorango)
        t.setheading(angulo)
        t.goto(nodorama[0], nodorama[1])
        t.pendown()
        longitud = random.randint(*longitudrango)
        for _ in range(longitud):
            t.penup()
            t.setheading(angulo + random.randint(*setheadingrango))
            t.pendown()
            t.forward(longitudrangocu)
            a = probrl(40, 60)
            if a == "l":
                nodr.append(t.pos())
                sethr.append(t.heading())
        posnodo += 1
    return nodr

def hojas(nodos, flutos,listacolor):
    """Acá se colocan las hojas"""
    nodsflu = []
    faceflu = []

    hjrangoradA, hjrangoradB = hjrangorad
    hjrangoangleA, hjrangoangleB = hjrangoangle
    for nodoint in nodos:
        colorelecto = random.choice(listacolor)
        t.pencolor(colorelecto)
        t.penup()
        t.goto(nodoint)
        tempos = t.pos()
        probflu = probrl(97.5, 2.5)

        if probflu == "r" and flutos:
            nodsflu.append(t.pos())
            faceflu.append(t.heading())

        if probflu == "l" or flutos is False:
            prob = probrl(50, 50)
            if prob == "l":
                posfinal = tempos[0] + random.randint(0, 5), tempos[1] + random.randint(
                    0, 3
                )
            if prob == "r":
                posfinal = tempos[0] - random.randint(0, 5), tempos[1] - random.randint(
                    0, 3
                )

            t.goto(posfinal)

            t.pendown()
            sense = random.randint(hjrangoangleA, hjrangoangleB)  # mejorar a futuro)
            widtpencil = 5
            rad = random.randint(hjrangoradA, hjrangoradB)

            modeloshojas(2, listacolor, sense, widtpencil, rad, cantidadhojas, sectorcircular)

    return nodsflu, faceflu


def fluto(posn, facen):
    """Acá comienza a poner las flores y/o frutos"""
    boton, petalo = coloresflor()
    boton = random.choice(boton)
    petalo = random.choice(petalo)
    debugflfr=[]
    for pose in posn:
        probflu = probrl(70, 30)
        if probflu == "l":
            flor(
                flcantidadpetalos,
                flradpetalos,
                flradboton,
                flcolorboton,
                flcolorpetalos,
                pose,
                flconfiguracion,
                flbase,
                flaltura,
                flanguloparalelogramo,
                flgrosorpencil,
            ) #anguloflor,

            debugflfr.append("flor")
        if probflu == "r":
            sentido= random.randint(franguloA, franguloB) 
            fruto(sentido, frgrosor,frradio, frpaletacolor,pose, frconfig)
            debugflfr.append("fruto")

    print(f"flor: {debugflfr.count("flor")}")
    print(f"fruto: {debugflfr.count("fruto")}")
  
def rztallo(ancho,color, modif, rangoangulo,rangoangulomayor,longitudrango,longitudrangocu):
    """Acá se comienza el árbol"""
    posinicial = []
    nodorama = []
    

    t.width(ancho)
    t.pencolor(color)
    # t.pencolor("red")
    t.setheading(-90)
    angulo = random.randint(*rangoangulo)
    if modif:
        angulo = random.randint(*rangoangulomayor)
    longitud = random.randint(*longitudrango)
    posinicial.append(t.pos())

    t.setheading(random.randint(*rangoangulo))
    t.forward(random.randint(*tlrangotalloinicial))

    print(posinicial) #asdhbvasgyfabdiy
    for _ in range(longitud):
        posi = []
        posi.append(t.pos())
        t.penup()
        t.goto(posi[0])
        t.setheading(random.randint(angulo - 15, angulo + 15))
        t.pendown()
        t.forward(longitudrangocu)
    nodorama.append(t.pos())
    return nodorama, posinicial

def rzrama1(nodos, ancho,divididonum,angulorango,longitudrango,longitudrangocu):
    """Acá empiezan las ramas"""
    sethr = []
    nodr = []
    print(nodos)
    t.width(ancho / divididonum)
    dividido = random.randint(1, 5)
    for _ in range(dividido):
        angulo = random.randint(*angulorango)
        t.penup()
        t.goto(nodos[0])
        t.pendown()
        longitud = random.randint(*longitudrango)
        for _ in range(longitud):
            t.penup()
            t.setheading(random.randint(angulo - 15, angulo + 15))
            t.pendown()
            t.forward(longitudrangocu)
            a = probrl(40, 60)
            if a == "l":
                nodr.append(t.pos())
                sethr.append(t.heading())
    return nodr, sethr

def rzrama2(nodos, ancho, facep,dividido,angulosumadorango,longitudrango,setheadingrango,longitudrangocu
):
    """Acá empiezan las ramificaciones"""
    sethr = []
    nodr = []
    print(facep)
    print(nodos)
    t.width(ancho / dividido)
    posnodo = 0
    for nodorama in nodos:
        angulo = facep[posnodo]
        t.penup()
        angulo = angulo + random.randint(*angulosumadorango)
        t.setheading(angulo)
        t.goto(nodorama[0], nodorama[1])
        t.pendown()
        longitud = random.randint(*longitudrango)
        for _ in range(longitud):
            t.penup()
            t.setheading(angulo + random.randint(*setheadingrango))
            t.pendown()
            t.forward(longitudrangocu)
            a = probrl(40, 60)
            if a == "l":
                nodr.append(t.pos())
                sethr.append(t.heading())
        posnodo += 1
    return nodr, sethr

def rzrama3(nodos, ancho, facep,dividido,angulosumadorango,longitudrango,setheadingrango,longitudrangocu):
    """Acá terminan las ramificaciones"""
    sethr = []
    nodr = []
    print(facep)
    print(nodos)
    t.width(ancho / dividido)
    posnodo = 0
    for nodorama in nodos:
        angulo = facep[posnodo]
        t.penup()
        angulo = random.randint(*angulosumadorango)
        t.setheading(angulo)
        t.goto(nodorama[0], nodorama[1])
        t.pendown()
        facetemp=t.heading()
        longitud = random.randint(*longitudrango)        
        for _ in range(longitud):
            t.penup()
            t.setheading(facetemp-random.randint(-15,15))
            t.pendown()
            t.forward(longitudrangocu)
            a = probrl(40, 60)
            if a == "l":
                nodr.append(t.pos())
                sethr.append(t.heading())
        posnodo += 1
    return nodr

def raiz(inicio,rznum):
    t.penup()
    t.goto(*inicio)
    # t.goto(0,250)
    t.pendown()
    t.setheading(-90)
    if rznum > 1:
        rzangulomodif=True
        print("Mayor")
    else:
        rzangulomodif=False
        print("Menor")
    rztlnodo, rztlinicio=rztallo(tlancho,tlcolor,rzangulomodif,rztlrangoangulo,rztlrangoangulomayor,rztllongitud,rztllongitudcu)
    # t.pencolor("blue")
    rzr2nodos, rzr2sentido=rzrama1(rztlnodo,tlancho,r1dividido,rzr1angulorango,rzr1longitudrango,rzr1longitudrangocu)
    # t.pencolor("green")
    r3nodos, r3sentido=rzrama2(rzr2nodos, tlancho, rzr2sentido,r2dividido,rzr2angulosumadorango,rzr2longitudrango,rzr2setheadingrango,rzr2longitudrangocu)
    # t.pencolor("magenta")
    rzrama3(r3nodos, tlancho, r3sentido,rzr3dividido,rzr3angulosumadorango,rzr3longitudrango,rzr3setheadingrango,rzr3longitudrangocu)

def esqueleto(degree):
    tlnodo, tlinicio = tallo(tlancho,tlcolor,degree,tlrangoangulo,tlrangoangulomayor,tllongitud,tllongitudcu)
    r2nodos, r2sentido = rama1(tlnodo, tlancho,r1dividido,r1angulorango,r1longitudrango,r1longitudrangocu)
    r3nodos, r3sentido = rama2(r2nodos, tlancho, r2sentido,r2dividido,r2angulosumadorango,r2longitudrango,r2setheadingrango,r2longitudrangocu)
    hjnodos = rama3(r3nodos, tlancho, r3sentido,r3dividido,r3angulosumadorango,r3longitudrango,r3setheadingrango,r3longitudrangocu)
    
    return tlinicio,hjnodos

#configuraciones flor:
flcolorboton, flcolorpetalos = coloresflor()
flcolorboton = random.choice(flcolorboton)
flcolorpetalos = random.choice(flcolorpetalos)
flradboton = round(random.uniform(0.5, 2), 1)  # predeterminado: 3
flradpetalos = round(random.uniform(4, 9), 1)  # predeterminado: 6
print(f"RADIOPETALOS: {flradpetalos}")
flcantidadpetalos = random.randint(2, 6)
flconfiguracion = random.randint(0, 9)
flbhselect = random.choice(["radpetalos", "diferentes"])
if flbhselect == "radpetalos":
    flbase = flradpetalos  # por defecto radpetalos # por flor de base cuadrilatera
    flaltura = flradpetalos  # por defecto radpetalos  # por flor de base cuadrilatera
else:
    flbase = random.randint(4, 9)
    flaltura = random.randint(4, 9)
flanguloparalelogramo = random.randint(
    10, 350
)  # 75=bonita,  90 y 270 = flor cuadrada #120 curiosa
flgrosorpencil = round(random.uniform(1, 4), 1)
flanguloflor = random.randint(0, 360)

#configuración fruto
frangulo= random.choice(
        [(0, 360), (0, 180), (45, 135), (75, 105), (180, 360), (225, 315), (255, 285)])
frradio = random.uniform(7,15) #2,6
frgrosor=round(random.uniform(0.5,1),1) #fr = round(random.uniform(4, 9), 1)
frx=0 #indice
frpaletacolor=coloresfruto(frx,True)
print(f"PALETA FRUTO: {frpaletacolor}")

print(frangulo)
franguloA, franguloB = frangulo

frconfig=random.randint(0,3)

t.hideturtle()

tlancho = random.randint(5, 30)
tlcolor = colortallo()
hjcolor= coloreshojas(0,True)
print(f"color lista hj: {hjcolor}")
hjrangorad = random.choice(
    [(1, 10), (1, 5), (5, 10), (3, 7), (10, 20)]
)  # MAÑANA VER ESTO PARA AÑADIR ANGULOS

#hjrangorad=(10,20) #mi favorito

hjrangoangle = random.choice(
    [(0, 360), (0, 180), (45, 135), (75, 105), (180, 360), (225, 315), (255, 285)]
)

cantidadhojas=random.randint(1,5)
sectorcircular=random.uniform(0,180)

# hjrangoangle=(225,315) #mi favorito
print(hjrangorad)
print(hjrangoangle)

#parametros tallo
tlrangotalloinicial=(10,11)

tlrangoangulo=(70,110)
tlrangoangulomayor=(60,150)
tllongitud=(10,40)
tllongitudcu=5

#parametros RamE1
r1dividido=1.5
r1angulorango=(45,135)
r1longitudrango=(25,60)
r1longitudrangocu=5


#parametros RamE2
r2dividido=2
r2angulosumadorango=(-45,45)
r2longitudrango=(10,25)
r2setheadingrango=(-15,15)
r2longitudrangocu=5

#parametros RamE3
r3dividido=3
r3angulosumadorango=(-45, 45)
r3longitudrango=(7,15)
r3setheadingrango=(-15,15)
r3longitudrangocu=5

#=======

#parametros tallo raiz
rztlrangoangulo=(-135,-45)
rztlrangoangulomayor=(-135,-45)
rztllongitud=(10,15)
rztllongitudcu=5
#añadir anchura

#parametros RamE1 raiz
rzr1dividido=1.5
rzr1angulorango=(-180,0)
rzr1longitudrango=(20,40)
rzr1longitudrangocu=5 #perrdfecto, creo)

#parametros RamE2 raiz
rzr2dividido=2
rzr2angulosumadorango=(-135,-45) #ver
rzr2longitudrango=(10,20)
rzr2setheadingrango=(45,135)
rzr2longitudrangocu=5

#parametros RamE3 raiz
rzr3dividido=3
rzr3angulosumadorango=(-135,-45)
rzr3longitudrango=(3,10)
rzr3setheadingrango=(-135,-45)
rzr3longitudrangocu=5

TLSrangoTallos=(1,4)

def pasto():
    t.pencolor("#209020")
    pos = t.pos()
    t.penup()
    t.goto(-1000,0)
    t.pendown()
    t.setheading(0)
    t.forward(20000)

# pasto()
# TLSrangoTallos=(20,21) 
def estructura(numero):
    if numero > 1:
        angulomodif=True
        print("Mayor")
    else:
        angulomodif=False
        print("Menor")
    talloinicio, nodoshj=esqueleto(angulomodif)    
    nodefr, facefr = hojas(nodoshj, True, hjcolor) #mejorar
    fluto(nodefr, facefr)  # fluto=flor+fruto
    raiz(talloinicio,1) #CAMBIARRRRRRRRRRRRRRRRRRRR

def arbol(numero):
    estructura(numero)
    

nserie=0    
for _ in range(random.randint(*TLSrangoTallos)): #(random.randint(1,4)):
    t.penup()
    t.goto(0, -250)
    t.pendown()
    nserie+=1
    arbol(nserie)

t.penup()
t.goto(-150,-275)
t.pendown()
spp= nombrecientifico()
t.pencolor("black")
t.write(spp, font=("Times New Roman", 20, "italic"), align="right")

flposicion = [-150, -200]

flor(
    flcantidadpetalos,
    flradpetalos * 3,
    flradboton * 3,
    flcolorboton,
    flcolorpetalos,
    flposicion,
    flconfiguracion,
    flbase * 3,
    flaltura * 3,
    flanguloparalelogramo,
    flgrosorpencil,
) #anguloflor,

frsentido= random.randint(franguloA, franguloB)
frpose=[-250, -180]
fruto(frsentido, frgrosor*3,frradio*3, frpaletacolor,frpose,frconfig)


v.update()
turtle.done()

#nota: fl= Flor, fr= Fruto, tl = Tallo, r1 = Ramificación Etapa 1, r2= Ramificación Etapa 2, r3= Ramificación Etapa 3, hj= Hoja, rz= Sistema de Raíces
#añadir parametro de colores, raices, nudos y yemas


print(semillaconstante)
