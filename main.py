# Задание.
# Создать клиент-серверное приложение на примере Simple app.
# Используем fastapi, router + uvicorn.
# Работа с пользователем: email и ФИО.
# Само приложение .py в контейнере.
# Написать Dockerfile.
# Создание(POST)/получение(GET).
# Информацию храним в dict(), никуда не сохраняем. Примеры есть в лекции.

# Дополнительное задание.
# Вместо в dict() пишем в БД postgresql.
# Поднимаем два контейнера с помощью docker-compose.

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi import APIRouter
import uvicorn as uvic

app = FastAPI()
task_router = APIRouter()
users = {}

@app.get("/")
async def test() -> dict:
    return {"message": "Тестирование"}

@task_router.post("/create_user")
async def create_user(user: dict[str, str]) -> dict:
    name = user["name"]
    email = user["email"]
    u = f"{name}: {email}"
    return {"message": "Пользователь добавлен"}

@app.get("/get_user")
async def get_user(email: str = None) -> dict:
    if email in users:
        for user in users.values():
            if user["email"] == email:
                return {"name": user["name"], "email": user["email"]}
    elif email not in users:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    return {"message": "Пользователь найден"}

if __name__ == "__main__":
    uvic.run(app, host="127.0.0.1", port=8000)

app.include_router(task_router)