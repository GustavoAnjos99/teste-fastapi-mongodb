from fastapi import FastAPI

from usuarioroutes import router as UsuarioRouter

app = FastAPI()

app.include_router(UsuarioRouter, prefix='/usuario')

@app.get('/')
async def root():
    return { "VOCÊ ENTROU!" }