from django.urls import path
from . import views


# Hier werden die URLs angelegt, die für die jeweiligen Seiten definiert werden
# Jeder URL wird auch eine entsprechende View zugewiesen
urlpatterns = [
    path('', views.shop, name="shop"),
    path('warenkorb/', views.warenkorb, name="warenkorb"),
    path('kasse/', views.kasse, name="kasse"),
]

