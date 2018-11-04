1. 安装mongodb  
    1. 设置配置文件，启用密码
    ```
    dbpath=/data/db
    logpath=/data/log
    journal=false
    fork=true
    auth=true
    ```
    2. admin数据库，这只超级管理园
    ```
    use admin
    db.createUser(
        {
        user: "dba",
        pwd: "123456",
        roles: [ { role: "userAdminAnyDatabase", db: admin" },
                { role: "dbAdminAnyDatabase", db: "admin" },
                { role: "clusterAdmin", db: "admin"},
                { role: "dbOwner", db: "admin"}]
        }
    )
    ```
    3. 建立数据库 osr_web,osr_user,osr_sys
    ```
    use osr_web
    db.createrUser(
        {
            user: "root",
            pwd: "123456",
            roles: [ 
                { role: "dbOwner", db: "osr_web" },
                { role: "dbAdmin", db: "osr_web" },
                { role: "readWrite", db: "osr_web" },
                { role: "userAdmin", db: "osr_web" }
            ]
        }
    )
    ```
    4. 启动数据库  
    `mongod --config /data/mongodb.conf`
    5. 数据库基本操作  
        1. 启动 `./mongo`
        2. 登录 `db.auth('root','123456')

2. 安装redis  
    1. 设置配置文件，启用密码
        >编辑`/etc/redis/redis.conf`  
        配置密码将
        `#requirepass foobared`  
        修改为
        `requirepass your-password`
    2. 启动服务 `redis-server`
    3. 使用redis  `redis-cli -a 123456`
