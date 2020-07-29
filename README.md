#项目说明 

Django技术栈 基于 djangorestframework 的REST接口后台开发模板

### 依赖库清单
- python 3.7
- django 2.2
- djangorestframework 3.11

### 代码结构
```
├── apps 用户自定义应用
│   ├── swaggerdoc 接口文档app
│   ├── users 自定义用户app
│   ├── response.py 接口响应
│   └── views.py 定义接口基类
├── backend 后端配置目录
│   ├── dev_settings.py 开发环境配置文件
│   ├── settings.py 生成环境配置文件
│   ├── urls.py 全局路由配置
│   └── wsgi.py WSGI配置
├── docs 项目文档
│   └── 接口文档.yml API文档
├── conf.cnf 项目启动配置文件，包含数据库账号配置等
├── Makefile 接口测试
├── manage.py 命令管理
├── README.md 项目说明文档
├── requirements.txt 项目依赖包清单
└── scripts 脚本文件目录
    └── sql sql脚本文件目录
```
