#!/usr/bin/python
import os

'''
Worker's status code
'''
IDLE = 0
BUSY = 1
'''
Message format

message = {'msg_type_id': msg_type_id,
           'msg_id': msg['MsgId'],
           'content': content,
           'to_user_id': msg['ToUserName'],
           'user': user}
'''
class myWXWorker:
    def __init__(task_queue,output_queue):
        self.status = IDLE
        self.task_queue = task_queue
        self.output_queue = output_queue
        self.pid = os.getpid()
        print 'Worker (%s) started.' % self.pid
    def start():
        self.stauts = BUSY
        while self.stauts == BUSY:
            msg = self.task_queue.get(True)
            print 'Worker (%s) grabed a task' % self.pid
            handle_msg(msg)
    def handle_msg(msg):
        '''
        handle msg here
        '''
        
        '''
        return result to output queue
        '''
        self.output_queue.put(result) 
        print 'Worker (%s) finished task' % self.pid
        
        
