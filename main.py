# Importando biblitecas
from fastapi import FastAPI
import psycopg

app = FastAPI()

@app.get("/")
def home():
    return ("Dinheirando!")

@app.get("/user")
def read_user():
    user_resposta = []
        # Conectando no Banco de Dados
    with psycopg.connect("dbname=dbmu38rmc5su92 user=omsisprosblwpg password=a100ad21e0e6f3aacfaeba408db87bd2b21adb0ed14ae7ee8d354b41c13418c5") as conn:

        # Cursor to perform database operations
        with conn.cursor() as cur:

            # Selecionando dados da tabela users.
            cur.execute("SELECT * FROM users;")
            
            for record in cur.fetchall():
                user_resposta.append({
                    "id": record[0],
                    "username": record[1],
                    "email": record[2]
                })

            # Make the changes to the database persistent
            conn.commit()
    return user_resposta

@app.get("/perfil")
def read_perfil():
    perfil_resposta = []
        # Conectando no Banco de Dados
    with psycopg.connect("dbname=postgres user=postgres password=postgree ") as conn:

        # Cursor to perform database operations
        with conn.cursor() as cur:

            # Selecionando dados da tabela perfil.
            cur.execute("SELECT * FROM perfil;")
            
            for record in cur.fetchall():
                perfil_resposta.append({
                    "id": record[0],
                    "user_id": record[1],
                    "nickname": record[2],
                    "foto": record[3],
                    "descrição": record[4],
                    "preferências": record[5]
                })

            # Make the changes to the database persistent
            conn.commit()
    return perfil_resposta


@app.get("/progresso")
def read_progresso():
    progresso_resposta = []
        # Conectando no Banco de Dados
    with psycopg.connect("dbname=postgres user=postgres password=postgree ") as conn:

        # Cursor to perform database operations
        with conn.cursor() as cur:

            # Selecionando dados da tabela progresso.
            cur.execute("SELECT * FROM progresso;")
            
            for record in cur.fetchall():
                progresso_resposta.append({
                    "id": record[0],
                    "Porcentagem (Progresso)": record[1],
                    "user_id": record[2],
                    "cursos_id": record[3]
                })

            # Make the changes to the database persistent
            conn.commit()
    return progresso_resposta

@app.get("/forum")
def read_forum():
    forum_resposta = []
        # Conectando no Banco de Dados
    with psycopg.connect("dbname=postgres user=postgres password=postgree ") as conn:

        # Cursor to perform database operations
        with conn.cursor() as cur:

            # Selecionando dados da tabela forum.
            cur.execute("SELECT * FROM forum;")
            
            for record in cur.fetchall():
                forum_resposta.append({
                    "id": record[0],
                    "user_id": record[1],
                    "Pontuação": record[2]
                })

            # Make the changes to the database persistent
            conn.commit()
    return forum_resposta

@app.get("/post")
def read_post():
    post_resposta = []
        # Conectando no Banco de Dados
    with psycopg.connect("dbname=postgres user=postgres password=postgree ") as conn:

        # Cursor to perform database operations
        with conn.cursor() as cur:

            # Selecionando dados da tabela post.
            cur.execute("SELECT * FROM post;")
            
            for record in cur.fetchall():
                post_resposta.append({
                    "id": record[0],
                    "perg": record[1],
                    "resp": record[2],
                    "avaliação": record[3],
                    "tag": record[4]
                })

            # Make the changes to the database persistent
            conn.commit()
    return post_resposta

@app.get("/cursos")
def read_cursos():
    cursos_resposta = []
        # Conectando no Banco de Dados
    with psycopg.connect("dbname=postgres user=postgres password=postgree ") as conn:

        # Cursor to perform database operations
        with conn.cursor() as cur:

            # Selecionando dados da tabela cursos.
            cur.execute("SELECT * FROM cursos;")
            
            for record in cur.fetchall():
                cursos_resposta.append({
                    "id": record[0],
                    "titulo": record[1],
                    "id_midia": record[2]
                })

            # Make the changes to the database persistent
            conn.commit()
    return cursos_resposta

@app.get("/rank")
def read_rank():
    rank_resposta = []
        # Conectando no Banco de Dados
    with psycopg.connect("dbname=postgres user=postgres password=postgree ") as conn:

        # Cursor to perform database operations
        with conn.cursor() as cur:

            # Selecionando dados da tabela rank.
            cur.execute("SELECT * FROM rank;")
            
            for record in cur.fetchall():
                rank_resposta.append({
                    "id": record[0],
                    "user_id": record[1],
                    "Pontuação": record[2]
                })

            # Make the changes to the database persistent
            conn.commit()
    return rank_resposta

@app.get("/midias")
def read_midias():
    midias_resposta = []
        # Conectando no Banco de Dados
    with psycopg.connect("dbname=postgres user=postgres password=postgree ") as conn:

        # Cursor to perform database operations
        with conn.cursor() as cur:

            # Selecionando dados da tabela rank.
            cur.execute("SELECT * FROM midias;")
            
            for record in cur.fetchall():
                midias_resposta.append({
                    "id": record[0],
                    "Tipo": record[1]
                })

            # Make the changes to the database persistent
            conn.commit()
    return midias_resposta

@app.get("/questionario")
def read_questionario():
    questionario_resposta = []
        # Conectando no Banco de Dados
    with psycopg.connect("dbname=postgres user=postgres password=postgree ") as conn:

        # Cursor to perform database operations
        with conn.cursor() as cur:

            # Selecionando dados da tabela questionario.
            cur.execute("SELECT * FROM questionario;")
            
            for record in cur.fetchall():
                questionario_resposta.append({
                    "id": record[0],
                    "pergunta": record[4],
                    "resp_user": record[1],
                    "resp_app": record[2],
                    "cursos_id": record[3]
                })

            # Make the changes to the database persistent
            conn.commit()
    return questionario_resposta


@app.post("/createUser")
def write_user():
        # Conectando no Banco de Dados
    with psycopg.connect("dbname=postgres user=postgres password=postgree ") as conn:

        # Cursor to perform database operations
        with conn.cursor() as cur:
            # Enviando dados para a tabela users                
            cur.execute("""INSERT INTO users (username, email, password) VALUES (%s, %s,%s);""",("Caio", "caio@tcc.com.br","321456"))                      
            # Make the changes to the database persistent
            conn.commit()
    return {"Status": "OK"}