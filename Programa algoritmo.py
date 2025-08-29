SumaT=0
R = input ("Quiere registrar una bebida? (S/N): ")

while R == "S":
    
        print ("Ingresa tu bebida")
        bebida = input()
    
        if bebida == "tequila":
            Precio = 80
            SumaT = SumaT + Precio
        
        else:
            if bebida == "cerveza":
                Precio = 55
                SumaT = SumaT + Precio
        
            else:
                if bebida == "whisky":
                    Precio = 100
                    SumaT = SumaT + Precio
            
                else:
                    print("Bebida no registrada")
        
            
        Respuesta = input("Quiere registrar otra bebida? (S/N): ")
        
        if Respuesta == "N":
            break




print ("Tu total a pagar es:", SumaT) 