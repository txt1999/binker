# coding=utf-8
from ad_sys.public_include.manage_public import *
from manage_modules.notice_manage.notice import *



# 获取IP分配信息列表
mg_rest_api.mg_reg_rest_api("/v1.0/icp_updown_log/get_log_list", get_notice_info)


