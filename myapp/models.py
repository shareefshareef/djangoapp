from django.db import models

# Create your models here.

class Tweets(models.Model):
    topic = models.CharField(max_length=30,null=False,blank=False)
    tweet = models.CharField(max_length=150,null=False,blank=False)
    pub_date  = models.DateTimeField()

    def __str__(self):
        return self.topic 
