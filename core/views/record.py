from django.shortcuts import render
from django.db.models import *
from django.db import transaction
from core.serializers import *
from core.models import *
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.generics import CreateAPIView, DestroyAPIView, UpdateAPIView
from rest_framework import permissions
from rest_framework import generics
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from django.core import serializers
from django.utils.html import strip_tags
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters
from datetime import datetime
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.dateparse import parse_date
import string
import random
import json

class UpdateRecordView(generics.CreateAPIView):
    
    # Actualizar el modelo Record basado en los datos recibidos
    def post(self, request, *args, **kwargs):
        
        # Obtener los datos enviados en la solicitud POST
        level = request.data["level"]
        result = request.data["result"]
                
        # Actualizar el modelo Record basado en los datos recibidos
        record = Record.objects.get(user=request.user)  # Asume que el usuario ya tiene un registro
        if level == 1:
            if result == 1:
                record.n1w += 1
            else:
                record.n1l += 1
        elif level == 2:
            if result == 1:
                record.n2w += 1
            else:
                record.n2l += 1
        elif level == 3:
            if result == 1:
                record.n3w += 1
            else:
                record.n3l += 1

        # Guardar los cambios en el modelo
        record.save()
        
        return Response({
            "success for id user: ":record.user.pk,
            "level": level,
            "result": result
            }, 200)
    
    # Obtener el modelo Record basado en el usuario
    def get(self, request, *args, **kwargs):
        record = Record.objects.get(user=request.user)
        serializer = RecordSerializer(record)
        return Response(serializer.data, status=200)