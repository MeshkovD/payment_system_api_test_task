from django.urls import path

from cartapp.views import ItemDetail, buy, ItemList

urlpatterns = [
    path('', ItemList.as_view(), name='items'),
    path('buy/<int:pk>/', buy, name="buy"),
    path('item/<int:pk>/', ItemDetail.as_view(), name="item"),
]
