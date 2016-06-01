from django.shortcuts import render


def post_list(request):
    return render(request, 'signup/register.html', {})

# Create your views here.
