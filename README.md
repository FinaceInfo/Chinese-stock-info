# 国内A股信息获取服务

这个服务使用tushare来获取股票信息,采用restful风格的接口设计.

# 测试

`nosetests --py3where=test  --with-coverage --cover-package=app,api,download -v --cover-html
 --cover-html-dir=src/uchtml`
