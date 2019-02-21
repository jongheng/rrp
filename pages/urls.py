# from django.urls import url
# from django.conf.urls import url
from django.contrib import admin
# from django.views.generic import TemplateView
from django.urls import path
from . import views

# urlpatterns = [
# url(r'^admin/', admin.site.urls),    
# url(r'^$', views.home, name='home'),
# url(r'^$',views.about, name='about'),
# url(r'^$', views.contact, name='contact'),
# url(r'^$',views.index, name='index'),
# url(r'^$',views.left_sidebar, name='left-sidebar'),
# url(r'^$',views.right_sidebar, name='right-sidebar'),
# url(r'^$',views.no_sidebar, name='no-sidebar'),
# ]

urlpatterns = [
path(r'^admin/', admin.site.urls),    
path('', views.home, name='home'),
path('',views.about, name='about'),
path('', views.contact, name='contact'),
path('',views.index, name='index'),
path('',views.left_sidebar, name='left-sidebar'),
path('',views.right_sidebar, name='right-sidebar'),
path('',views.no_sidebar, name='no-sidebar'),
]

# urlpatterns = [
# url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
# url(r'^about',TemplateView.as_view(template_name='about.html'), name='about'),
# url(r'^contact', TemplateView.as_view(template_name='contact.html'), name='contact'),
# url(r'^index',TemplateView.as_view(template_name='index.html'), name='index'),
# url(r'^left_sidebar',TemplateView.as_view(template_name='left-sidebar.html'), name='left-sidebar'),
# url(r'^right_sidebar',TemplateView.as_view(template_name='right-sidebar.html'), name='right-sidebar'),
# url(r'^no_sidebar',TemplateView.as_view(template_name='no-sidebar.html'), name='no-sidebar'),
# ]