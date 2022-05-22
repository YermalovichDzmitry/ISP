from django.urls import path
from . import views

urlpatterns = [
    path('', views.NewsHome.as_view(), name="news_home"),
    path('create', views.Create.as_view(), name="create"),
    path('<int:pk>', views.NewDetailView.as_view(), name='news-detail'),
    path('<int:pk>/update', views.NewsUpdateView.as_view(), name='news-update'),
    path('<int:pk>/delete', views.NewsDeleteView.as_view(), name='news-delete'),
    path('category/<int:cat_id>/', views.ShowCategory.as_view(), name='category'),
    path('register/', views.RegisterUser.as_view(), name="register"),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.LogoutUser.as_view(), name='logout'),

    path('authors_name/', views.AuthorsName.as_view(), name='authors_name'),
    path('authors_name/<int:authors_id>', views.ShowAuthors.as_view(), name='authors_detail'),
]
