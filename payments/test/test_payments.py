import pytest # type: ignore
from rest_framework.test import APIClient # type: ignore
from payments.models import Payment

client = APIClient()

@pytest.mark.django_db
def test_initiate_payment():
    data = {
        "customer_name": "John Doe",
        "customer_email": "john@gmail.com",
        "status": "pending",
        "amount": "50.00"
    }
    #  endpoint
    response = client.post("/api/v1/payments/", data, format="json")

    assert response.status_code == 201
    assert "payment_id" in response.data
    assert response.data["status"] == "pending"


@pytest.mark.django_db
def test_get_payment_status():
    # Arrange: create a dummy payment
    payment = Payment.objects.create(
        customer_name="Alice",
        customer_email="alice@gmail.com",
        amount="100.00",
        status="completed"
    )

    # Act
    response = client.get(f"/api/v1/payments/{payment.id}/")

    # Assert
    assert response.status_code == 200
    assert response.data["payment"]["customer_name"] == "Alice"
    assert response.data["status"] == "success"
    assert "Payment retrieved successfully" in response.data["message"]
