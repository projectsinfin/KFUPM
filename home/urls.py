from django.urls import path

from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', views.index, name='index'),
    path('introduction', views.intro, name='intro'),
    path('vision', views.vision, name='vision'),
    path('kfupm-funds', views.facts, name='kfupm-funds'),
    path('commitments', views.commitment, name='commitments'),
    path('contribute', views.intro, name='contribute'),
    path('educational', views.educational, name='educational'),
    path('undergraduate', views.undergraduate, name='undergraduate'),
    path('graduate-programs', views.graduate, name='graduate'),
    path('summer-traning-programs', views.summertraning, name='summertraning'),
    path('faculty-programs', views.faculty, name='faculty'),
    path('research', views.research, name='research'),
    path('community', views.campus_community, name='community'),
    path('partner', views.partner, name='patners'),
    path('online-contribution', views.contribution_online, name='online-contribution'),
    path('contribution-form', views.contribution, name='contribution-form'),
    path('FAQs', views.faq, name='FAQS'),
    path('contactUS', views.contact_us, name='contactUS'),
    path('newletter',csrf_exempt(views.new_letter), name='newletter'),
    path('submit-form', views.from_data, name='submit-form'),
    
]