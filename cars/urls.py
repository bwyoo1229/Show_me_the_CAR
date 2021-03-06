from django.urls import path

from . import views as car_views


app_name = "cars"

urlpatterns = [
    path("", car_views.car_list, name="car_list"),
    path("<int:pk>/", car_views.car_detail, name="car_detail"),
]
