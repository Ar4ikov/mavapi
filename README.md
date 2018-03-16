# MAV API

**MAV (Minecraft Account Verification)** - Уникальная база привязки `Minecraft` аккаунта к любым
социальным сетям или отдельным системам ID, которая создана
для подтверждения принадлежности того или иного MC аккаунта
той или иной странице в социальной сети.

Моя библиотека направлена на работу с MAV API, имеет некоторые
преимущества и удобства, особенно говоря о легком доступе к API

---
### Установка

Для установки потребуется иметь руки
```bash
pip install mav_api
```

Хотите установить определенную версию? используйте `==version`, где version - версия
```bash
pip install mav_api==2.2.1
```

Вам может понадобиться установить некоторые зависимости, если `pip` не установит их сам
```bash
pip install asyncio
pip install aiohttp
```

---
### Использование

Чтобы уж точно и наверняка - полное описание всегда в директории `tests`

Для начала, объявим экземпляр класса API
```python
# Импортируем модуль
import mavapi

# Создаем экземпляр класса API
api = mavapi.API(access_token='токен', server='сервер')
```
где:
- access_token - Access Token юзера
- server - Сервер MAV API

Обратимся к методу `getUser` с параметром ***mav_id*** = 16
```python
>>> api.getUser(mav_id=16)
```

На этом всё
