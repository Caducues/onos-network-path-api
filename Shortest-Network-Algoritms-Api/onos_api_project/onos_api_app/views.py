from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PathRequestSerializer
from .utils import get_links, build_graph_from_links
from .dijkstra import dijkstra

class ShortestPathView(APIView):
    def post(self, request):
        serializer = PathRequestSerializer(data=request.data)
        if serializer.is_valid():
            src = serializer.validated_data['src']
            dst = serializer.validated_data['dst']

            try:
                links = get_links()
                graph = build_graph_from_links(links)
                path = dijkstra(graph, src, dst)
                if path:
                    return Response({'path': path})
                else:
                    return Response({'error': 'Path not found'}, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
