from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from tendersapi.models import Bartender as BartenderModel
from django.contrib.auth.models import User

class BartenderSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for bartenders
    Arguments:
        serializers
    """
    class Meta:
        model = BartenderModel
        url = serializers.HyperlinkedIdentityField(
            view_name='bartender',
            lookup_field='id'
        )
        fields = ('id', 'url', 'image_url', 'user', 'user_id')
        depth = 1


class Bartenders(ViewSet):
    
    def list(self, request):
        """Handle GET requests to bartenders resource
        
        Returns:
            Response -- JSON serialized list of bartenders
        """

        bartenders = BartenderModel.objects.all()

        serializer = BartenderSerializer(bartenders, many=True, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):

        try:
            bartender = BartenderModel.objects.get(pk=pk)
            serializer = BartenderSerializer(bartender, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)