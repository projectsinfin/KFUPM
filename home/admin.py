from django.contrib import admin
from .models import *
# Register your models here.

class form_Data(admin.ModelAdmin):
    list_display=('kfupm_id_number','name','e_mail','mobile','amount','date')
    list_filter=('kfupm_id_number',)
    search_fields=('kfupm_id_number','name','e_mail','mobile','amount','date',)

admin.site.register(HomePage)
admin.site.register(IntroductionPage)
admin.site.register(Link)
admin.site.register(VisionAndMissionPage)
admin.site.register(OurCommitment)
admin.site.register(EducationalPage)
admin.site.register(UndergraduateProgramsPage)
admin.site.register(FacultyProgramsPage)
admin.site.register(SummerTrainingProgramsPage)
admin.site.register(GraduateProgramsPage)
admin.site.register(CampusCommunityPage)
admin.site.register(FaqsPage)
admin.site.register(ContactUsPage)
admin.site.register(ResearchInnovation)
admin.site.register(FundsNumber)
admin.site.register(PatnerPage)
admin.site.register(FormData,form_Data)
admin.site.register(NewsLetter)