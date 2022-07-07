from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import generic

from catalog.forms import AuthorCreationForm, BookForm, BookSearchForm
from catalog.models import Book, Author, LiteraryFormat


# def hello_world(request, unique_number):
#     print(request.method)
#     print(request.GET)
#     now = datetime.datetime.now()
#     return HttpResponse(
#         "<html>"
#         "<h1>Hello, world!</h1>"
#         f"<h2>Current moment: {now}</h2>"
#         f"<h2>Current moment: {unique_number}</h2>"
#         "</html>"
#     )


@login_required
def index(request):
    num_books = Book.objects.count()
    num_authors = Author.objects.count()
    num_literary_formats = LiteraryFormat.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_books": num_books,
        "num_authors": num_authors,
        "num_literary_formats": num_literary_formats,
        "num_visits": num_visits + 1
    }

    return render(request, "catalog/index.html", context=context)


class LiteraryFormatListView(LoginRequiredMixin, generic.ListView):
    model = LiteraryFormat
    template_name = "catalog/literary_format_list.html"
    context_object_name = "literary_format_list"


# def literary_format_list_view(request):
#     literary_format_list = LiteraryFormat.objects.all()
#
#     context = {
#         "literary_format_list": literary_format_list,
#     }
#
#     return render(
#         request, "catalog/literary_format_list.html", context=context
#     )


class BookListView(LoginRequiredMixin, generic.ListView):
    model = Book
    queryset = Book.objects.all().select_related("format")
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)

        title = self.request.GET.get("title", "")

        context["search_form"] = BookSearchForm(initial={
            "title": title
        })

        return context

    def get_queryset(self):
        # title = self.request.GET.get("title")
        form = BookSearchForm(self.request.GET)

        # if title:
        #     return self.queryset.filter(title__icontains=title)

        if form.is_valid():
            return self.queryset.filter(
                title__icontains=form.cleaned_data["title"]
            )

        return self.queryset


class BookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Book


class BookCreateView(LoginRequiredMixin, generic.CreateView):
    model = Book
    form_class = BookForm


class BookUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Book
    form_class = BookForm


# def book_detail_view(request, pk):
#     try:
#         book = Book.objects.get(id=pk)
#     except Book.DoesNotExist:
#         raise Http404("Book does not exist")
#
#     context = {
#         "book": book,
#     }
#
#     return render(request, "catalog/book_detail.html", context=context)


def test_session_view(request):
    request.session["book"] = "Test session book"
    return render(request, "catalog/test-sessions.html")


class LiteraryFormatCreateView(LoginRequiredMixin, generic.CreateView):
    model = LiteraryFormat
    fields = "__all__"
    success_url = reverse_lazy("catalog:literary_format_list")
    template_name = "catalog/literary_format_form.html"


class LiteraryFormatUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = LiteraryFormat
    fields = "__all__"
    success_url = reverse_lazy("catalog:literary_format_list")
    template_name = "catalog/literary_format_form.html"


class LiteraryFormatDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = LiteraryFormat
    success_url = reverse_lazy("catalog:literary_format_list")
    template_name = "catalog/literary_format_confirm_delete.html"


class AuthorListView(LoginRequiredMixin, generic.ListView):
    model = Author
    paginate_by = 2


class AuthorDetailView(LoginRequiredMixin, generic.DetailView):
    model = Author


class AuthorCreateView(LoginRequiredMixin, generic.CreateView):
    model = Author
    form_class = AuthorCreationForm

    def get_success_url(self):
        return reverse("catalog:author-detail", kwargs={'pk': self.object.pk})
