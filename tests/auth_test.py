import mavapi

'''
    Тест #1. Авторизация
    Присваиваем api объект API для дальнейшей работы, указывая сервер запросов
'''

api = mavapi.API('api end-server')

'''
    Указываем наш ACCESS_TOKEN
    Если токена нет, поднимет ошибку
    Можно использовать через конструкцию try - except
'''

try:
    access_token = api.Auth('access_token')
except mavapi.MAVAPIAuthError as error:
    print(str(error))
