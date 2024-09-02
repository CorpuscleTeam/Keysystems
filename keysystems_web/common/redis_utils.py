import json

from keysystems_web.settings import REDIS_DB, REDIS_TTL


# сохраняем данные
async def add_online_user(room_name: str, user_id: int) -> None:
    data = []
    REDIS_DB.setex(room_name, REDIS_TTL, json.dumps(data))


# возвращаем данные
async def get_user_data(chat_id) -> dict:
    key = f"{chat_id}"
    data = REDIS_DB.get(key)
    return json.loads(data) if data else {}


# добавляет данные
# async def update_user_data(chat_id: int, key: str, value: str) -> None:
#     data = get_user_data(chat_id)
#     data[key] = value
#     save_user_data(chat_id, data)