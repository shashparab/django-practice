from django.shortcuts import render

# Create your views here.

posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
    }
]
def starting_page(request):
    return render(request, "blog/index.html")


def posts(request):
    return render(request,"blog/all-posts.html")


def post_detail(request, slug):
    return render(request, "blog/post-detail.html")
