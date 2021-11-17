from rest_framework import routers
from core.viewsets import ArticleViewSet


router = routers.DefaultRouter()
router.register(r'article', ArticleViewSet)