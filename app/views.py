from rest_framework import generics, response
from app.models import Users
from app.serializer import UserActivitySerializer

# Create your views here.


class UserActivity(generics.GenericAPIView):

    serializer_class = UserActivitySerializer

    def get_queryset(self):
        return Users.objects.filter(is_active=True)

    def get(self, request):
        query_set = self.get_queryset()
        data = self.serializer_class(query_set, many=True).data
        response_data = {"ok": True, "members": data}
        return response.Response(response_data)

