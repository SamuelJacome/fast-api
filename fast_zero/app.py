from http import HTTPStatus

from fastapi import FastAPI

from fast_zero.routers import auth, users
from fast_zero.schemas import Message
import uvicorn

app = FastAPI()

app.include_router(users.router)
app.include_router(auth.router)


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá Mundo!'}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)