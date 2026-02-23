from database.connection import get_connection
from models.aluno import Aluno


class AlunoDAO:
    def __init__(self):
        self.connect = get_connection()
        self.cursor = self.connect.cursor()

    def create(self, nome, idade, curso):
        self.cursor.execute(
            """
            INSERT INTO alunos (nome, idade, curso)
            VALUES (?, ?, ?)
            """,
            (nome, idade, curso),
        )
        self.connect.commit()

    def read(self):
        self.cursor.execute("SELECT * FROM alunos")
        linhas = self.cursor.fetchall()

        alunos = []

        for linha in linhas:
            alunos.append(Aluno(*linha))

        return alunos

    def read_by_id(self, id):
        self.cursor.execute("SELECT * FROM alunos WHERE id = ?", (id,))
        linha = self.cursor.fetchone()

        if linha:
            return Aluno(*linha)
        return None

    def update(self, id, nome, idade, curso):
        self.cursor.execute(
            """
            UPDATE alunos
            SET nome = ?, idade = ?, curso = ?
            WHERE id = ?
            """,
            (nome, idade, curso, id),
        )
        self.connect.commit()

    def delete(self, id):
        self.cursor.execute("DELETE FROM alunos WHERE id = ?", (id,))
        self.connect.commit()

    def close(self):
        self.cursor.close()
        self.connect.close()