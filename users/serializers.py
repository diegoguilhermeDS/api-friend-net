from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "is_superuser",
            "first_name",
            "last_name",
            "password",
        ]

        read_only_fields = ["is_superuser"]
        extra_kwargs = {"password": {"write_only": True}}

        username = serializers.CharField(
            validators=[
                UniqueValidator(
                    queryset=User.objects.all(),
                    message="A user with that username already exists",
                )
            ]
        )
        email = serializers.EmailField(
            validators=[
                UniqueValidator(
                    queryset=User.objects.all(),
                    message="A user with that email already exists",
                )
            ]
        )

    def create(self, validated_data):
        new_user = User.objects.create(**validated_data)
        new_user.set_password(validated_data["password"])
        new_user.save()
        return new_user

    def update(self, instance: User, validated_data: dict):
        for key, value in validated_data.items():
            if key == "password":
                instance.set_password(value)
            else:
                setattr(instance, key, value)

        instance.save()

        return instance
