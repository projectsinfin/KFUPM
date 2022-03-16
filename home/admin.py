from django.contrib import admin
from .models import HomePage, IntroductionPage, Link, VisionAndMissionPage, OurCommitment
# Register your models here.

# class home_page_data(admin.ModelAdmin):
#     list_display=('user','region','query','pubnum','tech_area')
#     list_filter=('user',)
#     search_fields=('user','region','query','pubnum','tech_area')

admin.site.register(HomePage)
admin.site.register(IntroductionPage)
admin.site.register(Link)
admin.site.register(VisionAndMissionPage)
admin.site.register(OurCommitment)