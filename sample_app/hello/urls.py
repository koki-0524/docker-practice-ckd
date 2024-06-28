from django.urls import path
from hello import views as hello
from django.views.generic import RedirectView

urlpatterns = [
    path("", hello.index, name='index'),
    path("ja/", hello.index_ja),
    path("login/", hello.login_View, name='login'),
    path("logout/", hello.logout, name='logout'),
    path("book_r/", hello.book_register, name='book_r'),
    
    path("redirect/", hello.index_redirect),
    path("redirect2/", hello.RedirectView.as_view(url="/hello/ja")),
    
]
 # path("hello/<int;user_id>",hello.index),# hello/