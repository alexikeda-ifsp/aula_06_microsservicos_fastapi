from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/emprestimo/{id}")
def get_emprestimo(id: int):
    try:
        response = requests.get(f"http://livroservice:8000/livros/{id}")
        
        response.raise_for_status()

        livros = response.json()

        return {
            "emprestimo_id": id,
            "livros": livros
        }

    except requests.exceptions.RequestException:
        return {
            "erro": "Falha ao comunicar com o LivroService"
        }