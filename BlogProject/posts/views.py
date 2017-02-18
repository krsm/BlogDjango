from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Post
from .forms import PostForm


# Create your views here.
def post_create(request):
    form = PostForm(request.POST)
    # forms of django do the validation
    if form.is_valid():
        instance = form.save(commit=False)
        # print(form.cleaned_data())
        instance.save()
        # to redirect to another page, after save
        # message success
        messages.success(request, "Post was created!")
        return HttpResponseRedirect(instance.get_absolute_url())
    # else:  # in case of form is not valid
    #     messages.success(request, "Post was not created!")
    # to catch data
    # if request.method == 'POST':
    #     title= request.POST.get("content")
    #     print(request.POST.get("title"))

    context = {
        "form": form,
    }
    # return HttpResponse("<h1>Create</h1>")
    return render(request, "post_form.html", context)


def post_detail(request, id=None):  # retrieve
    instance = get_object_or_404(Post, id=id)
    context = {
        "title": instance.title,
        "instance": instance
    }
    return render(request, "post_detail.html", context)


def post_list(request):
    # queryset = Post.objects.all().order_by("-timestamp") class Meta replace this
    queryset_list = Post.objects.all()
    # code related to pagination
    paginator = Paginator(queryset_list, 10)  # Show 25 contacts per page
    page_request_var = "page"
    page = request.GET.get(page_request_var)

    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)
    # end of code related to pagination

    context = {
        "object_list": queryset,
        "title": "List",
        "page_request_var": page_request_var
    }
    # if request.user.is_authenticated():
    #     context = {
    #         "title": "My User List"
    #     }
    # else:
    #     context = {
    #         "title": "List"
    #     }
    return render(request, "post_list.html", context)


def post_update(request, id=None):
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance=instance)
    # forms of django to the validation
    if form.is_valid():
        instance = form.save(commit=False)
        # print(form.cleaned_data())
        instance.save()
        # to redirect to another page, after save
        # message success
        messages.success(request, "Post was updated!")
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "title": instance.title,
        "instance": instance,
        "form": form,

    }

    return render(request, "post_form.html", context)


def post_delete(request, id=None):
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    # message success
    messages.success(request, "Post was deleted!")
    return redirect("posts:list")
