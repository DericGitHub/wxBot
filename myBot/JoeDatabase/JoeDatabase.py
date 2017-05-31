#!/usr/bin/env python2.7

from peewee import *
#class JoeDatabase1(object):
#    @classmethod
#    def JoeDatabase2(cls,db):
#        class JoeDatabase_class(Model):
#            def getOne(cls,*query, **kwargs):
#                try:
#                    return cls.get(*query, **kwargs)
#                except DoesNotExist:
#                    return None
#            class Meta:
#                database = dbclass JoeDatabase1(object):
#    @classmethod
def init_class(db):
    class JoeDatabase_class(Model):
        @classmethod
        def getOne(cls,*query, **kwargs):
            try:
                return cls.get(*query, **kwargs)
            except DoesNotExist:
                return None
        class Meta:
            database = db
    return JoeDatabase_class
