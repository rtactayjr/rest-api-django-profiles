from django.urls import path, include

from rest_framework.routers import DefaultRouter

from . import views


# router = DefaultRouter()
# router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
# router.register('profile', views.UserProfileViewSet)
# router.register('feed', views.UserProfileFeedViewSet)

'''
    This part specifies the view class that will be used to handle the request.
    In Django Rest Framework, views are implemented as Python classes.

    The as_view() method is a method provided by DRF that converts
    the view class into a callable view function that can be used in URL patterns
'''

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),

    # path('login/', views.UserLoginApiView.as_view()),
    #
    # path('', include(router.urls))
]
