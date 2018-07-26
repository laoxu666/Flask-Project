### Flask 项目结构规划
- 创建一个App包，主要用来放我们的应用
- 在App包中的入口文件 __init__.py 中创建Flask程序，并进行初始化
    - 初始化Flask自己
    - 使用配置文件，在Flask上进行设置
    - 初始化蓝图，也就是初始化Views
    - 初始化第三方，初始化ext
    
    
#### 项目结构
- manage.py    用来全局控制我们的项目
- App          代表项目
    - App/__init__    初始化，使用进行项目初始化
    - App/views         视图函数，用来处理我们的请求
        - views中使用蓝图进行的实现
    - App/models        模型，用来定义和数据映射的对象的
        - 使用orm进行实现
    - App/settings      设置，配置，App应用的配置文件
        - 全局配置
        - 设置多套环境的配置
    - App/ext           扩展库，第三方扩展库统一管理 
        - 轻量级框架
        - 第三方插件多，可以统一处理



##### 配置
- 企业中开发中，可能同时拥有多套运行环境
- 可以直接写一个文件，实现多套环境的配置
- 环境中有很多通用部分，我们可以进行一个代码提取



##### flask-migrate
- 数据库迁移
- 使用流程
    - 安装 pip install flask-migrate
    - 进行初始化
        - 在ext中进行初始化
        - 迁移库需要同时绑定app和db
        
- 使用方法（原生方法，针对默认结构有效，修改的结构需要额外配置）
     - flask db init 
     - flask db migrate
     - flask db upgrade 
     - flask db downgrade
     - flask db -- help 

- 集成 flask-script 使用
    - 按照使用流程进行配置
    - 添加和flask-script对接的代码
    - 就是在manager中添加命令 manager.add_command('db', MigrateCommand)
    - 使用
        - python manage.py db init 
            - 初始化，每个项目只调用一次，生成迁移结构
        - python manage.py db migrate
            - 生成迁移文件，会在根目录生成迁移文件
            - 调用时机，每次修改model之后
        - python manage.py db upgrade
            - 执行迁移文件
            - 将修改映射到数据库中，增量的
        - python manage.py db downgrade
            - 执行迁移文件
            - 降级操作
            - 吃后悔药 
        - python manage.py db --help
            - 查看帮助
            
            
#### 模型定义
- 类型定义
- 约束定义
    - index 索引，不要乱用
    - 它会额外维护索引表
    - 比较常用的场景，pk，fk
    - 不常修改还非常具有代表性的字段
    
    
###### 数据查询
- query.all()       返回的是list，列表
- query.filter(条件)      返回的是BaseQuery
- query.filter_by(条件)   级联查询常用
- offset                偏移，跳过多少条
- limit                 限制结果集
- order_by              排序
- get                   获取单个资源
- first                 第一条（没有最后一条，没有last）
- paginate              分页



### 分页加载
- 优化数据的加载
- 分页核心点
    - 哪一页
    - 每一页多少数据
    - 对哪一个数据做的分页

- django中
    - 需要将分页数据传递给分页器
- flask中不需要
    - 分页器是使用数据模型对象获取出来
- 分页中内容
    - items 页面数据
    - has_prev 是否有上一页
    - has_next 是否有下一页
    - prev_num 上一页的页码
    - next_num 下一页的页码
    - iter_pages 迭代页面


#### 模型关系
- 1:1
- 1:M
    - 一个外键实现
    - 在多中声明外键关系
- M:N
    - 额外存在一张关系表
    - 关系表中存在两个两个外键
    - 两个外键关联到两张表的主键上

#### 元信息
- __tablename__  表名
- __abstract__ = True  是否抽象
    - 模型抽象可以复用结构
    - 如果不加的话，是不能够正常使用的


#### flask内置对象
- g
    - global
    - 可以在一个请求中，提供跨函数，跨内容的数据传输
    - 在刚进入请求的时候存入数据，在后续函数中或者模板中进行数据的获取

- request
- session
- config
    - 整个项目配置文件
    - 在python文件中存在current_app
        - 正在运行的项目
        - 使用一定记得注意，需要在项目之后才能获取


#### Flask AOP
- 面向切面编程
- 在不修改原有代码的情况下，实现对逻辑的控制
- 在django中具体展现形式叫做中间件
- flask中使用装饰器实现
    - 切点
        - before_request
        - error_handler
    - 蓝图的切点优先级低于app的
    - 蓝图的异常捕获，只能捕获本蓝图中发生的异常
    - 全局能够一直获取，应该app来注册

