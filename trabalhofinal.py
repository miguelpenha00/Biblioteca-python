#referencias:
#utilizei a base do programa de carros que fizmos em sala
#remoçao de elementos pop(): https://youtu.be/ND430nJ2HvY?si=i0jQvrTtjdXxi9_V
#uso de LLM na implementacao de um contador na funcao consultar_aut
#motivo:por poder ter varios livros de um autor nao poderia usar return


class Infolivro:
    titulo=''
    autor=''
    anopub=0
    codigo=''
    status='disponivel'
#inicio
def menu():
    print("1.Cadastrar livro")
    print("2.Consultar livro")
    print("3.Alterar dados")
    print("4.Remover livro")
    print("5.Listar livros")
    print("6.Realizar empréstimo")
    print("7.Devolver livro")
    print("8.Sair")
    opcao=int(input("Opção:"))
    return opcao
#1.cadastrar livro
def cadastrar(livros):
    livro=Infolivro()
    livro.codigo=input("código : ")
    for i in range(len(livros)):
      if livros[i].codigo==livro.codigo:
        print("Esse código já foi cadastrado")
        return
    livro.titulo=input("titulo : ")
    livro.autor=input("autor : ")
    livro.anopub=int(input("ano de publicação: "))
    livro.status="disponivel"
    livros.append(livro)
#2.consultar por autor
def consultar_aut(livros):
  autor=input("Informe o autor")
  achou=0
  for i in range (len(livros)):
    if livros[i].autor==autor:
      achou+=1
      print("---------Livro localizado---------")
      print("código do livro:",livros[i].codigo)
      print("Título do livro:",livros[i].titulo)
      print("Autor do livro:",livros[i].autor)
      print("Ano de publicação:",livros[i].anopub)
      print("Status do livro:",livros[i].status)
  if achou==0:
   print("---------Livro não localizado---------")
#2.consultar por codigo e autor
def consultar(livros):
    print("1. Para consultar por código")
    print("2. Para consultar por autor")
    escolha=int(input("tipo de consulta:"))
    if escolha==1:
      codigo=input("Informe o código : ")
      for i in range (len(livros)):
        if livros[i].codigo==codigo:
            print("---------Livro localizado---------")
            print("código do livro:",livros[i].codigo)
            print("Título do livro:",livros[i].titulo)
            print("Autor do livro:",livros[i].autor)
            print("Ano de publicação do livro:",livros[i].anopub)
            print("Status do livro:",livros[i].status)
            return
      print("---------Livro não localizado---------")
    else:
      if escolha==2:
        consultar_aut(livros)
#3.alterar dados
def alterar (livros):
    codigo=input("Informe o código :")
    for i in range (len(livros)):
        if livros[i].codigo==codigo:
           livros[i].titulo=input("altere o título : ")
           livros[i].autor=input("altere o autor : ")
           livros[i].anopub=int(input("altere o ano : "))
           return
#4.revomer livro
def remover(livros):
    codigo=input("Informe o código :")
    for i in range (len(livros)):
      if livros[i].codigo==codigo:
        livros.pop(i)
        print("Livro removido")
        return
    print("Livro não encontrado")


#5.listar livros
def listar (livros):
    for i in range (len(livros)):
        print("------------------")
        print("titulo do livro : ",livros[i].titulo)
        print("ano de publicação : ",livros[i].anopub)
        print("------------------")

#6.realizar emprestimo
def emprestarl (livros):
  codigo=input("Informe o código :")
  for i in range (len(livros)):
   if livros[i].codigo==codigo:
    if livros[i].status=="indisponivel":
     print("livro ja emprestado")
    else:
      livros[i].status="indisponivel"
      print("emprestimo feito")
    return
#7.realizar decoluçao
def devolverl(livros):
  codigo=input("Informe o código")
  for i in range (len(livros)):
    if livros[i].codigo==codigo:
      livros[i].status="disponivel"
      print ("devolução feita")
      return


#principal
livros=[]
while True:
    opcao=menu()
    if opcao==8:
        break
    if opcao==1:
        cadastrar(livros)
    if opcao==2:
        consultar(livros)
    if opcao==3:
        alterar(livros)
    if opcao==4:
        remover(livros)
    if opcao==5:
        listar(livros)
    if opcao==6:
        emprestarl(livros)
    if opcao==7:
        devolverl(livros)
