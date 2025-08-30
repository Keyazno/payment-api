from django.urls import path # type: ignore
from .views import initiate_payment, get_payment_status

urlpatterns = [
    path('payments/', initiate_payment, name='initiate_payment'),
    path('payments/<int:payment_id>/', get_payment_status, name='get_payment_status'),
]
