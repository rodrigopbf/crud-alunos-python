# CRUD de Alunos em Python

Um projeto simples de **CRUD (Create, Read, Update, Delete)**
desenvolvido em Python para gerenciamento de alunos via terminal,
utilizando **SQLite** como banco de dados.

## Sobre o Projeto

Este projeto tem como objetivo praticar conceitos fundamentais de
desenvolvimento backend com Python, incluindo:

-   Estruturas de controle
-   Programação orientada a objetos (POO)
-   Persistência de dados com SQLite
-   Organização em camadas (DAO)

##  Funcionalidades

-    Cadastrar aluno;
-   Listar todos os alunos;
-    Buscar aluno por ID;
-   Atualizar dados de um aluno;
-   Remover aluno.

##  Estrutura do Projeto

    crud-alunos-python/
    │
    ├── main.py
    ├── dao/
    │   └── aluno_dao.py
    ├── models/
    │   └── aluno.py
    ├── database/
    │   └── database.py
    └── README.md

##  Tecnologias Utilizadas

-   Python 3.x
-   SQLite

## Como Executar

``` bash
git clone https://github.com/rodrigopbf/crud-alunos-python.git
cd crud-alunos-python
python main.py
```


