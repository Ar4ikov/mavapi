import mavapi
'''
    Тест #2. Запросы к API
    Повторяем процедуру из теста #1
'''

api = mavapi.API('сервер')
try:
    access_token = api.Auth('access_token')
except mavapi.MAVAPIAuthError as error:
    print(str(error))
else:
    '''
        method -> обязательный параметр, указывает, к какому методу мы хотим обратиться
        после метода идут кварги, указывайте в них всё, что требует от Вас API
    '''

    getTokenPerms = api.getRequest(method='getTokenPerms')
    getUser = api.getRequest(method='getUser', mav_id=16)