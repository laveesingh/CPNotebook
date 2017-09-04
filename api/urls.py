from django.conf.urls import url

from api import views

urlpatterns = [
    url(r'^$', views.post_list),
    url(r'^post_detail/(?P<pk>[0-9]+)/', views.post_detail),
    url(r'^post_list/', views.post_list),
    url(r'^post_create/', views.post_create),
]
