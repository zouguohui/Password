from django.db import models


# Create your models here.
class Type(models.Model):
    id = models.AutoField(primary_key=True)
    type1 = models.CharField('目录', max_length=50)
    type2 = models.CharField('分类', max_length=50)

    def __str__(self):
        return '%s %s' %(self.type1, self.type2)


class Password(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField('标题', max_length=50)
    user = models.CharField('用户名', max_length=50)
    password = models.CharField('密码', max_length=50)
    url = models.CharField('网址', max_length=100)
    pid = models.ForeignKey(Type, on_delete=models.CASCADE, verbose_name='分类')

    def __str__(self):
        return self.title
