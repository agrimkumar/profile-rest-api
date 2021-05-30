from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""
    def get(self, request, format=None):
        """Return a list of APIView features"""
        an_apiview = [
        'Uses HTTP method as function (get, post, path, delete)',
        'Is similar to a tradationsl Django view',
        'Give you the most control over your application logic',
        'Is mapped manually to URLS',
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})
