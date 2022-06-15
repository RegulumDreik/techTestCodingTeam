from django.urls import include, path

urlpatterns = [
    path('foods/', include('api.v1.foods.urls')),
]
