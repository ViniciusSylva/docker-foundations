from fastapi import FastAPI


app = FastAPI()


cursos = {
    1: {
        "Titulo": "Programação para Leigos",
        "Aulas": 112,
        "Horas": 58
    },
    2: {
        "Titulo": "Algoritimo e Lógica de Programação",
        "Aulas": 87,
        "Horas": 67        
    }
}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, debug=True)