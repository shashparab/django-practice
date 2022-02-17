from django.shortcuts import render
from django.http import  HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
# Create your views here.

monthly_challenges = {
    "january": "Eat no sweets for the entire month!",
    "february": "Read for at least 15 minutes everyday.",
    "march": "Do one Gymnastic move everyday.",
    "april": "This is for you dada learn to do Python!!!!!!!.",
    "may": "sup mama this is for you Walk for at least 20 minutes everyday.",
    "june": "Walk for at least 20 minutes everyday.",
    "july": "Walk for at least 20 minutes everyday.",
    "august": "Walk for at least 20 minutes everyday.",
    "september": "Walk for at least 20 minutes everyday.",
    "octomber": "Walk for at least 20 minutes everyday.",
    "november": "Walk for at least 20 minutes everyday.",
    "december": None
}
# def january(request):
#     return HttpResponse("Eat no sweets for the entire month!")


def index(request):
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months": months
    })


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month
            })
    except:
        raise Http404()
