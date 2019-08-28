from django.urls import path,include
from userss import views as api_views
from userss.views import UserCreateAPIView,login,logout,item_list,index,indexx,indexxx,indexl


urlpatterns = [
    path('',index,name='index'),
    path('indexx',indexx,name='indexx'),
    path('indexxx',indexxx,name='indexxx'),
    path('indexl',indexl,name='indexl'),
    path('api/signup',UserCreateAPIView.as_view()),
    path('api/login', login,name='login'),
    path('api/logout',logout),
    path('api/item',item_list),
   

]
