from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
def home14(request):
    return render(request, "index14.html")


def ajax_endpoint(request):
    if request.method == "POST":
        name = request.POST.get("name", "Guest")
        message = f"Hello, {name}! This response came from AJAX without a page reload."
        return JsonResponse({"success": True, "message": message})

    return JsonResponse({"success": False, "error": "Use POST to submit data."}, status=400)
  