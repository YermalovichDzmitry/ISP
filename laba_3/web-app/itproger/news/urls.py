from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_home, name="news_home"),
    path('create', views.create, name="create"),
    path('<int:pk>', views.NewDetailView.as_view(), name='news-detail'),
    path('<int:pk>/update', views.NewsUpdateView.as_view(), name='news-update'),
    path('<int:pk>/delete', views.NewsDeleteView.as_view(), name='news-delete'),
    path('category/<int:cat_id>/', views.show_category, name='category'),
    path('register/', views.RegisterUser.as_view(), name="register"),
    path('login/', views.login, name='login'),
]
