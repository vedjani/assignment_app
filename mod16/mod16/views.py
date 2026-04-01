from django.shortcuts import render

def index(request):
    apps = [
        {"name": "App 1", "url": "/q1/", "icon": "calculate", "color": "linear-gradient(135deg, #FF6B6B 0%, #FF8E53 100%)"},
        {"name": "App 2", "url": "/q2/", "icon": "description", "color": "linear-gradient(135deg, #4facfe 0%, #00f2fe 100%)"},
        {"name": "App 3", "url": "/q3/", "icon": "data_usage", "color": "linear-gradient(135deg, #43e97b 0%, #38f9d7 100%)"},
        {"name": "App 4", "url": "/q4/", "icon": "people", "color": "linear-gradient(135deg, #fa709a 0%, #fee140 100%)"},
        {"name": "App 6", "url": "/q6/", "icon": "build", "color": "linear-gradient(135deg, #30cfd0 0%, #330867 100%)"},
        {"name": "App 7", "url": "/q7/", "icon": "shopping_cart", "color": "linear-gradient(135deg, #a18cd1 0%, #fbc2eb 100%)"},
        {"name": "App 8", "url": "/q8/", "icon": "home", "color": "linear-gradient(135deg, #ff0844 0%, #ffb199 100%)"},
        {"name": "App 9", "url": "/q9/", "icon": "dashboard", "color": "linear-gradient(135deg, #f77062 0%, #fe5196 100%)"},
        {"name": "App 10", "url": "/q10/", "icon": "analytics", "color": "linear-gradient(135deg, #11998e 0%, #38ef7d 100%)"},
        {"name": "App 11", "url": "/q11/", "icon": "settings", "color": "linear-gradient(135deg, #fc4a1a 0%, #f7b733 100%)"},
        {"name": "App 12", "url": "/q12/", "icon": "camera", "color": "linear-gradient(135deg, #8A2387 0%, #E94057 100%)"},
        {"name": "App 13", "url": "/q13/", "icon": "music_note", "color": "linear-gradient(135deg, #0575E6 0%, #021B79 100%)"},
        {"name": "App 14", "url": "/q14/", "icon": "movie", "color": "linear-gradient(135deg, #1D976C 0%, #93F9B9 100%)"},
        {"name": "App 15", "url": "/q15/", "icon": "sports_esports", "color": "linear-gradient(135deg, #EB3349 0%, #F45C43 100%)"},
        {"name": "App 19", "url": "/q19/", "icon": "security", "color": "linear-gradient(135deg, #DD5E89 0%, #F7BB97 100%)"},
    ]
    return render(request, 'index.html', {'apps': apps})
