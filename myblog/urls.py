from django.urls import path
from .import views

urlpatterns = [
    path('index/',views.index,name="主页"),
    path('index/<str:num>/',views.index,name="主页"),
    path('details/<int:blog_id>',views.details,name="详情页"),
    path('about/', views.about, name="关于"),
    path('leacots/', views.leacots, name="留言"),
    path('album/', views.photos, name="照片"),
]