from base.serializers.CodeSerializers import CodeSerializer
from base.models.Code import Code
from rest_framework import generics

class CodeListAPIView(generics.ListCreateAPIView):
    queryset = Code.objects.all()
    serializer_class = CodeSerializer


class CodeDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Code.objects.all()
    serializer_class = CodeSerializer
