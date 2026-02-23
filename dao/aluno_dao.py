import sqlite3
from aluno import Aluno

class AlunoDAO:
    def __init__(self):
        self.connect = sqlite3.connect("db.sqlite")
        self.cursor = self.connect.cursor()
        self.create_table()
        
    def create_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS aluno(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade INTEGER NOT NULL,
            curso TEXT NOT NULL
        )
        """)
        self.connect.commit()
        
    def create (self,nome, idade, curso):
        self.cursor.execute(""" INSERT INTO aluno(
            nome, idade, curso) VALUES(?,?,?)""",
            (nome, idade, curso)
        )
        self.connect.commit()
        
    def read(self):
        self.cursor.execute("SELECT * FROM aluno")
        linha_aluno = self.cursor.fetchall()
        alunos = []
        
        if not linha_aluno:
            return []
        
        else:
        
            for linha in linha_aluno:
                alunos.append(Aluno(*linha))
            
            return alunos
    
    def read_by_id(self, id):
        self.cursor.execute("SELECT * FROM aluno WHERE id = ?", (id,))
        linha_aluno = self.cursor.fetchone()
        if linha_aluno:
            return Aluno(*linha_aluno)
        else:
            return None
    
    def update(self,id,nome,idade,curso):
        self.cursor.execute(
            "UPDATE aluno SET nome = ?, idade = ?, curso = ? WHERE id =?",
            (nome, idade, curso, id)
        )
        self.connect.commit()
    
    def delete(self,id):
        self.cursor.execute("DELETE FROM aluno WHERE id = ?", (id,))
        self.connect.commit()
    
    def close(self):
        self.cursor.close()
        self.connect.close()