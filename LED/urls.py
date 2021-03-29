from django.urls import path
from LED import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    #path('',views.api_root),
    path('LED/', views.LEDList.as_view(), name='LED-list'),
    path('LED/<int:pk>/', views.LEDDetail.as_view(), name='LED-detail'),
    path('users/',views.UserList.as_view(),name='user-list'),
    path('users/<int:pk>/',views.UserDetail.as_view(),name='user-detail'),
    path('LED/<int:pk>/users/', views.LEDUsers.as_view(),name='LED-users'),
]

urlpatterns = format_suffix_patterns(urlpatterns)