import time
from models import Model
from models.MyMongo import MyMongo
from models.mysql import myMysql

class Category(Model):
    def __init__(self, form):
        self.id = None
        self.title = form.get('title', '')
        self.ct = int(time.time())
        self.ut = self.ct


# class Category(MyMongo):
#     __fields__ = MyMongo.__fields__ +[
#         ('title', str, ''),
#     ]


# class Category(myMysql):
#     fields = myMysql.fields+[
#         'title',
#     ]




