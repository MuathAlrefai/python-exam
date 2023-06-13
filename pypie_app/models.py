from django.db import models
from login_app.models import User, Validator

class PyPie(models.Model):
    name = models.CharField(max_length=255)
    filling = models.CharField(max_length=255)
    crust = models.CharField(max_length=255)
    votes = models.IntegerField(default=0)
    user = models.ForeignKey(User, related_name='pypies', on_delete=models.CASCADE)
    user_voted = models.ManyToManyField(User, related_name='voted_pies')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = Validator()

def add_pie_model(request):
    user = User.objects.get(id=request.session['userid'])
    pie_name = request.POST['pie_name']
    pie_filling = request.POST['pie_filling']
    pie_crust = request.POST['pie_crust']
    PyPie.objects.create(name = pie_name, filling = pie_filling, crust = pie_crust, user = user)

def update_pie_model(request):
    ID = request.POST['pie_id']
    pie = PyPie.objects.get(id = ID)
    pie_name = request.POST['pie_name']
    pie_filling = request.POST['pie_filling']
    pie_crust = request.POST['pie_crust']

    pie.name = pie_name
    pie.filling = pie_filling
    pie.crust = pie_crust
    pie.save()
    return ID
    
def get_all_pies():
    return PyPie.objects.all()

def get_pie(ID):
    return PyPie.objects.get(id = ID)

def get_user_session(request):
    return User.objects.get(id=request.session['userid'])

# def all_user_pies_model(request):
#     user = User.objects.get(id=request.session['userid'])
#     return user.pypies.all()

def delete_pie_model(request, uuid):
    pie = PyPie.objects.get(id = uuid)
    pie.delete()

def add_vote_model(request, ID):
    pie = PyPie.objects.get(id = ID)
    user = User.objects.get(id=request.session['userid'])
    user.voted_pies.add(pie)
    pie.votes += 1
    pie.save()

def remove_vote_model(request, ID):
    pie = PyPie.objects.get(id = ID)
    user = User.objects.get(id=request.session['userid'])
    user.voted_pies.remove(pie)
    pie.votes -= 1
    pie.save()
