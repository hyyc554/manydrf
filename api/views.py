from django.shortcuts import render
from rest_framework import serializers
from api.models import Membership, Member, Group
from rest_framework.views import APIView
from rest_framework.response import Response
from api import models
from rest_framework.viewsets import GenericViewSet, ViewSetMixin

# Create your views here.

class MembershipSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField(source='group.id')
    name = serializers.ReadOnlyField(source='group.name')

    class Meta:
        model = Membership

        fields = ('id', 'name', 'join_date',)

class MemberSerializer(serializers.ModelSerializer):
    groups = MembershipSerializer(source='membership_set', many=True)
    class Meta:
        model = Member


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group


class MemberShipView(ViewSetMixin,APIView):
    def list(self, request, *args, **kwargs):
        """
        课程列表接口
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        ret = {'code': 1000, 'data': None}

        queryset = models.Membership.objects.all()

        ser = MembershipSerializer(instance=queryset, many=True)
        print(ser.data)
        ret['data'] = ser.data


        return Response(ret)
