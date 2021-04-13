# IotServer (Django REST Framwork)

## run the server 
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

## using anaconda to handle virtual environment
```
conda env export > environment.yml   ## expport requried packages
conda env update --file environment.yml    ## update env packages
```

## utils API
### mail certification
```
url : http://140.117.71.98:8000/utils/mail_certification/
method : POST
data : mail
response : success->是否成功寄出認證信件
```
