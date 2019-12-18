from flask import Flask, render_template, request, session, redirect
import os
import requests
from captcha import verifyCaptchaValue

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('user')
    password = request.form.get('pass')
    captchaToken = request.form.get('captcha_verification_value')

    privKey = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX" #redacted
    # user=&pass=&captcha_verification_value=
    r = requests.get('http://127.0.0.1:{}/captchaVerify?captchaUserValue={}&privateKey={}'.format(str(port), captchaToken, privKey))
    #backdoored ;)))
    if username == "backd00r" and password == "catsrcool" and r.content == b'allow':
        session['logged'] = True
        return redirect('//redacted//')
    else:
        return "login failed"


@app.route('/captchaVerify')
def captchaVerify():
    #only 127.0.0.1 has access
    if request.remote_addr != "127.0.0.1":
        return "Access denied"

    token = request.args.get('captchaUserValue')
    privKey = request.args.get('privateKey')
    #TODO: remove debugging privkey for testing: 8EE86735658A9CE426EAF4E26BB0450E from captcha verification system
    if(verifyCaptchaValue(token, privKey)):
        return str("allow")
    else:
        return str("deny")

# user=backd00r&pass=catsrcool&captcha_verification_value=d1zYAxV5Uk%26privateKey=8EE86735658A9CE426EAF4E26BB0450E
# ===> /dashboard_jidcc88574c

# /static/hidden_directory_1337_781/098c533dc5420628a9f51c1911198c4c.jpg
# /static/hidden_directory_1337_781/2.jpg
# /wtf.mp4  => 404  세션이 있으면 다운받아짐. 이 영상에 플래그가 있음

