from django.urls import path
from .views import index, gallery, contact, basic_grid

urlpatterns = [
    path('', index, name="index"),
    path('gallery/', gallery, name="gallery"),
    path('contact/', contact, name="contact"),
    path('basic_grid/', basic_grid, name="basic_grid"),
]
