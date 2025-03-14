from django.contrib.auth import authenticate
from django.utils.translation import gettext as _
from rest_framework import serializers

from .models import CustomUser


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate_email(self, value):
        """
        Check if the email already exists in the database.
        """
        if not CustomUser.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email does not exist")
        return value

    def validate(self, attrs):
        self._errors = {}
        email = attrs.get("email")
        password = attrs.get("password")

        user = authenticate(email=email, password=password)

        if not user:
            self._errors["email"] = [_("Invalid email or password")]
            self._errors["password"] = [_("Invalid email or password")]
            raise serializers.ValidationError(self._errors)

        attrs["user"] = user
        return attrs


class UserSerializer(serializers.ModelSerializer):
    password_2 = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = [
            "id",
            "email",
            "first_name",
            "last_name",
            "password",
            "password_2",
            "is_active",
            "is_staff",
        ]

    def validate(self, data):
        if data["password"] != data["password_2"]:
            raise serializers.ValidationError("Passwords do not match")

        return data

    def create(self, validated_data):
        email = validated_data["email"]
        first_name = validated_data["first_name"]
        last_name = validated_data["last_name"]
        password = validated_data["password"]

        user = CustomUser(
            email=email,
            first_name=first_name,
            last_name=last_name,
            is_active=False,
        )
        user.set_password(password)
        user.save()

        return user
