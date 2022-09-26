from django.urls import path
from erp.views import firstview

urlpatterns = [
    path('index/', firstview)
]
