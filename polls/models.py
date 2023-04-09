import datetime
from datetime import timezone
from django.db import models
from django.contrib.auth.models import User

    
# models
class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200, blank=True)
    
    def __str__(self):
        return self.name
    
class Nominee(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='nominee_images/', blank=True)
    description = models.CharField(max_length=200, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.name
    
class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nominee = models.ForeignKey(Nominee, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.user} voted for {self.nominee}'


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published", auto_now_add=True)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now