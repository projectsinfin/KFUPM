from django.http import HttpResponse, JsonResponse ,FileResponse
from django.shortcuts import render,redirect
from .models import *
import os
def get_link():
    Links = Link.objects.all()
    Links = Links[len(Links)-1]
    del Links._state
    del Links.id
    Links = Links.__dict__
    return Links

def index(request):
    content_data = HomePage.objects.all()
    content_data = content_data[len(content_data)-1]
    Links = get_link()
    data = {'title_1':content_data.title_1,
            'title_1_text':[i.strip() for i in content_data.title_1_text.split('\n') if i.strip() != ''],
            'title_2':content_data.title_2,
            'title_2_text':[i.strip() for i in content_data.title_2_text.split('\n') if i.strip() != ''],
            'title_3':content_data.title_3,
            'title_4':content_data.title_4,
            'title_4_text':[i.strip() for i in content_data.title_4_text.split('\n') if i.strip() != ''],
            'title_5':content_data.title_5,
            'title_5_text':[i.strip() for i in content_data.title_5_text.split('\n') if i.strip() != ''],'Links':Links}
    # print(d/ata)
    # del Links['id']
    # data = data.update(Links)
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
    Links = get_link()
    data = {
        'page_title':content_data.page_title,
        'title_1':content_data.title_1,
        'title_1_text':[i.strip() for i in content_data.title_1_text.split('\n') if i.strip() != ''],
        'title_2':content_data.title_2,
        'title_2_text':[i.strip() for i in content_data.title_2_text.split('\n') if i.strip() != ''],'Links':Links}
    print(data)
    return render(request, 'home/introduction.html', data)

def vision(request):
    content_data = VisionAndMissionPage.objects.all()
    content_data = content_data[len(content_data)-1]
    # print(content_data)
    Links = get_link()
    data = {
        'page_title':content_data.page_title,
        'title_1':content_data.title_1,
        'title_1_text':[i.strip() for i in content_data.title_1_text.split('\n') if i.strip() != ''],
        'title_2':content_data.title_2,
        'title_2_text':[i.strip() for i in content_data.title_2_text.split('\n') if i.strip() != ''],'Links':Links}
    print(data)
    return render(request, 'home/vision_mission.html', data)

def commitment(request):
    content_data = OurCommitment.objects.all()
    content_data = content_data[len(content_data)-1]
    del content_data._state
    Links = get_link()
    content_data.page_content = [i.strip() for i in content_data.page_content.split('\n') if i.strip() != '']
    content_data.__dict__['Links']=Links
    print(content_data.__dict__)
    return render(request, 'home/our_commitment.html', content_data.__dict__)

def campus_community(request):
    content_data = CampusCommunityPage.objects.all()
    content_data = content_data[len(content_data)-1]
    del content_data._state
    Links = get_link()
    content_data.title_1_text = [i.strip() for i in content_data.title_1_text.split('\n') if i.strip() != '']
    content_data.__dict__['Links']=Links
    return render(request, 'home/campus_community.html', content_data.__dict__)

def research(request):
    return render(request, 'home/research_&_innovation.html', {})

def educational(request):
    content_data = EducationalPage.objects.all()
    content_data = content_data[len(content_data)-1]
    del content_data._state
    Links = get_link()
    content_data.page_content = [i.strip() for i in content_data.page_content.split('\n') if i.strip() != '']
    content_data.__dict__['Links']=Links
    return render(request, 'home/educational.html', content_data.__dict__)

def undergraduate(request):
    content_data = UndergraduateProgramsPage.objects.all()
    content_data = content_data[len(content_data)-1]
    del content_data._state
    Links = get_link()
    content_data.title_1_text = [i.strip() for i in content_data.title_1_text.split('\n') if i.strip() != '']
    content_data.title_2_text = [i.strip() for i in content_data.title_2_text.split('\n') if i.strip() != '']
    content_data.title_3_text = [i.strip() for i in content_data.title_3_text.split('\n') if i.strip() != '']
    content_data.title_4_text = [i.strip() for i in content_data.title_4_text.split('\n') if i.strip() != '']
    # content_data.title_1_text = [i.strip() for i in content_data.title_1_text.split('\n') if i.strip() != '']
    content_data.__dict__['Links']=Links
    return render(request, 'home/undergraduate_programs.html', content_data.__dict__)

def graduate(request):
    content_data = GraduateProgramsPage.objects.all()
    content_data = content_data[len(content_data)-1]
    del content_data._state
    Links = get_link()
    content_data.title_1_text = [i.strip() for i in content_data.title_1_text.split('\n') if i.strip() != '']
    content_data.title_2_text = [i.strip() for i in content_data.title_2_text.split('\n') if i.strip() != '']
    content_data.__dict__['Links']=Links
    return render(request, 'home/graduate_Programs.html', content_data.__dict__)

def summertraning(request):
    content_data = SummerTrainingProgramsPage.objects.all()
    content_data = content_data[len(content_data)-1]
    del content_data._state
    Links = get_link()
    content_data.title_1_text = [i.strip() for i in content_data.title_1_text.split('\n') if i.strip() != '']
    content_data.__dict__['Links']=Links
    
    return render(request, 'home/summer_training_programs.html', content_data.__dict__)

def partner(request):
    return render(request, 'home/sponsorspartners.html', {})

def facts(request):
    Links = get_link()
    return render(request, 'home/facts_figures.html', {'Links':Links})

def faculty(request):
    content_data = FacultyProgramsPage.objects.all()
    content_data = content_data[len(content_data)-1]
    del content_data._state
    Links = get_link()
    content_data.title_1_text = [i.strip() for i in content_data.title_1_text.split('\n') if i.strip() != '']
    content_data.__dict__['Links']=Links
    return render(request, 'home/faculty_programs.html', content_data.__dict__)

def contribution_online(request):
    return render(request, 'home/online_contribution.html', {})

def contribution(request):
    return render(request, 'home/contribution_form.html', {})

def faq(request):
    content_data = FaqsPage.objects.all()
    content_data = content_data[len(content_data)-1]
    del content_data._state
    Links = get_link()
    content_data.question_1_text = [i.strip() for i in content_data.question_1_text.split('\n') if i.strip() != '']
    content_data.question_2_text = [i.strip() for i in content_data.question_2_text.split('\n') if i.strip() != '']
    content_data.question_3_text = [i.strip() for i in content_data.question_3_text.split('\n') if i.strip() != '']
    content_data.question_4_text = [i.strip() for i in content_data.question_4_text.split('\n') if i.strip() != '']
    content_data.question_5_text = [i.strip() for i in content_data.question_5_text.split('\n') if i.strip() != '']
    content_data.question_6_text = [i.strip() for i in content_data.question_6_text.split('\n') if i.strip() != '']
    # content_data.title_1_text = [i.strip() for i in content_data.title_1_text.split('\n') if i.strip() != '']
    content_data.__dict__['Links']=Links
    return render(request, 'home/faq.html', content_data.__dict__)

def contact_us(request):
    content_data = ContactUsPage.objects.all()
    content_data = content_data[len(content_data)-1]
    del content_data._state
    Links = get_link()
    content_data.__dict__['Links']=Links
    return render(request, 'home/contact_us.html', content_data.__dict__)

def serve_pdf(request):
    filepath = os.path.join('static', 'setup.pdf')
    return FileResponse(open(filepath, 'rb'), content_type='application/pdf')

def from_data(request):
    print(request.POST)
    return JsonResponse({'data':[]})