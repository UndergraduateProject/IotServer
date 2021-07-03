# IotServer (Django REST Framwork)

## Models
### Plantimg

路徑為 ```media/year/month+day/hour+minnute.jpg``` e.g."media/2021/0621/2127.jpg"

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

### watering
```
url -> http://127.0.0.1:8000/utils/mail_certification/
method -> POST
data -> volum  #這邊要在思考需要甚麼data
response -> {INFO : 'message'}
```

### mail certification
```
url -> http://140.117.71.98:8000/utils/mail_certification/
method -> POST
data -> mail
response -> {INFO : 'message'}
```

## auth API

### register
```
url -> http://140.117.71.98:8000/user/register/
method -> POST
data -> username, password, email
response -> {user : user detail} 
response fail -> {use}
```

### login
```
url -> http://140.117.71.98:8000/user/register/
method -> POST
data -> username, password
response -> {user : user detail, token : a hash number}
```

### logout
```
url : http://140.117.71.98:8000/user/register/
method -> POST
data -> {}
response -> {}
```

## some notes
> hyperlink 所對應的attr必須和models裡面定義的一樣
> code不可以有print，不然run background會報錯

