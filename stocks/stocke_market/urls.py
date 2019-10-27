from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('add_stock', views.add_stock, name='add_stock'),
    path('delete/<stock_id>', views.delete, name='delete'),
    # url(r'^delete/(?P<pk>\d+)/$', views.delete, name='delete'),
]
