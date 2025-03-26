from django.urls import path

from .views import get_note, CustomTokenObtainPairView, CustomTokenRefreshView, logout, is_authenticated, register

urlpatterns = [   
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
    path('note/', get_note),
    path('logout/', logout),
    path('is_authenticated/', is_authenticated),
    path('register/', register)
]