def  adicionar_nota(nota):
     nome_aluno = input("\nNome do aluno: ")
     nota_aluno = input("Nota do Aluno: ")
     while not (nota.isdigit() and 1 <= float(nota) <= 10):
            print("nota inválida\n")
            nota_aluno = input("Nota do Aluno: ")

     disciplina = input("Disciplina : ")
     nota.append((nome_aluno, float(nota_aluno), disciplina))
    
     print("Nota adcionado com sucesso !")

def  melhor_aluno(nota):
     pass

def consultar_notas_por_aluno(nota):
     nome_busca = input("digite o nome do aluno")
     encontrou = False

     for n in nota:
          if n[0].lower().strip() == nome_busca.lower().strip():
               print(f"disciplina: {n[2]} | nota : {n[1]}")
               encontrou = True
     if not encontrou:
          print("nenhuma nota encontrada para este aluno.")

def obter_nota(tupla):
     return tupla [1]


def  exibir_notas(nota):
    if len(nota) == 0:
        print("nenhuma nota cadastrada ainda")
        return
    notas_ordenadas = sorted(nota, key= obter_nota, reverse=True)
    print("notas ordenas (descrecnte)")

    for n in nota:
        print(f"{n[1]:.2f},{n[0]},{n[2]}")

def main():
    nota = []

    while True:
        print("\n 'Boletim Escolar'")
        print("1- Adicionar nota :")
        print("2- Mostrar Melhor Aluno por disciplina :")
        print("3- Consultar Notas por aluno :")
        print("4- Exibir Notas Ordenadas (Decrescente): ")
        print("5- Sair")
        escolha = input("Escolha uma opção (1-5):")

        if escolha == "1":
             adicionar_nota(nota)
        elif escolha == "2":
             melhor_aluno(nota)
        elif escolha == "3":
             consultar_notas_por_aluno(nota)
        elif escolha == "4":
             exibir_notas(nota)
        elif escolha == "5":
             print("Obrigado por usar nosso sistema , até mais  (^-^) ")
             break
        else:
             print("Opção inválida !")
if __name__ == "__main__":
        main()