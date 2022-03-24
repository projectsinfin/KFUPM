from django.db import models
from django.contrib.postgres.fields import JSONField
from datetime import date
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class Link(models.Model):
    facebook_url = models.URLField()
    twitter_url = models.URLField()
    linkedin_url = models.URLField()
    youTube_url = models.URLField()
    youTube_video_url = models.URLField()
    alumni_portal = models.URLField()
    KFUPM_News = models.URLField()
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
    
class EducationalPage(models.Model):
    page_title = models.TextField()
    page_content = models.TextField()
    Progam_title_1 = models.TextField()
    Progam_title_2 = models.TextField()
    Progam_title_3 = models.TextField()
    Progam_title_4 = models.TextField()
    
    def __str__(self):              # __unicode__ on Python 2
        return self.page_title
    
class UndergraduateProgramsPage(models.Model):
    page_title = models.TextField()
    title_1 = models.TextField()
    title_1_text = models.TextField()
    title_2 = models.TextField()
    title_2_text = models.TextField()
    title_3 = models.TextField()
    title_3_text = models.TextField()
    title_4 = models.TextField()
    title_4_text = models.TextField()
    
    def __str__(self):              # __unicode__ on Python 2
        return self.page_title
    
class FacultyProgramsPage(models.Model):
    page_title = models.TextField()
    title_1 = models.TextField()
    title_1_text = models.TextField()
    
    
    def __str__(self):              # __unicode__ on Python 2
        return self.page_title
    
class SummerTrainingProgramsPage(models.Model):
    page_title = models.TextField()
    title_1 = models.TextField()
    title_1_text = models.TextField()
    
    
    def __str__(self):              # __unicode__ on Python 2
        return self.page_title

class GraduateProgramsPage(models.Model):
    page_title = models.TextField()
    title_1 = models.TextField()
    title_1_text = models.TextField()
    title_2 = models.TextField()
    title_2_text = models.TextField()
    
    def __str__(self):              # __unicode__ on Python 2
        return self.page_title
    
class CampusCommunityPage(models.Model):
    page_title = models.TextField()
    title_1 = models.TextField()
    title_1_text = models.TextField()
    
    
    def __str__(self):              # __unicode__ on Python 2
        return self.page_title
    
class FaqsPage(models.Model):
    page_title = models.TextField()
    question_1 = models.TextField()
    question_1_text = models.TextField()
    question_2 = models.TextField()
    question_2_text = models.TextField()
    question_3 = models.TextField()
    question_3_text = models.TextField()
    question_4 = models.TextField()
    question_4_text = models.TextField()
    question_5 = models.TextField()
    question_5_text = models.TextField()
    question_6 = models.TextField()
    question_6_text = models.TextField()
    
    def __str__(self):              # __unicode__ on Python 2
        return self.page_title
    
class ContactUsPage(models.Model):
    page_title = models.TextField()
    title_1 = models.TextField()
    email = models.EmailField(max_length = 254)
    phone_no = PhoneNumberField(null=False, blank=False, unique=True)
    place_name = models.CharField(max_length=200)
    
    def __str__(self):              # __unicode__ on Python 2
        return self.page_title
    
class ResearchInnovation(models.Model):
    page_title = models.TextField()
    page_content = models.TextField()
    slider_title = models.TextField()
    research_center_1 = models.TextField()
    research_center_2 = models.TextField()
    research_center_3 = models.TextField()
    research_center_4 = models.TextField()
    research_center_5 = models.TextField()
    research_center_6 = models.TextField()
    research_center_7 = models.TextField()
    research_center_8 = models.TextField()
    research_center_9 = models.TextField()
    research_center_10 = models.TextField()
    research_center_11 = models.TextField()
    research_center_12 = models.TextField()
    research_center_13 = models.TextField()
    research_center_14 = models.TextField()
    research_center_15 = models.TextField()
    research_center_16 = models.TextField()
    title_1 = models.TextField()
    title_1_objective = models.TextField(blank = True)
    title_1_text = models.TextField()
    title_2 = models.TextField()
    title_2_objective = models.TextField(blank = True)
    title_2_text = models.TextField()
    title_3 = models.TextField()
    title_3_objective = models.TextField(blank = True)
    title_3_text = models.TextField()
    title_4 = models.TextField()
    title_4_objective = models.TextField(blank = True)
    title_4_text = models.TextField()
    title_5 = models.TextField()
    title_5_objective = models.TextField(blank = True)
    title_5_text = models.TextField()
    title_6 = models.TextField()
    title_6_objective = models.TextField(blank = True)
    title_6_text = models.TextField()
    
    def __str__(self):              # __unicode__ on Python 2
        return self.page_title
    
class FundsNumber(models.Model):
    page_title = models.TextField()
    main_title = models.TextField()
    number_1 = models.CharField(max_length=200)
    number_1_title = models.TextField()
    number_1_text = models.TextField()
    number_2 = models.CharField(max_length=200)
    number_2_title = models.TextField()
    number_2_text = models.TextField()
    number_3 = models.CharField(max_length=200)
    number_3_title = models.TextField()
    number_3_text = models.TextField()
    number_4 = models.CharField(max_length=200)
    number_4_title = models.TextField()
    number_4_text = models.TextField()
    number_5 = models.CharField(max_length=200)
    number_5_title = models.TextField()
    number_5_text = models.TextField()
    number_6 = models.CharField(max_length=200)
    number_6_title = models.TextField()
    number_6_text = models.TextField()
    number_7 = models.CharField(max_length=200)
    number_7_title = models.TextField()
    number_7_text = models.TextField()
    number_8 = models.CharField(max_length=200)
    number_8_title = models.TextField()
    number_8_text = models.TextField()
    def __str__(self):              # __unicode__ on Python 2
        return self.page_title
    
class PatnerPage(models.Model):
    page_title = models.TextField()
    page_content = models.TextField()
    title_1 = models.TextField()
    title_2 = models.TextField()
    all_patners = models.TextField()
    slider_title = models.TextField()
    research_center_1 = models.TextField()
    research_center_2 = models.TextField()
    research_center_3 = models.TextField()
    research_center_4 = models.TextField()
    research_center_5 = models.TextField()
    research_center_6 = models.TextField()
    research_center_7 = models.TextField()
    research_center_8 = models.TextField()
    
    def __str__(self):              # __unicode__ on Python 2
        return self.page_title