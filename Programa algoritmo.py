##Proyecto
## aquí voy a meter todos los diccionarios que haga para tenr una base de datos y ocuparlos mas adelante ( el profe nos los hace validos como listas nos dijo el )
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
                       "Ambar": {"Precio":60}
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

## Esta lista es para que busque en los dicionarios 
bebidas = [tequilas,cervezas,whiskys]

## Aqui estaran las listas de todas las bebidas
Lista_tequilas = ("\nCentenario plata","Centenario azul","Centenario reposado","Cuervo especial","Cuervo plata",
                  "Herradura antiguo", "Hornitos reposado", "Tradicional reposado","Tradicional plata","Maestro dobel",
                  "Don julio reposado","1800 Cristalino","Don julio 70")

Lista_cervezas = ("Corona","Victoria","Ligth","Ultra","Pacifico","Modelo especial","Modelo oscura","Ambar")

Lista_whiskys = ("JB","Black n white","Etiqueta roja","Jacks daniels","Chivas 12","Buchanas","Etiqueta negra","Glenfuddich","Glenlivet 12 doble oak")

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
        
## Funión para calcular el precio del Ron
def Ron (R):
      Suma = 0
      if R == "1":
            Precio = 90
            Suma = Suma + Precio
            return Suma
      else : 
            if R == "2":
                  Precio = 90
                  Suma = Suma + Precio 
                  return Suma 
            else:
                  if R == "3":
                        Precio = 90
                        Suma = Suma + Precio 
                        return Suma
                  else : 
                        if R == "4":
                              Precio = 95
                              Suma = Suma + Precio 
                              return Suma 
                                   
## Estos valores se los puse para lograr saber de cuales han consumido y si tienen una 
## queja que vayam a barra a preguntar
W = 0
C = 0
T = 0
ror = 0
SumaT=0
R = input ("Quiere registrar una bebida? (S/N): ")

while R == "S":
        print ("\nQue bebida quieres?")
        print ("Tequila\nCerveza\nWhisky\nRon\nBrandy\n")
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
                          print("1)Bacardi\n2)Potosi\n3)Matusalen Clasico\n4)Flor de Caña 7")
                          Ro = input ()
                          Precio = Ron (Ro)
                          SumaT = SumaT + Precio 
                          ror = ror  + 1
                    else:
                          print("Bebida no registrada")
                    
        
            
        Respuesta = input("\nQuiere registrar otra bebida? (S/N): ")
        
        if Respuesta == "N":
            break
if R == "N":
      print ("No debes nada")
else:
    print("Consumo total \n", T , "Tequila(s)\n", W , "Whisky(s)\n", C,"Cerveza(s)\n", ror , "Ron" )
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

