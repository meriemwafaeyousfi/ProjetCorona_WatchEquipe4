from rest_framework import routers

from Robots import views

router = routers.DefaultRouter()
router.register(r'facebook', views.pubFacebookView,basename='facebook')
router.register(r'youtube', views.pubYoutubeView, basename='youtube')
router.register(r'web', views.pubSiteWebView, basename='web')


urlpatterns = router.urls