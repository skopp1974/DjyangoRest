from rest_framework import generics
from .models import Rig
from .serializers import RigSerializer



class RigList(generics.ListCreateAPIView):
    queryset = Rig.objects.all()
    serializer_class = RigSerializer

    # def perform_create(self, serializer):
    #     print("==>perform_create")
    #     print(serializer.data)


class RigDetail(generics.RetrieveDestroyAPIView):
    queryset = Rig.objects.all()
    serializer_class = RigSerializer
