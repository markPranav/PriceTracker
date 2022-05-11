
from rest_framework.exceptions import  ValidationError
from rest_framework import status

from durin.views import LoginView as DurinLoginView
from durin.models import Client as APIClient
class LoginView(DurinLoginView):

    @staticmethod
    def get_client_obj(request):
        # get the client's name from a request header
        client_name = request.META.get("HTTP_CLIENTNAME", None)
        if not client_name:
            raise ValidationError("No client specified.", status.HTTP_400_BAD_REQUEST)

        client = APIClient.objects.get_or_create(name=client_name)
        return client[0]