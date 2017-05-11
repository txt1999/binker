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
            cur_date = time.strftime('%Y-%m-%d',time.localtime(time.time()))  # 默认的日期为当日
            updown = int(self.get_argument)("updown")  # 上传和下载类型，0为上传，1为下载
            start_date = self.get_argument("start_time",cur_date)  # 获取起始日期，默认值为当前日期
            end_date = self.get_argument("start_time", cur_date)  # 获取结束日期，默认值为当前日期
            start_time = start_date + ' 00:00:00'  # 起始时间为开始日期的00:00:00
            end_time = end_date + ' 23:59:59'  # 结束时间为结束日期的23:59:59

            # 调用接口参数
            send_data = dict()
            send_data["updown"] = updown
            send_data["start_time"] = start_time
            send_data["end_time"] = end_time
            send_data["skip"] = rows * (page - 1)
            send_data["limit"] = rows
            send_json = json.dumps(send_data)

            send_manage_url = dict()
            send_manage_url["url"] = "/v1.0/icp_updown_log/get_log_list"
            send_manage_url["timeout"] = 10

            recv_json = yield ad_web_rest.web_send_post(send_manage_url, send_json)
            ret_data = json.loads(recv_json)
            print "icp_updown_log----get_log_list, ret_data ===", ret_data
            if ret_data.has_key("code") and ret_data["code"] == 0:
                self.write(ret_data) 
        except:
            traceback.print_exc()