from rest_framework import generics
from app.models import Users
from app.serializer import UserActivitySerializer
# Create your views here.


class UserActivity(generics.ListAPIView):
    

    serializer_class = UserActivitySerializer
    def get_queryset(self):
        return Users.objects.filter(is_active=True)

