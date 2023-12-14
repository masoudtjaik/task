
from django.contrib import admin
from django.urls import path,include
from .views import *
from django.conf import settings
from django.conf.urls.static import static
app_name='task'
urlpatterns = [
    path('',home,name='home'),
    path('login/',login_page2,name='login'),
    path('logout/',logout_page,name='logout'),
    path('detail/<int:id>',detail,name='detail'),
    path('details/<int:id>',detail_submits,name='details'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
