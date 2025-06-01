from .views import index_page,maqsad
from django.urls import path

urlpatterns = [
    path('', index_page, name='home'),
    path('content/<int:content_id>/', maqsad, name='maqsad'),
]