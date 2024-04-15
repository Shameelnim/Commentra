from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
	
	path('',views.home,name="home"),
    path('add',views.add,name="add"),
    path('update/<str:pk>',views.update,name="update"),
    path('login',views.login,name="login"),
    path('register',views.register,name="register"),
    path('delete/<str:pk>',views.delete,name="delete"),
    path('logout',views.logout,name="logout"),
    path('view/<str:comment>',views.show_the_post,name="view"),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
