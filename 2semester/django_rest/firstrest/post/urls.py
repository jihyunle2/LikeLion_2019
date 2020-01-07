
'''
#3주차
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from post import views


urlpatterns=[
    path('post/',views.PostList.as_view()),
    path('post/<int:pk>/',views.PostDetail.as_view()),
]

urlpatterns=format_suffix_patterns(urlpatterns)

'''


#2주차 & 4주차
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from post import views

router = DefaultRouter()
router.register('post',views.PostViewSet)

urlpatterns = [
    path('',include(router.urls)),
]
