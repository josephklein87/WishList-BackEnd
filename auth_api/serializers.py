from rest_framework import serializers
from .models import UserAccount
from .models import Follow

### ALLOWS YOU TO CREATE AND CHECK PASSWORDS
from django.contrib.auth.hashers import make_password, check_password



class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ('id', 'email', 'password', 'username', 'birthday')

    ### THIS HASHES A NEW USERS PASSWORD WHEN THEY CREATE AN ACCOUNT
    def create(self, validated_data):
        user = UserAccount.objects.create(
        email=validated_data['email'],
        password = make_password(validated_data['password']),
        username = validated_data['username'],
        birthday = validated_data['birthday']
        )
        user.save()
        return user

    ### THIS MAKES SURE THEIR UPDATED PASSWORDS ARE ALSO HASHED
    def update(self,instance, validated_data):
        user = UserAccount.objects.get(email=validated_data["email"])
        user.password = make_password(validated_data["password"])
        user.save()
        return user

class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = ('id', 'user', 'following')


class UserAccountFollowing(serializers.ModelSerializer):

    follower_list = serializers.SerializerMethodField()
    following_list = serializers.SerializerMethodField()

    class Meta:
        model = UserAccount
        fields = ('id', 'email', 'username', 'follower_list', 'following_list')

    def get_follower_list(self, obj):
        obj.follower_list = []
        for item in obj.followers.all():
            obj.follower_list.append(item.user.username)
        return obj.follower_list

    def get_following_list(self, obj):
        obj.following_list = []
        for item in obj.following.all():
            obj.following_list.append(item.following.username)
        return obj.following_list


    


        