from django.urls import path
from .views import *


urlpatterns = [
    path('',index,name='index'),
    path('upload_img/',upload_img,name='upload_img'),
    path('category/',category,name='category'),
    path('contact/',contact,name='contact'),
    path('login/',login_user,name='login_user'),
    path('myproducts/',myproducts,name='myproducts'),
    path('signup/',signup,name='signup'),
    path('logout_user/',logout_user,name='logout_user'),
    path('cart_product<id>/',cart_product,name='cart_product'),
    path('usercart/',usercart,name='usercart'),
    path('buy_product<id>/<args>/',buy_product,name='buy_product'),
    path('likes<id>',likes,name='likes'),
    path('myproducts/edit<id>/',edit,name='edit'),
    path('delete_product<id>/',delete_product,name='delete_product'),
    path('place_order<id>/',place_order,name='place_order'),
    path('order_history/',order_history,name='order_history'),
    path('remove_from_cart<id>/',remove_from_cart,name='remove_from_cart'),
    # path('sell<id>/',sell,name='sell'),
    path('history_sellers/',history_sellers,name='history_sellers'),

]
