from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .serializers import ArticleSerializer

from .negotiation import IgnoreClientContentNegotiation
from rest_framework.response import Response
from rest_framework import status
from rest_framework_xml.parsers import XMLParser


class ArticleList(APIView):
    content_negotiation_class = IgnoreClientContentNegotiation
    parser_classes = [XMLParser]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = ArticleSerializer(data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(status.HTTP_200_OK)
