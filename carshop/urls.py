from django.urls import path,include
from .import views

urlpatterns = [

    path('detail/<int:id>/',views.DetailPostView.as_view(), name='detail_car'),
    path('buy/<int:post_id>/', views.buy, name='buy'),

]
