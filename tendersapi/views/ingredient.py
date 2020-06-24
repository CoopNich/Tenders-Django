from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from tendersapi.models import Ingredient, Cocktail, Bartender

class IngredientSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Ingredient
        url = serializers.HyperlinkedIdentityField(
            view_name='ingredient',
            lookup_field='id'
        )
        fields = ('id', 'url', 'ingredient', 'measurement', 'cocktail_id', 'cocktail')
        # depth = 1

class Ingredients(ViewSet):
    
    def list(self, request):

        ingredients = Ingredient.objects.all()
        cocktail_id = self.request.query_params.get('cocktail_id', None)

        if cocktail_id is not None:

            ingredients = ingredients.filter(cocktail_id=cocktail_id)
            serializer = IngredientSerializer(ingredients, many=True, context={'request': request})
            return Response(serializer.data)

    def retrieve(self, request, pk=None):

        try:
            ingredient = Ingredient.objects.get(pk=pk)
            serializer = IngredientSerializer(ingredient, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def create(self, request):

        new_ingredient = Ingredient()
        new_ingredient.ingredient = request.data["ingredient"]
        new_ingredient.measurement = request.data["measurement"]
        new_ingredient.cocktail_id = request.data["cocktail_id"]

        new_ingredient.save()

        serializer = IngredientSerializer(new_ingredient, context={'request': request})

        return Response(serializer.data)

    def update(self, request, pk=None):

        ingredient = Ingredient.objects.get(pk=pk)
        ingredient.measurement = request.data["measurement"]
        ingredient.ingredient = request.data["ingredient"] 
        ingredient.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):

        try:
            ingredient = Ingredient.objects.get(pk=pk)
            ingredient.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Ingredient.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
            
        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)