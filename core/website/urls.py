from django.urls import path
from website.views import api_index

app_name = "website"

urlpatterns = [
    # path("", index_view, name="index"),
    path("", api_index, name= "index")
]