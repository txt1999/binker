#coding=utf-8
'''
Created on 2014-12-12

@author: Administrator
'''
from adweb.sys_interface import ad_web_rest
from modules.icp_updown_log.code import views

ad_web_rest.web_reg_rest_api("/v1.0/icp_updown_log/get_log_list", views.get_log_list)


# ad_web_rest.web_reg_one_level("系统管理", 5, 'sys_manage.png')
# ad_web_rest.web_reg_two_level("系统管理", "待办事项", 1,"/v1.0/system_manage/system_param_config/get_work_list")
