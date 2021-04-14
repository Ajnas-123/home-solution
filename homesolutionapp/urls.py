from django.urls import path
from homesolutionapp import views

urlpatterns = [
	path('',views.display),
	path('about/',views.about),
	path('contact/',views.contact),
	path('error/',views.error),
	path('gallery/',views.gallery),
	path('services/',views.services),
	path('typography/',views.typography),
	path('user_register/',views.user_register),
	path('user_login/',views.user_login),
	path('user_logout/',views.user_logout),
	path('worker_register/',views.worker_register),
	path('worker_login/',views.worker_login),
	path('worker_logout/',views.worker_logout),
	path('complaint_register/',views.complaint_register),
	path('admin_login/',views.admin_login),
	path('admin_view/',views.admin_page),
	path('admin_logout/',views.admin_logout),
	path('show_details/',views.show_details),
	path('img/',views.img),
	path('imgview/',views.imgview),
	path('download/',views.download),









]