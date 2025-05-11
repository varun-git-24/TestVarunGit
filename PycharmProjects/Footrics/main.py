import json

from fastapi import FastAPI

my_app_obj = FastAPI()


@my_app_obj.get('/')
def user_name():
    d = '{"Varusha":{"relation":"love","age":"28"},"trips":["Ooty","Kashmir","Coorg"]}'
    out = json.loads(d)
    return out


@my_app_obj.get('/food')
def user_fav():
    f = '{"Chinese":["Noodles","Momos"],"Indian":["Idli","Vada"]}'
    out = json.loads(f)
    return out

#print(user_name())
