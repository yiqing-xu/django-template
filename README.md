# 项目说明 

Django restframework开发模板

### 依赖库清单
- python 3.7
- django 2.2
- djangorestframework 3.11
- channels
- django-redis
- rq

### 实现功能
- 基于restframework的serializer序列化
- 基于jwt的用户token认证  
- 基于redis的缓存(使用django-redis提供的API)
- websocket服务，实现向指定用户和群发消息功能
- 基于rq的异步任务
- 基于模板的swagger接口文档

### 项目运行
```shell script
python manage.py runserver // 启动web服务
python manage.py rqworker  // 启动rq任务
```

### 项目部署
```shell script
gunicorn project.wsgi -b 0.0.0.0:port -w (cpu.count * 2) + 1 
daphne project.asgi:application -b 0.0.0.0 -p port
```

### 代码结构
```
├── apps 
│   ├── user 
|   |—— models.py
│   ├── response.py 
│   └── views.py 
├── project 
│   ├── dev_settings.py 
│   ├── settings.py 
│   ├── urls.py 
│   └── wsgi.py 
├── docs 
│   └── 接口文档.yml 
├── manage.py 
├── README.md 
├── requirements.txt 
|—— nginx.conf
|—— supervisor.ini
```
