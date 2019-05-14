import time
from models import Model
from models import load
from models.MyMongo import MyMongo
from models.mysql import myMysql
from models.mysql import mysqlHelper


class Page(Model):
    @classmethod
    def new(cls, form,**kwargs):
        t = cls(form)
        for k,v in kwargs:
            setattr(t,k,v)
        t.save()
        return t

    @classmethod
    def all(cls,page = 0,size =5):
        path = cls.db_path()
        models = load(path)
        ms = [cls._new_from_dict(m) for m in models]
        if page == 0:
            return ms
        else:
            star = (page-1)*size
            end =page*size
            return ms[star:end]


    def __init__(self, form):
        self.id = None
        self.title = form.get('title', '')
        self.content = form.get('content', '')
        self.desc = form.get('desc','')
        self.author = form.get('author', '')
        self.ct = int(time.time())
        self.ut = self.ct
        self.category = form.get('category','')


    def category(self):
        from .category import Category
        m = Category.find(self.category)
        return m


# class Page(MyMongo):
#     __fields__ = MyMongo.__fields__ + [
#         ('title', str, ''),
#         ('content', str, ''),
#         ('desc', str, ''),
#         ('author', str, ''),
#         ('category', str, '')
#     ]
#
#
#     def category(self):
#         from .category import Category
#         m = Category.find(self.category)
#         return m
#
#     @classmethod
#     def all(cls,page = 0,size =5):
#         ms = cls.find_outside()
#         if page == 0:
#             return ms
#         else:
#             star = (page-1)*size
#             end =page*size
#             return ms[star:end]


# class Page(myMysql):
#     fields = myMysql.fields + [
#         'title',
#         'content',
#         'desc',
#         'author',
#         'category',
#     ]
#
#     @classmethod
#     def all(cls,page = 0,size =5):
#         name = cls.__name__
#         sql = 'SELECT * FROM {}'.format(name)
#         all = list(mysqlHelper.get_all(sql))
#         if page == 0:
#             return all
#         else:
#             star = (page-1)*size
#             end =page*size
#             return all[star:end]