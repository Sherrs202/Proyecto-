# Proyecto
# Bibliotecas
from prettytable import PrettyTable  # type: ignore


"""
================== Diccionarios =====================================
Estos diccionarios sirven como una base de datos que ayuda
a identificar el precio y tipo de bebidas disponibles.
"""


Tequila = {
    "Nombre": "Tequila",
    "Tipo": {
        "Centenario plata": {"Precio": 90},
        "Centenario azul": {"Precio": 90},
        "Centenario reposado": {"Precio": 90},
        "Cuervo especial": {"Precio": 90},
        "Cuervo plata": {"Precio": 90},
        "Herradura antiguo": {"Precio": 100},
        "Hornitos reposado": {"Precio": 100},
        "Tradicional reposado": {"Precio": 100},
        "Tradicional plata": {"Precio": 100},
        "Maestro dobel": {"Precio": 130},
        "Don julio reposado": {"Precio": 130},
        "1800 Cristalino": {"Precio": 150},
        "Don julio 70": {"Precio": 170}
    }
}

Cerveza = {
    "Nombre": "Cerveza",
    "Tipo": {
        "Corona": {"Precio": 55},
        "Victoria": {"Precio": 55},
        "Ligth": {"Precio": 60},
        "Ultra": {"Precio": 60},
        "Pacifico": {"Precio": 60},
        "Modelo especial": {"Precio": 60},
        "Modelo oscura": {"Precio": 60},
        "Ambar": {"Precio": 60},
        "Estela": {"Precio": 60}
    }
}

Whisky = {
    "Nombre": "Whisky",
    "Tipo": {
        "JB": {"Precio": 90},
        "Black n white": {"Precio": 90},
        "Etiqueta roja": {"Precio": 100},
        "Jacks daniels": {"Precio": 100},
        "Chivas 12": {"Precio": 130},
        "Buchanas": {"Precio": 150},
        "Etiqueta negra": {"Precio": 170},
        "Glenfuddich": {"Precio": 200},
        "Glenlivet 12 doble oak": {"Precio": 200}
    }
}

Ron = {
    "Nombre": "Ron",
    "Tipo": {
        "Apppleton state": {"Precio": 90},
        "Flor de caña 4": {"Precio": 90},
        "Matusalen clasico": {"Precio": 90},
        "Matusalen platino": {"Precio": 190},
        "Ron potosi": {"Precio": 90},
        "Appleton esp": {"Precio": 90},
        "Bacardi blanco": {"Precio": 90},
        "Bacardi añejo": {"Precio": 90},
        "Bacardi solera": {"Precio": 90},
        "Castillo": {"Precio": 90},
        "Malibu": {"Precio": 90},
        "Appleton blanco": {"Precio": 90},
        "Flor de caña blanco": {"Precio": 90},
        "Flor de caña 7": {"Precio": 95},
        "Mastusalen gran reserva": {"Precio": 100},
        "Havanna club 7": {"Precio": 100},
        "Bacardi 8": {"Precio": 135},
        "Zacapa 23": {"Precio": 220}
    }
}

Brandy = {
    "Nombre": "Brandy",
    "Tipo": {
        "Presidente": {"Precio": 80},
        "Don pedro": {"Precio": 80},
        "Torres 5": {"Precio": 90},
        "Torres 10": {"Precio": 90},
        "Azteca de oro": {"Precio": 90},
        "Terry": {"Precio": 90},
        "Fundador": {"Precio": 90},
        "Parris-torres": {"Precio": 100}
    }
}

Vodka = {
    "Nombre": "Vodka",
    "Tipo": {
        "Ocsolut LALO": {"Precio": 60},
        "Stolichnaya": {"Precio": 90},
        "Absolut": {"Precio": 90},
        "Oso negro": {"Precio": 90},
        "Smirnoff": {"Precio": 90}
    }
}

Mezcal = {
    "Nombre": "Mezcal",
    "Tipo": {
        "400 conejos": {"Precio": 130},
        "Gusano rojo": {"Precio": 130},
        "Naksir": {"Precio": 130}
    }
}

Gin = {
    "Nombre": "Gin",
    "Tipo": {
        "Oso negro gin": {"Precio": 90},
        "Beefeater": {"Precio": 100},
        "Tanqueray": {"Precio": 130}
    }
}

Anis = {
    "Nombre": "Anis",
    "Tipo": {
        "Mico dulce": {"Precio": 90},
        "Sambuca vaccari": {"Precio": 100},
        "Chichon dulce": {"Precio": 125}
    }
}


"""
================== Lista =====================================
Esta lista sirve para buscar las bebidas por su nombre.
"""

bebidas = [
    Tequila, Cerveza, Whisky, Ron,
    Brandy, Vodka, Mezcal, Gin, Anis
]


"""
================== Funciones precio y buscar ==========================
"""


def propina(porcentaje, subtotal):
    """Calcula la propina según el porcentaje indicado."""
    return porcentaje * subtotal / 100


def total(propina_valor, subtotal):
    """Devuelve el total a pagar con propina."""
    return propina_valor + subtotal


def buscar(bebida, tipo):
    """Busca el precio de una bebida y tipo específico."""
    for i in bebidas:
        if i["Nombre"].lower() == bebida.lower():
            for tip, dat in i["Tipo"].items():
                if tip.lower() == tipo.lower():
                    return dat["Precio"]
            return "No tenemos ese tipo."
    return "Bebida no registrada."


def mostrar_tipos(bebida):
    """Muestra los tipos disponibles de una bebida en una tabla."""
    tabla = PrettyTable()
    tabla.field_names = ["N°", "Tipo", "Precio"]
    tipos = list(bebida["Tipo"].keys())

    for i, tipo in enumerate(tipos, start=1):
        precio = bebida["Tipo"][tipo]["Precio"]
        tabla.add_row([i, tipo, precio])

    print(f"\nTipos de {bebida['Nombre']}:")
    print(tabla)
    return tipos


"""
================== Variables =====================================
"""

total_tequila = 0
total_cerveza = 0
total_whisky = 0
total_ron = 0
total_brandy = 0
total_vodka = 0
total_mezcal = 0
total_gin = 0
total_anis = 0
suma_total = 0


r = input("¿Quiere registrar una bebida? (S/N): ").strip().upper()


"""
================== Código principal ===================================
"""

while r == "S":
    print(
        "\n¿Qué bebida quieres?\n"
        "Tequila\nCerveza\nWhisky\nRon\nBrandy\n"
        "Vodka\nMezcal\nGin\nAnis"
    )
    bebida = input().capitalize()

    if bebida == "Tequila":
        mostrar_tipos(Tequila)
        tipo = input("\n¿Qué tequila quieres?: ")
        precio = buscar(bebida, tipo)
        suma_total += precio
        total_tequila += 1

    elif bebida == "Cerveza":
        mostrar_tipos(Cerveza)
        tipo = input("\n¿Qué cerveza quieres?: ")
        precio = buscar(bebida, tipo)
        suma_total += precio
        total_cerveza += 1

    elif bebida == "Whisky":
        mostrar_tipos(Whisky)
        tipo = input("\n¿Qué whisky quieres?: ")
        precio = buscar(bebida, tipo)
        suma_total += precio
        total_whisky += 1

    elif bebida == "Ron":
        mostrar_tipos(Ron)
        tipo = input("\n¿Qué ron quieres?: ")
        precio = buscar(bebida, tipo)
        suma_total += precio
        total_ron += 1

    elif bebida == "Brandy":
        mostrar_tipos(Brandy)
        tipo = input("\n¿Qué brandy quieres?: ")
        precio = buscar(bebida, tipo)
        suma_total += precio
        total_brandy += 1

    elif bebida == "Vodka":
        mostrar_tipos(Vodka)
        tipo = input("\n¿Qué vodka quieres?: ")
        precio = buscar(bebida, tipo)
        suma_total += precio
        total_vodka += 1

    elif bebida == "Mezcal":
        mostrar_tipos(Mezcal)
        tipo = input("\n¿Qué mezcal quieres?: ")
        precio = buscar(bebida, tipo)
        suma_total += precio
        total_mezcal += 1

    elif bebida == "Gin":
        mostrar_tipos(Gin)
        tipo = input("\n¿Qué gin quieres?: ")
        precio = buscar(bebida, tipo)
        suma_total += precio
        total_gin += 1

    elif bebida == "Anis":
        mostrar_tipos(Anis)
        tipo = input("\n¿Qué anis quieres?: ")
        precio = buscar(bebida, tipo)
        suma_total += precio
        total_anis += 1

    else:
        print("Bebida no registrada.")

    respuesta = input("\n¿Registrar otra bebida? (S/N): ").strip().upper()
    if respuesta == "N":
        break


if r == "N":
    print("No debes nada.")
else:
    print(
        "\nConsumo total:\n"
        f"{total_tequila} Tequila(s)\n"
        f"{total_whisky} Whisky(s)\n"
        f"{total_cerveza} Cerveza(s)\n"
        f"{total_ron} Ron(es)\n"
        f"{total_brandy} Brandy(s)\n"
        f"{total_vodka} Vodka(s)\n"
        f"{total_mezcal} Mezcal(es)\n"
        f"{total_gin} Gin(s)\n"
        f"{total_anis} Anis(es)\n"
    )

    confirmar = input("\n¿Es correcto? (S/N): ").strip().upper()
    if confirmar == "N":
        print("Cheque con barra.")
    else:
        res_prop = input("¿Quiere dejar propina? (S/N): ").strip().upper()
        if res_prop == "S":
            porcentaje = int(input("¿Cuánto porcentaje de propina?: "))
            p = propina(porcentaje, suma_total)
            print(f"Tu total sin propina es: {suma_total}")
            print(f"La propina es de: {p}")
            print(f"Tu total a pagar con propina es: {total(p, suma_total)}")
        else:
            print(f"Tu total a pagar es: {suma_total}")
