#!/usr/bin/env python
# coding: utf-8
#

from wxbot import *
import cv2

class MyWXBot(WXBot):
    def handle_msg_all(self, msg):
        print msg
        if msg['msg_type_id'] == 4 and msg['content']['type'] == 0 and msg['content']['data'] == u'\u751f\u6210\u5934\u50cf':
            msg1 = 'save headicon to'+self.get_head_img(msg['user']['id'])
            print msg1
            self.send_msg_by_uid(self.to_unicode(msg1), msg['user']['id'])
            headicon = cv2.imread('temp/'+headicon_path,0)
            #self.send_img_msg_by_uid("img/1.png", msg['user']['id'])
            #self.send_file_msg_by_uid("img/1.png", msg['user']['id'])
'''
    def schedule(self):
        self.send_msg(u'张三', u'测试')
        time.sleep(1)
'''


def main():
    bot = MyWXBot()
    bot.DEBUG = True
    bot.conf['qr'] = 'tty'
    bot.run()


if __name__ == '__main__':
    main()
