from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Post
from .forms import PostForm


# Create your views here.
def post_create(request):
    form = PostForm(request.POST)
    # forms of django to the validation
    if form.is_valid():
        instance = form.save(commit=False)
        print(form.cleaned_data())
        instance.save()
    # to catch data
    # if request.method == 'POST':
    #     title= request.POST.get("content")
    #     print(request.POST.get("title"))

    context = {
        "form": form,

    }
    # return HttpResponse("<h1>Create</h1>")
    return render(request, "post_form.html", context)


def post_detail(request, id):  # retrieve
    instance = get_object_or_404(Post, id=id)
    context = {
        "title": instance.title,
        "instance": instance
    }
    return render(request, "post_detail.html", context)


def post_list(request):
    queryset = Post.objects.all()
    # return HttpResponse("<h1>List</h1>")
    context = {
        "object_list": queryset,
        "title": "My User List"
    }
    # if request.user.is_authenticated():
    #     context = {
    #         "title": "My User List"
    #     }
    # else:
    #     context = {
    #         "title": "List"
    #     }
    return render(request, "index.html", context)


def post_update(request):
    return HttpResponse("<h1>Update</h1>")


def post_delete(request):
    return HttpResponse("<h1>Delete</h1>")
