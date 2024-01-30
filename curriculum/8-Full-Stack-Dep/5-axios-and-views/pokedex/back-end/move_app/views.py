from .models import Move
from .serializers import MoveSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


# Create a view that utilizes APIView to inherit DRF's built in functionality
class All_moves(APIView):
    # establish a get method that will be triggered by GET requests
    def get(self, request):
        # utilize your ModelSerializer to serialize your queryset and return a proper response with DRF's Response
        moves = MoveSerializer(Move.objects.all(), many=True)
        return Response(moves.data)
    
class A_move(APIView):
    def get(self, request, name):
        move = Move.objects.get(name = name.title())
        return Response(MoveSerializer(move).data)
