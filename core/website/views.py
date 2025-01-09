from django.shortcuts import render
# Index view
def api_index(request):
    return render(request, "website/index.html")
