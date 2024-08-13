"""ColorKit es útil en la manipulación de colores,
aunque de momento es para cubrir mis necesidades, en el futuro añadiré mas cositas."""


def hex_to_rgb(hexcolor):
    """Convertir color en hexadecimal en RGB."""
    hexcolor = hexcolor.lstrip("#")
    return tuple(int(hexcolor[i : i + 2], 16) for i in (0, 2, 4))


htr = hex_to_rgb


def rgb_to_hex(rgbcolor):
    """Convertir color en RGB en hexadecimal."""
    return "#{:02x}{:02x}{:02x}".format(*rgbcolor)


rth = rgb_to_hex


def complementario(colorprocesar):
    """Obtener el complementario de un color."""
    complementariorgb = []
    colortupla = hex_to_rgb(colorprocesar)
    for cadauno in colortupla:
        valor = 255 - cadauno
        complementariorgb.append(valor)
    colortuplamodif = tuple(complementariorgb)
    colortupla = rgb_to_hex(colortuplamodif)
    return colortupla.upper()


cpl = complementario


def mixcolor(color1, color2, cantidad=1, noanadir=None, esultimo=None):
    """Mezclar colores con una cantidad específica."""

    def mix_color(color1, color2, ratio):
        rgb1 = hex_to_rgb(color1)
        rgb2 = hex_to_rgb(color2)
        mixed = tuple(int(c1 * (1 - ratio) + c2 * ratio) for c1, c2 in zip(rgb1, rgb2))
        return rgb_to_hex(mixed)

    listacolor = []

    cantidad = cantidad + 1
    for i in range(cantidad + 1):
        ratio = i / cantidad
        mixed_color = mix_color(color1, color2, ratio)
        listacolor.append(mixed_color.upper())

    if noanadir:
        listacolor.pop(0)

    if esultimo:
        listacolor.pop(-1)

    return listacolor


mxc = mixcolor


def isvalidcolor(color):
    """Verificar sí un color es válido o no."""
    try:
        color = htr(color)
        return True
    except ValueError:
        return False


ivc = isvalidcolor


def hex_to_cmy(color, porcentaje=True):
    color = color.lstrip("#")
    colormodif = complementario(color)
    if porcentaje is False:
        return colormodif
    else:
        colorlisto = []
        colormodif = hex_to_rgb(colormodif)
        for elemento in colormodif:
            elementofi = (elemento * 1) / 255
            if elementofi > 1:
                elementofi = 1
            elif elementofi < 0:
                elementofi = 0
            colorlisto.append(elementofi)
        return colorlisto


# htc = hex_to_cmy


# def hex_to_cmyk(color):
#     a = 90


# gtck = hex_to_cmyk
