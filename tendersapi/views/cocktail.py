from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from tendersapi.models import Bartender
from tendersapi.models import Cocktail as CocktailModel
from datetime import datetime

class CocktailSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = CocktailModel
        url = serializers.HyperlinkedIdentityField(
            view_name='cocktail',
            lookup_field='id'
        )
        fields = ('id', 'name', 'bartender_id', 'bartender', 'date_added', 'glass', 'instructions', 'is_edited', 'is_new', 'image_url')
        # depth = 1

class Cocktail(ViewSet):

    def retrieve(self, request, pk=None):

        try:
            cocktail = CocktailModel.objects.get(pk=pk)
            serializer = CocktailSerializer(cocktail, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):

        user = self.request.query_params.get('user', None)
        if user is not None:
            bartender = Bartender.objects.get(user=request.auth.user)
            cocktail = CocktailModel.objects.filter(bartender=bartender)
        else:
            cocktail = CocktailModel.objects.all()

        serializer = CocktailSerializer(
            cocktail, many=True, context={'request': request})
        
        return Response(serializer.data)

    def create(self, request):

        bartender = Bartender.objects.get(user=request.auth.user)

        new_cocktail = CocktailModel()
        new_cocktail.bartender = bartender
        new_cocktail.bartender_id = bartender.id
        new_cocktail.date_added = datetime.now()
        new_cocktail.name = request.data["name"]
        new_cocktail.external_id = request.data["external_id"]
        new_cocktail.glass = request.data["glass"] 
        new_cocktail.instructions = request.data["instructions"]
        new_cocktail.is_edited = request.data["is_edited"]
        new_cocktail.is_new = request.data["is_new"]
        new_cocktail.image_url = request.data["image_url"]

        new_cocktail.save()

        serializer = CocktailSerializer(
            new_cocktail, context={'request': request}
        )

        return Response(serializer.data)
    
    def update(self, request, pk=None):

        cocktail = CocktailModel.objects.get(pk=pk)
        cocktail.instructions = request.data["instructions"]
        cocktail.name = request.data["name"] 
        cocktail.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):

        try:
            cocktail = CocktailModel.objects.get(pk=pk)
            cocktail.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except CocktailModel.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
            
        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
