from swagger import views
from django.urls import path


urlpatterns = [
    path('doc', views.DocIndexView.as_view(), name='doc-index'),
]
