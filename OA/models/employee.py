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


