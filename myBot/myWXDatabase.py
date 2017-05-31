#!/usr/bin/env python2.7
from JoeDatabase import JoeDatabase
from peewee import *
import ConfigParser
import functools
import datetime
import os

class myWXDatabaseOperate():

    ##################################################
    #       __init__
    ##################################################
    def __init__(self):

        self.db_ini = None
        self.db_name = None
        self.db = None
        self.db_table_class = {}


        self.set_db_ini()
        self.set_db()
        self.set_db_table()

    ##################################################
    #       set_db_ini
    ##################################################

    def set_db_ini(self):
        cf = ConfigParser.ConfigParser()
        #create Database.ini if not exists.
        if not os.path.isfile('Database.ini'):
            print "Could not read Database.ini."
            self.db_ini = open('Database.ini','w')
            self.db_ini.close()
        else:
            self.db_ini = 'Database.ini'
        #read Database.ini for ConfigParser
        #set self.database
        cf.read('Database.ini')
        try:
            self.db_name = cf.get('DB','DB_FILE')
        except:
            self.db_name = 'myWXBot.db'
        #check if self.database exists
        if os.path.isfile(self.db_name):
            print "Get database : %s" %(self.db_name)
        else:
            #if database info does not exist in ini file, add a item.
            try:
                cf.add_section('DB')
            except:
                pass
            cf.set('DB','db_file',self.db_name)
            cf.write(open(self.db_ini,'w')) 
            
    ##################################################       
    #       set_db
    ##################################################       

    def set_db(self):
        #load db file
        self.load_db(self.db_name)
        #connect db file
        self.connect_db()
        print "Load and connect to %s" %(self.db_name)

    def load_db(self,db_name):
        self.db = SqliteDatabase(self.db_name)

    def connect_db(self):
        self.db.connect()

    ##################################################
    #       set_db_table
    ##################################################
    
    def set_db_table(self):
        self.set_db_table_class()
        self.create_table_if_necessary(self.db_table_class)

    def set_db_table_class(self):
        #db_table_class : 'user':class_instance
        self.create_WXDatabase_classes()
        #for class_instance in self.create_WXDatabase_classes():
            #self.db_table_class.update(class_instance)
        print self.db_table_class

    def create_WXDatabase_classes(self):
        #modify the classes_list to support more tables
        base_class = JoeDatabase.init_class(self.db)

        class user_table(base_class):
            wx_id = CharField(unique = True,primary_key = True)
            name = CharField()
            points = IntegerField(default = 0)
            level = CharField(default = 'low')
            timestamp = DateTimeField(default = datetime.datetime.now)

        class chat_history_table(base_class):
            wx_id = ForeignKeyField(user_table,related_name='chat_history')
            friend_id = CharField()
            to_me = BooleanField()
            content = TextField()
            timestamp = DateTimeField(default = datetime.datetime.now)
        self.db_table_class = {
        'user':user_table,
        'chat_history':chat_history_table,
        }
        
        

        #return ({class_name:class_address()} for class_name,class_address in classes_list.items())

    #create a peewee class with db specificed
#    def create_user_class(self):
#        db_tmp = self.db
#        class user_table(JoeDatabase.init_class(db_tmp)):
#            wx_id = CharField(unique = True,primary_key = True)
#            name = CharField()
#            points = IntegerField(default = 0)
#            level = CharField(default = 'low')
#            timestamp = DateTimeField(default = datetime.datetime.now)
#        return user_table
#
#    def create_chat_history_class(self):
#        father = self
#        db_tmp = self.db
#        class chat_history_table(JoeDatabase.init_class(db_tmp)):
#            wx_id = ForeignKeyField(father.db_table_class['user'],related_name='chat_history')
#            friend_id = CharField()
#            to_me = BooleanField()
#            content = TextField()
#            timestamp = DateTimeField(default = datetime.datetime.now)
#        return chat_history_table


    def create_table_if_necessary(self,table_class):
        self.db.create_tables(self.get_all_class_instance(),safe = True)

    def get_all_class_instance(self):
        return [class_instance for class_name,class_instance in self.db_table_class.items()]

    ##################################################
    #       Decorator
    ##################################################
         
    def check_user_exist(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print 'Check user exist before call %s' % func.__name__
            try:
                if args[0].get_user(args[1]) != None:
                    return func(*args,**kw)
            except:
                try:
                    if args[0].get_user(kw['wx_id']) != None:
                        return func(*args,**kw)
                except:
                    print 'could not find user'
            return None
        return wrapper
    def check_user_not_exist(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print 'Check user not exist before call %s' % func.__name__
            try:
                if args[0].get_user(args[1]) == None:
                    return func(*args,**kw)
                else:
                    return None
            except:
                try:
                    if args[0].get_user(kw['wx_id']) == None:
                        return func(*args,**kw)
                    else:
                        return None
                except:
                    print 'could not find user'
            return None
        return wrapper

    ##################################################
    #       Operation
    ##################################################
 
    def get_user(self,wx_id):
        return self.db_table_class['user'].getOne(wx_id=wx_id)

    @check_user_not_exist
    def add_user(self,wx_id,name):
        print 'add wx_id:%s name:%s' % (wx_id,name)
        self.db_table_class['user'].insert(wx_id=wx_id,name=name).execute()

    @check_user_exist
    def remove_user(self,wx_id):
        print 'remove wx_id:%s' % wx_id
        self.db_table_class['user'].getOne(wx_id=wx_id).delete_instance()

    @check_user_exist
    def get_name_by_wx_id(self,wx_id):
        return self.db_table_class['user'].getOne(wx_id=wx_id).name

    @check_user_exist
    def get_timestamp_by_wx_id(self,wx_id):
        return self.db_table_class['user'].getOne(wx_id=wx_id).timestamp

if __name__ == '__main__':
    obj1 = myWXDatabaseOperate()
    obj1.add_user(wx_id='test2',name='test2')
    obj1.remove_user('test2')
    print obj1.get_name_by_wx_id('test1')
