from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('api/useraccount', views.UserAccountList.as_view(), name='useraccount_list'),
    path('api/useraccount/<int:pk>', views.UserAccountDetail.as_view(), name='useraccount_detail'),
    path('api/useraccount/login', csrf_exempt(views.check_login), name="check_login"), # api/useraccount/login will be routed to the check_login function for auth
    path('api/useraccount/search', views.user_search, name='user_search'),
    path('api/follow', views.FollowList.as_view(), name='follow_list'),
    path('api/follow/<int:pk>', views.FollowDetail.as_view(), name='follow_detail'),
]