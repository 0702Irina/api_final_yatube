from rest_framework import routers
from django.views.generic import TemplateView
from django.urls import include, path
from api.views import CommentViewSet, GroupViewSet, PostViewSet

router_v1 = routers.DefaultRouter()
router_v1.register('posts',
                   PostViewSet,
                   basename='posts')
router_v1.register('posts/(?P<post_id>\\d+)/comments',
                   CommentViewSet,
                   basename='comments')
router_v1.register('groups',
                   GroupViewSet,
                   basename='groups')


urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
