from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import BusinessCard

@api_view(['GET'])
def get_card(request, username):
    try:
        card = BusinessCard.objects.get(username=username)
        data = {
            'name': card.full_name,
            'phone': card.phone,
            'email': card.email,
            'website': card.website
        }
        return Response(data)
    except BusinessCard.DoesNotExist:
        return Response({"error": "Card not found"}, status=404)