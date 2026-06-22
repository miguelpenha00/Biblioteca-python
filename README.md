# 📚 Sistema de Controle de Biblioteca

## Descrição

Este projeto foi desenvolvido para a disciplina de **Algoritmos e Programação** da **UFFS**. O sistema permite o cadastro e gerenciamento de livros por meio de um menu interativo executado no terminal.

Cada livro possui as seguintes informações:

* Título
* Autor
* Ano de publicação
* Código (ID único)
* Status (Disponível ou Emprestado)

---

## Funcionalidades

### 1. Cadastrar Livro

Permite adicionar um novo livro ao sistema.

**Validações:**

* Não permite códigos duplicados.
* Todo livro recebe o status inicial de **Disponível**.

---

### 2. Consultar Livro

Permite pesquisar livros de duas formas:

* Por código
* Por autor

Caso nenhum livro seja encontrado, o sistema exibe a mensagem:

```text
Livro não encontrado
```

---

### 3. Alterar Dados

Permite modificar as seguintes informações de um livro já cadastrado:

* Título
* Autor
* Ano de publicação

A busca é realizada através do código do livro.

---

### 4. Remover Livro

Remove um livro do sistema utilizando seu código.

Caso o código informado não exista, o sistema exibe:

```text
Livro não encontrado
```

---

### 5. Listar Todos os Livros

Exibe todos os livros cadastrados mostrando:

* Título
* Ano de publicação

---

### 6. Realizar Empréstimo

Altera o status do livro para **Emprestado**.

O empréstimo somente é realizado se o livro estiver disponível.

Caso contrário, o sistema exibe:

```text
Livro já emprestado
```

---

### 7. Realizar Devolução

Altera o status do livro para **Disponível**, permitindo novos empréstimos.

---

### 8. Sair

Encerra a execução do programa.

---

## Como Executar

1. Clone o repositório:

```bash
git clone LINK_DO_REPOSITORIO
```

2. Entre na pasta do projeto:

```bash
cd nome-do-projeto
```

3. Execute o programa:

```bash
python nome_do_arquivo.py
```

---

## Tecnologias Utilizadas

* Python 3
* Funções
* Estruturas condicionais
* Estruturas de repetição
* Listas e dicionários

---

## Objetivo do Projeto

O objetivo deste projeto é aplicar os conceitos fundamentais de programação estudados na disciplina de Algoritmos e Programação, desenvolvendo um sistema funcional para gerenciamento de uma biblioteca e praticando a organização de código através do uso de funções e estruturas de dados.
