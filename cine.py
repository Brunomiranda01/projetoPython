def reservar_assentos (assentos):
    numero = input("Digite o numero do assento a ser reservado (1 a 10) : ")
    while not (numero.isdigit() and 1 <= int(numero) <= 10):
            print("Número de assento inválido\n")
            numero = (input("digite o número de assento válido (1-10): "))
     
    
    if assentos [int(numero) - 1] == False:
            assentos[int(numero) -1] = True
            print(f"Assento {numero} reservado com sucesso !")
    elif assentos [int(numero) - 1] == True:
            print (f"o  assento {numero} ja está ocupado ")
    else:
        print("número de assento inválido , somente de 1 a 10")

def liberar_assento (assentos):
    numero = input("Digite o numero do assento a ser liberado (1 a 10) : ")
    while not (numero.isdigit() and 1 <= int(numero) <= 10):
            print("Número de assento inválido\n")
            numero = (input("digite o número de assento válido (1-10): "))
     
    if assentos [int(numero) - 1] == True:
            assentos[int(numero) -1]= False
            print(f"Assento  {numero} foi liberado com sucesso !")
    elif assentos [int(numero) - 1] == False:
            print (f"o assento {numero} ja está livre ")
    else:
        print("número de assento inválido , somente de 1 a 10")


def mostrar_mapa (assentos):
    for i in range(10):
        if assentos[i] == True:
            status = "Ocupado"
            print (f"\n Assento {i+1} : {status} .")
        else:
            status = "Livre"
            print (f"\n Assento {i+1} : {status} .")






def main():
    assentos = [False] * 10
    while True:
        print("\n '-------- CINE PIPOCA ----------'")
        print("1- Reservar um assento")
        print("2- liberar um assento")
        print("3- Mostrar mapa de ocupação")
        print("4- Sair")

        escolha = input("Escolha uma opção (1-4):")

        if escolha == "1":
             reservar_assentos(assentos)
        elif escolha == "2":
             liberar_assento(assentos)
        elif escolha == "3":
             mostrar_mapa(assentos)
        elif escolha == "4":
             print("Obrigado por usar nosso sistema , até mais  (^-^) ")
             break
        else:
             print("Opção inválida !")
if __name__ == "__main__":
        main()