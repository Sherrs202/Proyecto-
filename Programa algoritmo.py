##Proyecto
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

def Tequilas (T):
    Suma = 0
    if T == "Centenario plata" :
            Precio = 90
            Suma = Suma + Precio 
            return Suma
    
    else:
           if T == "Cuervo especial" :
                  Precio = 90
                  Suma = Suma + Precio 
                  return Suma
           else :
                  if T == "Tradicional reposado" :
                         Precio = 100
                         Suma = Suma + Precio 
                         return Suma
                  return 

## Esta función sirve para calcular que whisky quieren y darles el precio 
def Whisky (W):
    Suma = 0
    if W == "Black and White":
            Precio = 90
            Suma = Suma + Precio 
            return Suma
    
    else:
           if W == "Etiqueta roja":
                  Precio = 100
                  Suma = Suma + Precio 
                  return Suma
           else :
                  if W == "Etiqueta Negra":
                         Precio = 170
                         Suma = Suma + Precio 
                         return Suma
                  return 


## Estos valores se los puse para lograr saber de cuales han consumido y si tienen una 
## queja que vayam a barra a preguntar
W = 0
C = 0
T = 0
SumaT=0
R = input ("Quiere registrar una bebida? (S/N): ")

while R == "S":
        print ("\nQue bebida quieres?")
        print ("Tequila\nCerveza\nWhisky\nRon\nBrandy\n")
        bebida = input()
    
        if bebida == "Tequila":
              print("\nQue tequila quieres?")
              print("Centenario plata\nCuervo especial\nTradicional reposado")
              Teq = input()
              Precio = Tequilas (Teq)
              SumaT = SumaT + Precio 
              T = T + 1
        
        else:
            if bebida == "Cerveza":
                Precio = 55
                SumaT = SumaT + Precio
                C = C + 1
        
            else:
                if bebida == "Whisky":
                    print("\nQue Whisky quieres?")
                    print("Etiqueta roja\nEtiqueta negra\nBlack and White")
                    Wh = input()
                    Precio = Whisky (Wh)
                    SumaT = SumaT + Precio
                    W = W + 1
            
                else:
                    print("Bebida no registrada")
                    
        
            
        Respuesta = input("\nQuiere registrar otra bebida? (S/N): ")
        
        if Respuesta == "N":
            break
if R == "N":
      print ("No debes nada")
else:
    print("\nConsumio un total de\n", T , "Tequila(s)\n", W , "Whisky(s)\n", C,"Cerveza(s)" )
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
