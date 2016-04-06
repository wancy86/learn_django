import datetime
from django.db import models
from django.utils import timezone

# SublimeCodeIntel
# 只能提示插件
# http://www.cnblogs.com/dolphin0520/archive/2013/04/29/3046237.html
# 重启sublime，打开个python文件，按ctrl+shift+space，这时候第一次运行会去下载一些东西，可以按ctrl+~来看进度 之后就ok了
# 
class Employee(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


# no changes added to commit (use "git add" and/or "git commit -a")
# Please input comment:
# SublimeCodeIntel
# [master 8dba20f] SublimeCodeIntel
#  1 file changed, 1 insertion(+), 1 deletion(-)
# Warning: Permanently added the RSA host key for IP address '192.30.252.120' to the list of known hosts.
# Enter passphrase for key '/c/Users/Mark/.ssh/id_rsa':
# Counting objects: 5, done.
# Delta compression using up to 4 threads.
# Compressing objects: 100% (5/5), done.
# Writing objects: 100% (5/5), 594 bytes | 0 bytes/s, done.
# Total 5 (delta 3), reused 0 (delta 0)
# To git@github.com:wancy86/learn_django.git
#    0d8a169..8dba20f  master -> master