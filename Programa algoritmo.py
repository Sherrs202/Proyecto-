##Proyecto
## aqeui voy a meter todos los diccionarios que haga ( el profe nos dejo hacerlo y cuenta como listas)
tequilas = {"Nombre" :"Tequila",
            "Tipo" : 
                      {"Centenario plata":{"Precio":90},
                       "Centenario azul":{"Precio":90},
                       "Centenario reposado":{"Precio":90},
                       "Cuervo especial" : {"Precio":90},
                       "Cuervo plata": {"Precio":90},
                       "Herradura antiguo": {"Precio":100},
                       "Hornitos reposado" : {"Precio":100},
                       "Tradicional reposado":{"Precio":100},
                       "Tradicional plata": {"Precio":100},
                       "Maestro dobel": {"Precio":130},
                       "Don julio reposado": {"Precio":130},
                       "1800 Cristalino": {"Precio":150},
                       "Don julio 70": {"Precio":170}
                     }}

cervezas = {"Nombre" :"Cerveza",
            "Tipo" : 
                      {"Corona":{"Precio":55},
                       "Victoria":{"Precio":55},
                       "Ligth":{"Precio":60},
                       "Ultra" : {"Precio":60},
                       "Pacifico": {"Precio":60},
                       "Modelo especial": {"Precio":60},
                       "Modelo oscura": {"Precio":60},
                       "Ambar": {"Precio":60},
                       "Estela":{"Precio":60}
                     }}

whiskys = {"Nombre" :"Whisky",
            "Tipo" : 
                      {"JB":{"Precio":90},
                       "Black n white":{"Precio":90},
                       "Etiqueta roja":{"Precio":100},
                       "Jacks daniels" : {"Precio":100},
                       "Chivas 12": {"Precio":130},
                       "Buchanas": {"Precio":150},
                       "Etiqueta negra" : {"Precio":170},
                       "Glenfuddich":{"Precio":200},
                       "Glenlivet 12 doble oak": {"Precio":200},
                     }}

ron = {"Nombre" :"Ron",
            "Tipo" : 
                      {"Apppleton state":{"Precio":90},
                       "Flor de caña 4":{"Precio":90},
                       "Matusalen clasico":{"Precio":90},
                       "Matusalen platino" : {"Precio":190},
                       "Ron potosi": {"Precio":90},
                       "Appleton esp": {"Precio":90},
                       "Bacardi blanco" : {"Precio":90},
                       "Bacardi añejo":{"Precio":90},
                       "Bacardi solera": {"Precio":90},
                       "Castillo": {"Precio":90},
                       "Malibu": {"Precio":90},
                       "Appleton blanco": {"Precio":90},
                       "Flor de caña blanco": {"Precio":90},
                       "Flor de caña 7": {"Precio":95},
                       "Mastusalen gran reserva": {"Precio":100},
                       "Havanna club 7": {"Precio":100},
                       "Bacardi 8": {"Precio":135},
                       "Zacapa 23": {"Precio":220}
                     }}

brandy = {"Nombre" :"Brandy",
            "Tipo" : 
                      {"Presidente":{"Precio":80},
                       "Don pedro":{"Precio":80},
                       "Torres 5":{"Precio":90},
                       "Torres 10": {"Precio":90},
                       "Azteca de oro": {"Precio":90},
                       "Terry": {"Precio":90},
                       "Fundador": {"Precio":90},
                       "Parris-torres": {"Precio":100}
                     }}

vodka = {"Nombre" :"Vodka",
            "Tipo" : 
                      {"Ocsolut LALO":{"Precio":60},
                       "Stolichnaya":{"Precio":90},
                       "Absolut":{"Precio":90},
                       "Oso negro": {"Precio":90},
                       "Smirnoff": {"Precio":90}
                     }}

mezcal = {"Nombre" :"Mezcal",
            "Tipo" : 
                      {"400 conejos":{"Precio":130},
                       "Gusano rojo":{"Precio":130},
                       "Naksir":{"Precio":130}
                     }}

gin = {"Nombre" :"Gin",
            "Tipo" : 
                      {"Oso negro gin":{"Precio":90},
                       "Beefeater":{"Precio":100},
                       "Tanqueray":{"Precio":130}
                     }}

anis = {"Nombre" :"Anis",
            "Tipo" : 
                      {"Mico dulce":{"Precio":90},
                       "Sambuca vaccari":{"Precio":100},
                       "Chichon dulce":{"Precio":125}
                     }}

## Esta lista es para que busque en los dicionarios 
bebidas = [tequilas,cervezas,whiskys,ron,brandy,vodka,mezcal,gin,anis]

## Aqui estaran las listas de todas las bebidas
Lista_tequilas = ("\nCentenario plata","Centenario azul","Centenario reposado","Cuervo especial","Cuervo plata",
                  "Herradura antiguo", "Hornitos reposado", "Tradicional reposado","Tradicional plata","Maestro dobel",
                  "Don julio reposado","1800 Cristalino","Don julio 70")

Lista_cervezas = ("Corona","Victoria","Ligth","Ultra","Pacifico","Modelo especial","Modelo oscura","Ambar")

Lista_whiskys = ("JB","Black n white","Etiqueta roja","Jacks daniels","Chivas 12","Buchanas","Etiqueta negra","Glenfuddich","Glenlivet 12 doble oak")

Lista_rones = ("Appleton state","Flor de caña","Matusalen clasico","Matusalen platino","Ron potosi","Appleton esp","Bacardi blanco","Bacardi añejo","Bacardi solera","Castillo","Malibu","Appleton blanco",
               "Flor de caña blanco","Flor de caña 7","Matusalen gran reserva","Havvana club 7","Bacardi 8","Zacapa 23")

Lista_brandy = ("Presidente","Don pedro","Torres 5","Torres 10","Azteca de oro","Terry","Fundador","Paris-torres")

Lista_vodkas = ("Ocsolut LALO","Stolichnaya","Absolut","Oso negro","Smirnoff")

Lista_mezcal = ("400 conejos","Gusano rojo","Naksir")

Lista_gin = ("Oso negro gin","Beefeater","Tanqueray")

Lista_anis = ("Mico dulce","Sambuca vaccari","Chichon dulce")

## esta función la hago para caulcular la propina que van a dejar 
def propina (Prop,SumaT):
        P = Prop * SumaT/100
        return P


## Aqui logro calcular el total de toda la compra
def Total(P,SumaT) :
        Total = P + SumaT
        return Total

## Esta función sirve para saber que tequila quiere y dependiendo del tequila 
# el precio se ajusta 

def buscar (bebida, tipo):
    for i in bebidas:
        if i ["Nombre"] == bebida :
            for tip , dat in i["Tipo"].items():
                if tip == tipo:
                    return dat["Precio"]
            return "no tenemos"
        

## Estos valores se los puse para lograr saber de cuales han consumido y si tienen una 
## queja que vayan a barra a preguntar
W = 0
C = 0
T = 0
ror = 0
B = 0
V = 0
M = 0
G = 0
A = 0
SumaT=0
R = input ("Quiere registrar una bebida? (S/N): ")
## Este ciclo es para que se pueda registrar varias bebidas y asi poder ir acumulando el precio de cada una
while R == "S":
        print ("\nQue bebida quieres?")
        print ("Tequila\nCerveza\nWhisky\nRon\nBrandy\nVodka\nMezcal\nGin\nAnis")
        bebida = input()
    
        if bebida == "Tequila":
              print("\nQue tequila quieres?")
              for item in Lista_tequilas:
                    print(item)
              Teq = input()
              Precio = buscar (bebida,Teq)
              SumaT = SumaT + Precio 
              T = T + 1
        
        else:
            if bebida == "Cerveza":
                print("\nQue cerveza quieres?")
                for item in Lista_cervezas:
                     print(item)
                Cer = input()
                Precio = buscar (bebida,Cer)
                SumaT = SumaT + Precio
                C = C + 1
        
            else:
                if bebida == "Whisky":
                    print("\nQue Whisky quieres?")
                    for item in Lista_whiskys:
                         print(item)
                    Wh = input()
                    Precio = buscar (bebida,Wh)
                    SumaT = SumaT + Precio
                    W = W + 1
            
                else:
                    if bebida == "Ron":
                          print("\nQue ron quieres?")
                          for item in Lista_rones:
                               print(item)
                          Ro = input ()
                          Precio = buscar (bebida,Ro)
                          SumaT = SumaT + Precio 
                          ror = ror  + 1
                    else:
                          if bebida == "Brandy":
                               print("\nQue brandy quieres")
                               for item in Lista_brandy:
                                    print (item)
                               Bra = input()
                               Precio = buscar (bebida,Bra)
                               SumaT = SumaT + Precio
                               B = B + 1
                          else :
                               if bebida == "Vodka" :
                                    print ("\nQue vodka quieres")
                                    for item in Lista_vodkas:
                                         print (item)
                                    Vod = input()
                                    Precio = buscar (bebida,Vod)
                                    SumaT = SumaT + Precio
                                    V = V + 1 
                               else :
                                    if bebida == "Mezcal":
                                         print ("\nQue mezcal quieres")
                                         for item in Lista_mezcal:
                                              print (item)
                                         Mez = input()
                                         Precio = buscar (bebida,Mez)
                                         SumaT = SumaT + Precio
                                         M = M + 1
                                    else:
                                         if bebida == "Gin":
                                              print("\nQue ginebra quieres")
                                              for item in Lista_gin:
                                                   print (item)
                                              Gin = input()
                                              Precio = buscar (bebida,Gin)
                                              SumaT = SumaT + Precio
                                              G = G + 1
                                         else:
                                              if bebida == "Anis":
                                                   print ("\nQue anis quieres")
                                                   for item in Lista_anis:
                                                        print (item)
                                                   Ani = input()
                                                   Precio = buscar (bebida,Ani)
                                                   SumaT = SumaT + Precio
                                                   A = A + 1
                                              else:
                                                   print ("Bebida no registrada")
                     
        Respuesta = input("\nQuiere registrar otra bebida? (S/N): ")
        
        if Respuesta == "N":
            break
if R == "N":
      print ("No debes nada")
else:
    print("Consumo total \n", T , "Tequila(s)\n", W , "Whisky(s)\n", C,"Cerveza(s)\n", ror , "Ron\n",B , "Brandy(s)\n", V,"Vodka(s)\n",
           M ,"Mezcal(s)\n", G, "Gin(s)\n", A , "Anis(s)\n" )
    res = input("\nEs correcto (S/N)")
    if res =="N":
          print ("\nCheque con barra")
    else:      
        print("Quiere dejar propina? (S/N)")
        Res = input()
        if Res == "S" :
            Prop = int(input("Cuanto porcentaje de propina quiere dejar?"))
            P = propina (Prop,SumaT)
            print("Tu total sin propina es", SumaT)
            print("La propina es de ", P)
            print ("Tu total a pagar con propina es:",Total(P,SumaT))
        else :
            print ("Tu total a pagar es:", SumaT)
