from django.db import models

# Create your models here.
# Not much foreign key,poor design but smooth to code.

class Category(models.Model):
    # restrauts category
    cid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)


class Restraut(models.Model):
    # res information
    rid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    description = models.TextField()
    average_rate = models.CharField(max_length=100)
    comment_num = models.IntegerField()
    cate = models.ForeignKey(to="category", to_field="cid", on_delete=None)

    def comment_add(self):
        self.comment_num += 1

    def new_average(self, rate):
        rate = float(rate)
        self.average_rate = str(round(((self.comment_num-1)*float(self.average_rate)+rate)/self.comment_num,2))


class Comment(models.Model):
    cid = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    price = models.CharField(max_length=100)
    man_num = models.IntegerField()
    service_fee = models.CharField(max_length=100)
    is_anoym = models.IntegerField()
    rate = models.CharField(max_length=100)
    # 1 for is,0 for not

    # fkey
    res = models.ForeignKey(to="restraut", to_field="rid", on_delete=None)
    content = models.TextField()

    like_num = models.IntegerField()
    dislike_num = models.IntegerField()

    def add_like(self):
        self.like_num += 1

    def add_dislike(self):
        self.dislike_num += 1


class Reply(models.Model):
    rid = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    reply_to_id = models.IntegerField()
    reply_type = models.IntegerField()
    reply_to_uid = models.IntegerField(null=True)

    comment_id = models.IntegerField(null=True)

    content = models.TextField()


class User(models.Model):
    uid = models.AutoField(primary_key=True)

    # comments: one user to many
    # replies: one user to many
    # likes: one user to many
    # dislikes: one user to many
