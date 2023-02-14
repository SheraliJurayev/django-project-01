from django.urls import path
from .views import HomeView , AboutPageView , LikePageView  ,FollowPageView

urlpatterns = [
        path('follow/', FollowPageView.as_view(),name='follow'),
        path('like/' , LikePageView.as_view() , name='like'),
        path('about/' , AboutPageView.as_view(), name='about'),
        path('', HomeView.as_view(), name='home'),
        
]