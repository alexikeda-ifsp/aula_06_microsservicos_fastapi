from fastapi import FastAPI
import time

app = FastAPI()

@app.get("/livros/{id}")
def get_livros(id: int):
    time.sleep(2)
    return [
            {
                "emprestimo_id": id,
                "nome": f"O Hobbit",
                "autor": "Tolkien"
            },
            {
                "emprestimo_id": id,
                "nome": f"Senhor dos Anéis",
                "autor": "Tolkien"
            }
    ]