from django.urls import path
from core.views import PersonListView, PersonCreateView


app_name = "core"

urlpatterns = [
    path("people/", PersonListView.as_view(), name="person-list"),
    path("people/create/", PersonCreateView.as_view(), name="person-create"),
]
