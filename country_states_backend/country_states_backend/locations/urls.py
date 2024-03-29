from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CountryViewSet, StateViewSet, StateListView, LoginView, RegisterView
from knox import views as knox_views

# from .views import test_view
router = DefaultRouter()
router.register(r'countries', CountryViewSet)
router.register(r'states', StateViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('countries/<str:country_code>/states/', StateListView.as_view(), name='country-states'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    # path('test/', test_view, name='test'),
    path('logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
]

