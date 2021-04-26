# IotServer (Django REST Framwork)

### To do list
- [x] url filters
- [ ] verify 邏輯要確定
- [x] modelviewset 要加上hyperlink
- [x] mqtt   ##change to socket 
- [x] sqlite 更新問題

## Run the server 
```
python manage.py runserver 0.0.0.0:8000
```
如果在不同網路下測試 要在setting加上ALLOWED HOST

runserver的command 改成自己的private IP

## ssh connection (using command line)
```
ssh root@140.117.71.98
password:rootroot
```

## Using anaconda to handle virtual environment
```
conda env export > environment.yml   ## expport requried packages
conda env update --file environment.yml    ## update env packages
```

## utils API
### mail certification
```
url -> http://140.117.71.98:8000/utils/mail_certification/
method -> POST
data -> mail
response -> {success : 是否成功寄出認證信件}
```

## auth API
### register
```
url -> http://140.117.71.98:8000/auth/register/
method -> POST
data -> username, password, email
response -> {user : user detail} 
```
### login
```
url -> http://140.117.71.98:8000/auth/register/
method -> POST
data -> username, password
response -> {user : user detail, token : a hash number}
```
### logout
```
url : http://140.117.71.98:8000/auth/register/
method -> POST
data -> {}
response -> {}
```

## some notes
> hyperlink 所對應的attr必須和models裡面定義的一樣

