from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password',
                  'first_name', 'last_name',
                  'middle_name', 'phone_number', 'address']

        read_only_fields = ['username', 'id', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)

        user.set_password(validated_data['password'])
        user.save()

        return user

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance
