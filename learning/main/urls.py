from django.urls import path
from main import views

from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('typing/' , views.TypingList.as_view()),
    path('typing/<int:pk>/' ,  views.TypingDetail.as_view())
]
