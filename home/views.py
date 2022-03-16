from django.http import HttpResponse, JsonResponse ,FileResponse
from django.shortcuts import render,redirect
from .models import HomePage, IntroductionPage, Link, VisionAndMissionPage, OurCommitment
import os

def index(request):
    content_data = HomePage.objects.all()
    content_data = content_data[len(content_data)-1]
    # Links = Link.objects.all()
    # Links = Links[len(Links)-1]
    # print(content_data)
    data = {'title_1':content_data.title_1,
            'title_1_text':[i.strip() for i in content_data.title_1_text.split('\n') if i.strip() != ''],
            'title_2':content_data.title_2,
            'title_2_text':[i.strip() for i in content_data.title_2_text.split('\n') if i.strip() != ''],
            'title_3':content_data.title_3,
            'title_4':content_data.title_4,
            'title_4_text':[i.strip() for i in content_data.title_4_text.split('\n') if i.strip() != ''],
            'title_5':content_data.title_5,
            'title_5_text':[i.strip() for i in content_data.title_5_text.split('\n') if i.strip() != '']}
    print(data)
    # [i for i in content_data]
    # print([i.title_1 for i in content_data])
    # for i in content_data:
    #     print(i)
    return render(request, 'home/index.html', data)

def intro(request):
    content_data = IntroductionPage.objects.all()
    content_data = content_data[len(content_data)-1]
    # print(content_data)
    data = {
        'page_title':content_data.page_title,
        'title_1':content_data.title_1,
        'title_1_text':[i.strip() for i in content_data.title_1_text.split('\n') if i.strip() != ''],
        'title_2':content_data.title_2,
        'title_2_text':[i.strip() for i in content_data.title_2_text.split('\n') if i.strip() != '']}
    print(data)
    return render(request, 'home/introduction.html', data)

def vision(request):
    content_data = VisionAndMissionPage.objects.all()
    content_data = content_data[len(content_data)-1]
    # print(content_data)
    data = {
        'page_title':content_data.page_title,
        'title_1':content_data.title_1,
        'title_1_text':[i.strip() for i in content_data.title_1_text.split('\n') if i.strip() != ''],
        'title_2':content_data.title_2,
        'title_2_text':[i.strip() for i in content_data.title_2_text.split('\n') if i.strip() != '']}
    print(data)
    return render(request, 'home/vision_mission.html', data)

def commitment(request):
    content_data = OurCommitment.objects.all()
    content_data = content_data[len(content_data)-1]
    del content_data._state
    content_data.page_content = [i.strip() for i in content_data.page_content.split('\n') if i.strip() != '']
    print(content_data.__dict__)
    return render(request, 'home/our_commitment.html', content_data.__dict__)

def campus_community(request):
    return render(request, 'home/campus_community.html', {})

def research(request):
    return render(request, 'home/research_&_innovation.html', {})

def educational(request):
    return render(request, 'home/educational.html', {})

def undergraduate(request):
    return render(request, 'home/undergraduate_programs.html', {})

def graduate(request):
    return render(request, 'home/graduate_Programs.html', {})

def summertraning(request):
    return render(request, 'home/summer_training_programs.html', {})

def partner(request):
    return render(request, 'home/sponsorspartners.html', {})

def facts(request):
    return render(request, 'home/facts_figures.html', {})

def faculty(request):
    return render(request, 'home/faculty_programs.html', {})

def contribution_online(request):
    return render(request, 'home/online_contribution.html', {})

def contribution(request):
    return render(request, 'home/contribution_form.html', {})

def faq(request):
    return render(request, 'home/faq.html', {})

def contact_us(request):
    return render(request, 'home/contact_us.html', {})

def serve_pdf(request):
    filepath = os.path.join('static', 'setup.pdf')
    return FileResponse(open(filepath, 'rb'), content_type='application/pdf')

def from_data(request):
    print(request.POST)
    return JsonResponse({'data':[]})