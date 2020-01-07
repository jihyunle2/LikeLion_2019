from django.db import models

# Create your models here.
#class 대문자로 시작하기
class Posting(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField("Date Published")
    image = models.ImageField(upload_to="image/")
    body = models.TextField()

def __str__(self):
    return self.title





