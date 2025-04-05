from django.urls import path
from .views import MeterReadingCreateAPIView, UserBillListAPIView, UserBillDetailAPIView

urlpatterns = [
    path('meter_readings/', MeterReadingCreateAPIView.as_view(), name='add-reading-api'),
    path('bills/', UserBillListAPIView.as_view(), name='user-bills-list-api'),
    path('bill_details/<int:pk>/', UserBillDetailAPIView.as_view(), name='user-bills-detail-api'),
]