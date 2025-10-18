##Proyecto

#Biblotecas
from prettytable import PrettyTable #type : ignore 

"""
================== Dicionarios  =====================================
"""
"""
Estos dicionarios sirven para tener como una base 
de datos que me ayudan a identificar el precio
y el tipo de bebidas que buscan
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
================== Lista  =====================================
"""

bebidas = [Tequila,Cerveza,Whisky,Ron,Brandy,Vodka,Mezcal,Gin,Anis]
"""
Estas lista me ayuda a buscar por el nombre de bebida que
quiera el cliente
"""

"""
================= Funciones precio y buscar  ==========================
"""

def propina(prop, suma_t):
    """
    La función propina recibe el porcentaje que 
    el cliente quiera dejar de 
    propina y se lo multiplica al precio total 
    logrando sacar la propina,
    recibe el porcentaje de propina que el usuario quiera dejar y te 
    regresa la propina del total
    """
    p = prop * suma_t / 100
    return p

def total(p, suma_t):
    """
    La función total me ayuda a calcular la suma de la propina 
    y del total que consumio, recibe la propina el porcentaje de propina
    que quiere dejar el usuario y la suma de todo lo que consumio
    para regresar el total con propina
    """
    total_pagar = p + suma_t
    return total_pagar

def buscar(bebida, tipo):
    """
    Esta funcion me ayuda a poder buscar y calcular 
    el precio de cada bebida y su tipo logrando 
    guardar ese precio y usarlo mas adelante, recibe la bebida
    y el tipo de bebida que quiere el cliente 
    regresandote el precio de esta
    """
    for i in bebidas:
        if i["Nombre"] == bebida:
            for tip, dat in i["Tipo"].items():
                if tip == tipo:
                    return dat["Precio"]
            return "no tenemos"

def mostrar_tipos(bebida):
    """
    Me ayuda a mostrar los tipos de bebida que el cliente quiera
    en forma de tabla para que se alcance a ver de mejor forma,
    recibe la bebida que quiere el cliente para que regrese
    una tabla con los tipos de la bebida que desea
    """
    from prettytable import PrettyTable # type: ignore
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

w = 0
c = 0
t = 0
ror = 0
b = 0
v = 0
m = 0
g = 0
a = 0
suma_t = 0

r = input("Quiere registrar una bebida? (S/N): ")

"""
El ciclo ayuda a registrar el total de bebidas que el cliente consuma
y al final le de su total apagar preguntando si quiere dejar propina
"""

"""
================== Codigo principal ===================================
"""

while r == "S":
    print("\nQue bebida quieres?")
    print("Tequila\nCerveza\nWhisky\nRon\nBrandy"
          "\nVodka\nMezcal\nGin\nAnis")
    bebida = input()

    if bebida == "Tequila":
        print("\nQue tequila quieres?")
        mostrar_tipos(Tequila)
        teq = input()
        precio = buscar(bebida, teq)
        suma_t += precio
        t += 1

    elif bebida == "Cerveza":
        print("\nQue cerveza quieres?")
        mostrar_tipos(Cerveza)
        cer = input()
        precio = buscar(bebida, cer)
        suma_t += precio
        c += 1

    elif bebida == "Whisky":
        print("\nQue whisky quieres?")
        mostrar_tipos(Whisky)
        wh = input()
        precio = buscar(bebida, wh)
        suma_t += precio
        w += 1

    elif bebida == "Ron":
        print("\nQue ron quieres?")
        mostrar_tipos(Ron)
        ro = input()
        precio = buscar(bebida, ro)
        suma_t += precio
        ror += 1

    elif bebida == "Brandy":
        print("\nQue brandy quieres?")
        mostrar_tipos(Brandy)
        bra = input()
        precio = buscar(bebida, bra)
        suma_t += precio
        b += 1

    elif bebida == "Vodka":
        print("\nQue vodka quieres?")
        mostrar_tipos(Vodka)
        vod = input()
        precio = buscar(bebida, vod)
        suma_t += precio
        v += 1

    elif bebida == "Mezcal":
        print("\nQue mezcal quieres?")
        mostrar_tipos(Mezcal)
        mez = input()
        precio = buscar(bebida, mez)
        suma_t += precio
        m += 1

    elif bebida == "Gin":
        print("\nQue ginebra quieres?")
        mostrar_tipos(Gin)
        gin_ = input()
        precio = buscar(bebida, gin_)
        suma_t += precio
        g += 1

    elif bebida == "Anis":
        print("\nQue anis quieres?")
        mostrar_tipos(Anis)
        ani = input()
        precio = buscar(bebida, ani)
        suma_t += precio
        a += 1

    else:
        print("Bebida no registrada")

    respuesta = input("\nQuiere registrar otra bebida? (S/N): ")
    if respuesta == "N":
        break

if r == "N":
    print("No debes nada")
else:
    print(
        "Consumo total \n",
        t, "Tequila(s)\n",
        w, "Whisky(s)\n",
        c, "Cerveza(s)\n",
        ror, "Ron(es)\n",
        b, "Brandy(s)\n",
        v, "Vodka(s)\n",
        m, "Mezcal(es)\n",
        g, "Gin(s)\n",
        a, "Anis(es)\n"
    )

    res = input("\nEs correcto (S/N): ")
    if res == "N":
        print("\nCheque con barra")
    else:
        print("Quiere dejar propina? (S/N)")
        res_prop = input()
        if res_prop == "S":
            prop = int(input("Cuanto porcentaje de propina quiere dejar?: "))
            p = propina(prop, suma_t)
            print("Tu total sin propina es", suma_t)
            print("La propina es de", p)
            print("Tu total a pagar con propina es:", total(p, suma_t))
        else:
            print("Tu total a pagar es:", suma_t)
