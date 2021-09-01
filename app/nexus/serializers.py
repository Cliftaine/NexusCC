from rest_framework import serializers
from .models import User, Team, Accounts, Movements

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields = ['id', 'name', 'email', 'password', 'username']
        #extra_kwargs={
        #    'password': {'write_only':  True}
        #}

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['name']

class AccountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accounts
        fields = ['accountName', 'clientName', 'iCOperation', 'team']

class MovementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movements
        fields = ['start', 'end', 'team']


