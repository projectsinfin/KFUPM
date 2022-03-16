from django.db import models
from django.contrib.postgres.fields import JSONField
from datetime import date

# Create your models here.
class Link(models.Model):
    facebook_url = models.URLField()
    twitter_url = models.URLField()
    linkedin_url = models.URLField()
    youTube_url = models.URLField()
    youTube_video_url = models.URLField()
    brochure_pdf = models.FileField(upload_to='static/')
    
class HomePage(models.Model):
    title_1 = models.TextField()
    title_1_text = models.TextField()
    title_2 = models.TextField()
    title_2_text = models.TextField()
    title_3 = models.TextField()
    # tile__text = models.TextField()
    # tile_3 = models.TextField()
    title_4 = models.TextField()
    title_4_text = models.TextField()
    title_5 = models.TextField()
    title_5_text = models.TextField()
    
    
    def __str__(self):              # __unicode__ on Python 2
        return self.title_1
    
class IntroductionPage(models.Model):
    page_title = models.TextField()
    title_1 = models.TextField()
    title_1_text = models.TextField()
    title_2 = models.TextField()
    title_2_text = models.TextField()
    
    
    def __str__(self):              # __unicode__ on Python 2
        return self.page_title
    
class VisionAndMissionPage(models.Model):
    page_title = models.TextField()
    title_1 = models.TextField()
    title_1_text = models.TextField()
    title_2 = models.TextField()
    title_2_text = models.TextField()
    
    
    def __str__(self):              # __unicode__ on Python 2
        return self.page_title
    
class OurCommitment(models.Model):
    page_title = models.TextField()
    page_content = models.TextField()
    
    
    def __str__(self):              # __unicode__ on Python 2
        return self.page_title