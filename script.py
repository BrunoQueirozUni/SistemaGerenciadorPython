import os


os.system("cls")

alunos = []
professores = []

while True:
   print("""
╔════════════════════════════╗
║           OPÇÕES           ║
╠════════════════════════════╣
║ 1 - Adicionar aluno        ║
║ 2 - Adicionar professores  ║
║ 3 - Listar alunos          ║
║ 4 - Listar professores     ║
║ 5 - Sair                   ║
╚════════════════════════════╝
   """)
   opcao = input("Digite a opção desejada: ")
   os.system("cls")

   if opcao == "1":
      nome = input("Digite o nome do aluno: ")
      alunos.append(nome)
      print("Aluno cadastrado com sucesso!")
      os.system("cls")

   elif opcao == "2":
      nome = input("Digite o nome do professor: ")
      professores.append(nome)
      print("Professor cadastrado com sucesso!")
      os.system("cls")

   elif opcao == "3":
      print("""
╔══════════════════════════════════════════════════╗
║                 LISTA DE ALUNOS                  ║
╚══════════════════════════════════════════════════╝
   """)
      for aluno in alunos:
         print(aluno)
      input("Pressione enter para continuar...")
      os.system("cls")

   elif opcao == "4":
      print("""
╔══════════════════════════════════════════════════╗
║               LISTA DE PROFESSORES               ║
╚══════════════════════════════════════════════════╝
         """)
      for professor in professores:
         print(professor)
      input("Pressione enter para continuar...")
      os.system("cls")
   elif opcao == "5":
      break
   elif opcao == "Escondido":
      print("Para de se meter onde não é chamado!!!!!!!!")
      input("")
      os.system("cls")
   else:
      print("Opção inválida!")
      input("")
      os.system("cls")
