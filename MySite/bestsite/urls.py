from django.urls import path
from django.conf.urls import url
from . import views
app_name = 'bestsite'


urlpatterns = [
    url(r'^$', views.index, name="index"),
    # url(r'^detail/post-(?P<pk>\d+)$', views.single, name="single"),
    # url(r'^detail/(?P<pk>\d+)/$', views.single, name="single"),
    path('/detail/<int:pk>/', views.single, name='single'),
    path('/comment/<int:pk>/', views.submit_comment, name='submit_comment'),
    path('/like/<int:pk>/', views.submit_comment, name='submit_like')
]
