from django.conf.urls import url
from . import views

app_name = 'foodservise'
# /foodservise
urlpatterns = [
	url(r'^home$', views.homepage),
	url(r'^$', views.get_food_service.as_view()),
]