# log4mongo_log
使用Python的日志框架，结合MongoDB存储日志，比较简单的demo

*common* 公共配置存储  
*consumer* 存储测试脚本  
*pipeline*  使用mongoengine连接mongo,及操作  
*producer*  日志配置存储  
*utils* 工具存储

*本想自己搭建一个mongo日志存储中心，发现未能很好结合logging模块，后面在网上找到log4mongo库,
能够较好的结合logging, 参考连接: https://www.jianshu.com/p/bcd8b775c624
这里参考做了一个demo, 旧方式介绍了如何获取本地IP，运行进程号, 闭包的使用等等, 搞不懂为什么案例的方式不能存储INFO级别,
如果有好的建议, 欢迎留言交流 qq: 3184436402*