from django.urls import path
from apps.settings.views import IndexView

urlpatterns = [
    path("", IndexView.as_view(), name='index'),
]