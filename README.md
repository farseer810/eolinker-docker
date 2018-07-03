## 使用
```sh
$ docker run -d -p 8000:80 farseer810/eolinker:4.0
```

接着按官网安装教程提示进入首页完成配置安装，以本机安装以例：   
进入http://localhost:8000   
需要提前自行创建好空数据库   
    
**注意：要记住你配置时填写的数据库信息，重启docker需要用到**

### 重启eolinker容器
```sh
docker run -d -p 8000:80 \
-e IS_REPLICA=true \
-e DB_HOST=db_host \
-e DB_NAME=os_name \
-e DB_USER=db_user -e DB_PASSWORD=db_password \
-e WEBSITE_NAME="website_name" \
farseer810/eolinker:4.0
```
**其中WEBSITE_NAME不是必填的**
**其实也可以用重启eolinker容器的命令开多个实例，再在上层负载均衡**