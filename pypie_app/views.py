from django.shortcuts import render, redirect
from . import models
from django.contrib import messages

def pypie(request):
    context = {
        "user": models.get_user_session(request),
        "pies": models.get_all_pies(),
    }
    return render(request, 'pypie.html', context)

def add_pie(request):
    errors = models.PyPie.objects.pie_validator(request.POST)
    if len(errors) > 0:
        for k, v in errors.items():
            messages.error(request, v)
        return redirect('/pypie')
    else:
        models.add_pie_model(request)
        return redirect('/pypie')

def render_edit_pie(request, ID):
    context = {
        "user": models.get_user_session(request),
        "pies": models.get_all_pies(),
        "pie": models.get_pie(ID)
    }
    return render(request, 'edit_pie.html', context)

def update_pie(request):
    ID = models.update_pie_model(request)
    return redirect(f'/edit/{ID}')

def delete_pie(request, uuid):
    models.delete_pie_model(request, uuid)
    return redirect('/pypie')

def derby(request):
    context = {
        "user": models.get_user_session(request),
        "pies": models.get_all_pies().order_by("-votes"),
    }
    return render(request, 'pie_derby.html', context)

def pie_info(request, ID):
    print()
    context = {
        "user": models.get_user_session(request),
        "pies": models.get_all_pies(),
        "pie": models.get_pie(ID),
    }
    return render(request, 'pie_info.html', context)

def add_vote(request, ID):
    models.add_vote_model(request, ID)
    return redirect('/pies')

def remove_vote(request, ID):
    models.remove_vote_model(request, ID)
    return redirect('/pies')