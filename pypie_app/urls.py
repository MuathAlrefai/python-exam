from django.urls import path
from . import views

urlpatterns = [
    path('pypie', views.pypie),
    path('add_pie', views.add_pie),
    path('edit/<int:ID>', views.render_edit_pie),
    path('update', views.update_pie),
    path('delete/<int:uuid>', views.delete_pie),
    path('pies', views.derby),
    path('show/<int:ID>', views.pie_info),
    path('add_vote/<int:ID>', views.add_vote),
    path('remove_vote/<int:ID>', views.remove_vote),
]