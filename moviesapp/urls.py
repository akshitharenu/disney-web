from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name="index"),
    path('register',views.register,name="register"),
    path('login/',views.login,name='login'),
    path('mov',views.moviepage,name='moviepage'),
    path('home/',views.home,name='home'),
    path('moviedetail/<int:movie_id>/',views.moviedetail,name='moviedetail'),
    path('books/',views.books,name='books'),
    path('bookdetail/<int:book_id>/',views.bookdetail,name='bookdetail'),
    path('api/v1/movies',views.movieapi,name='movieapi'),
    # path('api/movies/<int:movie_id>/',views.singlemovieapi,name='singlemovieapi')
]