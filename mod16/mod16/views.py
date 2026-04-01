from django.shortcuts import render

def index(request):
    apps = [
        {"name": "App ", "url": "/q1/", "icon": "1", "color": "linear-gradient(135deg, #3B82F6 0%, #2DD4BF 100%)"},
        {"name": "App ", "url": "/q2/", "icon": "2", "color": "linear-gradient(135deg, #8B5CF6 0%, #EC4899 100%)"},
        {"name": "App ", "url": "/q3/", "icon": "3", "color": "linear-gradient(135deg, #F59E0B 0%, #EF4444 100%)"},
        {"name": "App ", "url": "/q4/", "icon": "4", "color": "linear-gradient(135deg, #10B981 0%, #3B82F6 100%)"},
        {"name": "App ", "url": "/q6/", "icon": "6", "color": "linear-gradient(135deg, #6366F1 0%, #A855F7 100%)"},
        {"name": "App ", "url": "/q7/", "icon": "7", "color": "linear-gradient(135deg, #F43F5E 0%, #F97316 100%)"},
        {"name": "App ", "url": "/q8/", "icon": "8", "color": "linear-gradient(135deg, #0EA5E9 0%, #10B981 100%)"},
        {"name": "App ", "url": "/q9/", "icon": "9", "color": "linear-gradient(135deg, #D946EF 0%, #8B5CF6 100%)"},
        {"name": "App ", "url": "/q10/", "icon": "10", "color": "linear-gradient(135deg, #14B8A6 0%, #84CC16 100%)"},
        {"name": "App ", "url": "/q11/", "icon": "11", "color": "linear-gradient(135deg, #F97316 0%, #EAB308 100%)"},
        {"name": "App ", "url": "/q12/", "icon": "12", "color": "linear-gradient(135deg, #3B82F6 0%, #8B5CF6 100%)"},
        {"name": "App ", "url": "/q13/", "icon": "13", "color": "linear-gradient(135deg, #EF4444 0%, #D946EF 100%)"},
        {"name": "App ", "url": "/q14/", "icon": "14", "color": "linear-gradient(135deg, #84CC16 0%, #10B981 100%)"},
        {"name": "App ", "url": "/q15/", "icon": "15", "color": "linear-gradient(135deg, #A855F7 0%, #EC4899 100%)"},
        {"name": "App ", "url": "/q19/", "icon": "19", "color": "linear-gradient(135deg, #06B6D4 0%, #3B82F6 100%)"},
    ]
    return render(request, 'index.html', {'apps': apps})
