def  adicionar_time(campeonato):
     time = input("Nome do time a adicionar : ").strip().lower()

     if time in campeonato:
          print("time ja está cadastrado")
     else:
          campeonato[time]= 0
          print(f"\n time '{time} adicionado com 0 pontos.'")

def  resultado_partida(campeonato):
     time1 = input("nome do Primeiro time : ").strip().lower()
     time2 = input("nome do Segundo time : ").strip().lower()

     if time1 not in campeonato or time2 not in campeonato:
          print("\nambos os times devem estar cadastrados.")
          return
     
     gols1 = input(f"\nGols do  {time1}:")
     while not (gols1.isdigit()):
       print("Gols deve ser um numero inteiro")
       gols1 = input(f"\nGols do  {time1}:")

     gols2 = input(f"\nGols do  {time2}:")
     while not (gols2.isdigit()):
       print("Gols deve ser um numero inteiro")
       gols2 = input(f"\nGols do  {time2}:")

       gols1n = int(gols1)
       gols2n = int(gols2)

     if gols1n > gols2n:
          campeonato[time1] += 3
          print(f"\n{time1} venceu {time2} e ganhou três pontos")
     elif gols2n > gols1n:
          campeonato[time2] += 3
          print(f"\n{time2} venceu {time1} e ganhou três pontos")
     else:
          campeonato[time1] += 1
          campeonato[time2] += 1
          print(f"A partida entre {time1} e {time2} acabou empatada")

def obter_pontos(item):
    return item[1]

def  mostrar_classificacao(campeonato):
      if not campeonato:
        print("nenhum time cadastrado.")
        return
      
      classificacao = sorted(campeonato, key= obter_pontos, reverse=True)
      
      print("\nClassificação: ")
      for time, pontos in campeonato.items():
           print(f"\n {time}: {pontos} ponto(s)")
           print("")

def  remover_time(campeonato):
     time = input("nome do time a remover : ").strip().lower()

     if time in campeonato:
          del campeonato[time]
          print(f"\nTime {time} deletado com sucesso !")
     else:
          print("time não encontrado")


def main():
    campeonato = {}

    while True:
        print("\n ' Campeonato SN '")
        print("1- Adicionar time :")
        print("2- Registrar Resultado de Partida :")
        print("3- Mostrar Clasificação (decrescente) :")
        print("4- Remover time: ")
        print("5- Sair")
        escolha = input("Escolha uma opção (1-5):")

        if escolha == "1":
             adicionar_time(campeonato)
        elif escolha == "2":
             resultado_partida(campeonato)
        elif escolha == "3":
             mostrar_classificacao(campeonato)
        elif escolha == "4":
             remover_time(campeonato)
        elif escolha == "5":
             print("Obrigado por usar nosso sistema , até mais  (^-^) ")
             break
        else:
             print("Opção inválida !")
if __name__ == "__main__":
        main()