from rest_framework.response import Response # pyright: ignore[reportMissingImports]
from rest_framework.decorators import api_view # pyright: ignore[reportMissingImports]
from rest_framework import status # pyright: ignore[reportMissingImports]
from .models import Payment
from .serializers import PaymentSerializer

@api_view(['POST'])
def initiate_payment(request):
    serializer = PaymentSerializer(data=request.data)
    if serializer.is_valid():
        payment = serializer.save(status='pending')
        return Response({"payment_id": payment.id,"status": "pending"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_payment_status(request, payment_id):
    try:
        payment = Payment.objects.get(id=payment_id)
        serializer = PaymentSerializer(payment)
        return Response({"payment":serializer.data,"status": "success","message": "Payment retrieved successfully"}, status=status.HTTP_200_OK)
    except Payment.DoesNotExist:
        return Response({"error": "Payment not found"}, status=status.HTTP_404_NOT_FOUND)