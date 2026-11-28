from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('science/', views.science, name='science'),
    path('maths/', views.maths, name='maths'),
    path('english/', views.english, name='english'),
    path('django/', views.django, name='django'),
    path('coding/', views.coding, name='coding'),
    path('downtime/', views.downtime, name='downtime'),
    path('dot/', views.dot, name='dot'),
    path('dot/chat/', views.dot_chat, name='dot_chat'),
    path('accounts/signup/', views.signup, name='signup'),
    path('learn/', views.learning_library, name='learning_library'),
    path('progress/', views.progress_dashboard, name='progress'),
    path('shop/', views.shop, name='shop'),
    path('shop/buy/<slug:item_slug>/', views.buy_shop_item, name='buy_shop_item'),
    path('quizzes/', views.quizzes, name='quizzes'),
    path('progress/buy-egg/', views.buy_egg, name='buy_egg'),
    path('progress/hatch/<int:pet_id>/', views.hatch_egg, name='hatch_egg'),
    path('learn/quiz/submit/', views.submit_quiz, name='submit_quiz'),
    path('learn/year/<int:year>/', views.year_dashboard, name='year_dashboard'),
    path('learn/year/<int:year>/<slug:subject_slug>/', views.year_subject, name='year_subject'),
    path('solar-system/', views.solar_system, name='solar_system'),
]
