# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
from flask import Flask, redirect, request, url_for
from weixin.login import WeixinLogin

app = Flask(__name__)

app_id = 'wxa6021efa99e473f1'
app_secret = '4875df98f78200b48297271c650f5bdb'
wx_login = WeixinLogin(app_id, app_secret)


@app.route("/login")
def login():
    openid = request.cookies.get("openid")
    next = request.args.get("next") or request.referrer or "/",
    if openid:
        return redirect(next)

    callback = url_for("authorized", next=next, _external=True)
    url = wx_login.authorize(callback, "snsapi_base")
    return redirect(url)


@app.route("/authorized")
def authorized():
    code = request.args.get("code")
    if not code:
        return "ERR_INVALID_CODE", 400
    next = request.args.get("next", "/")
    data = wx_login.access_token(code)
    openid = data.openid
    resp = redirect(next)
    expires = datetime.now() + timedelta(days=1)
    resp.set_cookie("openid", openid, expires=expires)
    return resp


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
