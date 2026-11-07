from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('science/', views.science, name='science'),
    path('maths/', views.maths, name='maths'),
    path('english/', views.english, name='english'),
    path('django/', views.django, name='django'),
    path('learn/', views.learning_library, name='learning_library'),
    path('learn/year/<int:year>/', views.year_dashboard, name='year_dashboard'),
    path('learn/year/<int:year>/<slug:subject_slug>/', views.year_subject, name='year_subject'),
    path('solar-system/', views.solar_system, name='solar_system'),
]
