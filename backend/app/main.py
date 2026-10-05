from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {
        "message": "HorarioOrganized IA API funcionando"
    }