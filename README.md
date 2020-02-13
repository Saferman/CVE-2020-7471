### CVE-2020-7471 

这个仓库提供 CVE-2020-7471 Potential SQL injection via StringAgg(delimiter) 漏洞的环境和 POC 

### 受影响的 django 版本

- 1.11 到 1.11.28（不含）
- 2.2 到 2.2.10（不含）
- 3.0 到 3.0.3（不含）

### 下载使用前需要如下操作：

1. 安装 django 漏洞版本，我测试用的是

   ```python
   pip install django==3.0.2 -i https://pypi.tuna.tsinghua.edu.cn/simple
   ```

2. 参考 [https://www.runoob.com/postgresql/windows-install-postgresql.html](https://www.runoob.com/postgresql/windows-install-postgresql.html) 完成 postgres 数据库的安装

3. 新建数据库

   ```sql
   CREATE DATABASE test;
   ```


4. 修改 sqlvul_projects/settings.py 里面的数据库配置，如果上一步你安装用的默认配置（包括设置密码为postgres），就无需修改任何配置，可以跳过这一步

   ```
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'test',         # 数据库名称
           'USER': 'postgres',
           'PASSWORD': 'postgres', # 数据库用户密码
           'HOST': '127.0.0.1',    # 数据库地址
           'PORT': '5432',
       }
   }
   ```

5. 通过 django 初始化数据表

   ```shell
   python3 manage.py migrate
   python3 manage.py makemigrations vul_app
   python3 manage.py migrate vul_app
   ```

然后运行 POC 脚本`CVE-2020-7471.py`就可以了

