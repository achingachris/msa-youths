import datetime
from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    description = models.CharField(max_length=200, null=True, blank=True)
    pub_date = models.DateTimeField("date published", auto_now_add=True)
    
    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text
    
# nomination category
class NominationCategory(models.Model):
    category_name = models.CharField(max_length=200)
    description = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='uploads/', null=True, blank=True)
    
    def __str__(self):
        return self.category_name
    
    class Meta:
        verbose_name_plural = "Nomination Categories"
        
# nominee
class Nominee(models.Model):
    nominee_name = models.CharField(max_length=200)
    category = models.ForeignKey(NominationCategory, on_delete=models.CASCADE)
    description = models.CharField(max_length=200, null=True, blank=True)
    tiktok = models.CharField(max_length=200, null=True, blank=True)
    instagram = models.CharField(max_length=200, null=True, blank=True)
    facebook = models.CharField(max_length=200, null=True, blank=True)
    youtube = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='uploads/', null=True, blank=True)
    
    def __str__(self):
        return self.nominee_name
    
    class Meta:
        verbose_name_plural = "Nominees"