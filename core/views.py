from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import generic

from core.forms import PersonForm
from core.models import Person


class PersonListView(generic.ListView):
    model = Person


# class PersonCreateView(generic.CreateView):
#     model = Person
#     fields = "__all__"
#     success_url = reverse_lazy("core:person-list")


class PersonCreateView(generic.CreateView):
    form_class = PersonForm
    template_name = "core/person_form.html"
    success_url = reverse_lazy("core:person-list")


# def person_create_view(request):
#     context = {}
#     form = PersonForm(request.POST or None)
#
#     if form.is_valid():
#         form.save()
#         # Person.objects.create(**form.cleaned_data)
#         return HttpResponseRedirect(reverse("core:person-list"))
#
#     context["form"] = form
#     return render(request, "core/person_form.html", context=context)

    # if request.method == "GET":
    #     context = {
    #         "form": PersonForm(),
    #     }
    #     return render(request, "core/person_form.html", context=context)
    #
    # elif request.method == "POST":
    #     form = PersonForm(request.POST)
    #
    #     if form.is_valid():
    #         Person.objects.create(**form.cleaned_data)
    #         return HttpResponseRedirect(reverse("core:person-list"))
    #
    #     context = {
    #         "form": form
    #     }
    #     return render(request, "core/person_form.html", context=context)


# def person_create_view(request):
#     if request.method == "GET":
#         return render(request, "core/person_form.html")
#
#     elif request.method == "POST":
#         full_name = request.POST["full_name"]
#         birth_year = request.POST["birth_year"]
#
#         if full_name and birth_year:
#             Person.objects.create(full_name=full_name, birth_year=birth_year)
#             return HttpResponseRedirect(reverse("core:person-list"))
#         else:
#             context = {
#                 "error": "Please, provide all information!"
#             }
#             return render(request, "core/person_form.html", context=context)
