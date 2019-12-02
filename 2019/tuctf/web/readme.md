# tuctf web
서버가 닫혀서 기억나는대로 끄적여본다.

# ?
html 코드 주석에 플래그가 있었다.

# ?


# ?
SSTI 문제. 주석 TODO에 있는 내용을 보고 welcome/test로 접속하는데, test 부분에서 취약점 발생. `__import__('os').listdir(".")`로 현재 디렉토리 리스트 확인하면 `flag.txt` 있음. 이거를 읽으면 해결.

# ?
세개의 페이지를 찾을 수 있는데, 네트워크 장비 기기의 로그인 페이지로 보인다. 해당 장비의 디폴트 아이디와 비밀번호를 찾아서 넣으면 된다. `admin / admin`으로 해결.

# ?
`admin.php` 접근하여 injection으로 간단하게 우회가 되고, 들어가면 서치가 있다.

# ?
풀지는 못했는데 time based 인젝션이 먹힌다. `union`, `select`, `sleep`이 필터링 되어있고, 쿼터가 들어갈 경우 `or`가 막히는데 `benchmark`함수를 이용하면 time based 공격이 가능하다. or 때문에 information_schema를 참조하지 못해서 적당한 조건이 떠오르지 않아서 추가 공격을 하지 못했다. 마지막 공격 쿼리는 다음과 같다. `'||if(1=2,1,benchmark(50000000,md5('a')))#`