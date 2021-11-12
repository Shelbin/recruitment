from django.db import models
from django.contrib.auth.models import User

# Create your models here.
JobTypes = [
    (0, "技术类"),
    (1, "产品类"),
    (2, "运营类"),
    (3, "设计类"),
]

Cities = [
    (0,"北京"),
    (1,"上海"),
    (2,"深圳"),
    (3,"广州"),
]

# 需要把这个model注册到管理后台才可使用
class Jobs(models.Model):
    job_type = models.SmallIntegerField(blank=False, choices=JobTypes, verbose_name="职位类别")
    job_name = models.CharField(max_length=250, blank=False, verbose_name="职位名称")
    job_city = models.SmallIntegerField(choices=Cities, blank=False, verbose_name="工作地点")
    job_responsibility = models.TextField(max_length=1024, verbose_name="职位职责")
    job_requirement = models.TextField(max_length=1024, blank=False, verbose_name="职位要求")
    # 创建者，定义为我们系统自带的用户，当前的登录用户，可以用models的外键引用
    # 外键引用，删除一个用户的时候，这个职位里面的用户就无效了，涉及到删除一个用户的时候，外键关联如何处理 on_delete
    creator =  models.ForeignKey(User, verbose_name="创建人", on_delete=models.SET_NULL, null=True)
    created_date = models.DateTimeField(verbose_name="创建日期")
    modified_date = models.DateTimeField(verbose_name="修改时间")
