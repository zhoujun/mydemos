# -*- coding: utf-8 -*-

from weixin import WeixinMP, WeixinError


app_id = 'wxa6021efa99e473f1'
app_secret = '4875df98f78200b48297271c650f5bdb'
mp = WeixinMP(app_id, app_secret)

# 获取菜单
try:
    print mp.menu_get()
except WeixinError:
    pass

# 创建菜单
button = [
    {
        "type": "view",
        "name": "测试",
        "url": "http://code.show/",
    },

    {
        "name": "菜单",
        "sub_button": [
            {
                "type": "view",
                "name": "搜索",
                "url": "http://wwww.soso.com/"
            },
            {
                "type": "view",
                "name": "视屏",
                "url": "http://v.qq.com"
            }
        ]
    }

]
print mp.menu_create(button)
