from django.urls import path
from .views import Show_All_Universities, Show_University_Details, Show_Filtered_Universities

urlpatterns = [
    path('allunilist', Show_All_Universities.as_view(), name='main_page'),
    path('filtereduni', Show_Filtered_Universities.as_view(), name='filtered_page'),
    path('allunilist/<int:pk>', Show_University_Details.as_view(),
         name='each_uni_selector'),
]
