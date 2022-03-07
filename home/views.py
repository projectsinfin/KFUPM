from django.http import HttpResponse, JsonResponse ,FileResponse
from django.shortcuts import render,redirect
import os

def index(request):
    return render(request, 'home/index.html', {})

def intro(request):
    return render(request, 'home/introduction.html', {})

def vision(request):
    return render(request, 'home/vision_mission.html', {})

def commitment(request):
    return render(request, 'home/our_commitment.html', {})

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