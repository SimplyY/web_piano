from django.db import models
# 用户信息表：用户编号，用户名，邮箱，密码。

class User(models.Model):
    name = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=30)

    def __str__(self):
        return "用户名: %s, email: %s, password: %s)" % (self.name, self.email, self.password)


# 钢琴表：编号，标题，简介，品牌，价格，使用时间，图片链接，外键卖家id。
class Piano(models.Model):
    title = models.CharField(max_length=20, unique=True)
    info = models.CharField(max_length=200)
    brand = models.CharField(max_length=20)
    price = models.CharField(max_length=10)
    use_time = models.CharField(max_length=20)
    image_link = models.CharField(max_length=20)
    seller = models.ForeignKey(User)

    def __str__(self):
        return "标题" + self.title


# 评论表：评论id，评论内容，外键评论人id，外键钢琴id。
class Comment(models.Model):
    content = models.CharField(max_length=200)
    user = models.ForeignKey(User)
    piano = models.ForeignKey(Piano)

    def __str__(self):
        return "评论id: %s ，评论人：%s" + (self.id, self.content)
