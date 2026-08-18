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


@app.get('/cursos')
async def get_cursos():
    return cursos


@app.get('/cursos/{curso_id}')
async def get_curso(curso_id: int):
    curso = curso[curso_id]
    curso.update({"id": curso_id})

    return curso

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
