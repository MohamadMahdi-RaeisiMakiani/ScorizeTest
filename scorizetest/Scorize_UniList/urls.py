from django.urls import path
from .views import Show_All_Universities, Show_University_Details

urlpatterns = [
    path('allunilist', Show_All_Universities.as_view(), name='main_page'),
    path('allunilist/<int:pk>', Show_University_Details.as_view(),
         name='each_uni_selector'),
]
