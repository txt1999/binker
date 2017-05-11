# coding=utf-8
import tornado.web
from adweb.sys_interface import ad_web_rest
from tornado.gen import coroutine
import socket
import struct
import json
from adweb.syshead import *

class get_log_list(BaseHandler):
    @coroutine
    def post(self):
        try:
            # 默认参数
            page = self.get_argument("page", 1)  # 页码
            rows_limit = self.get_argument("rows", 50)  # 显示条数

            # 查询参数
            updown = int(self.get_argument)("updown")  # 上传和下载类型，0为上传，1为下载
            start_date = self.get_argument("start_time")

        except:
            traceback.print_exc()