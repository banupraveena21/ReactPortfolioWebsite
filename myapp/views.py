from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import ContactMessage

@api_view(["POST"])
def contact_view(request):
    data = request.data
    ContactMessage.objects.create(
        name=data.get("name"),
        email=data.get("email"),
        message=data.get("message")
    )
    return Response({"success": "Message received!"}, status=200)
