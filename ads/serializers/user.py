from datetime import date

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from ads.models import User, Location


def check_birthdate(value: date):
    if date.today().year - value.year < 9:
        raise serializers.ValidationError('Birth_day must be oldest 9 year when created')


def check_domain(value):
    if 'rambler.ru' in value:
        raise serializers.ValidationError('Registration with rambler.ru is forbidden')


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class UserListSerializer(serializers.ModelSerializer):
    location = serializers.SlugRelatedField(
        required=False,
        many=True,
        queryset=Location.objects.all(),
        slug_field='name'
    )

    class Meta:
        model = User
        exclude = ['password']


class UserCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    location = serializers.SlugRelatedField(
        required=False,
        many=True,
        queryset=Location.objects.all(),
        slug_field='name'
    )
    birth_date = serializers.DateField(validators=[check_birthdate])
    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all()), check_domain])

    def is_valid(self, raise_exception=False):
        self._location = self.initial_data.pop("location")
        super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data["password"])

        for loc in self._location:
            obj, _ = Location.objects.get_or_create(name=loc)
            user.location.add(obj)

        user.save()
        return user

    class Meta:
        model = User
        fields = '__all__'


class UserUpdateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    birth_date = serializers.DateField(validators=[check_birthdate])
    location = serializers.SlugRelatedField(
        required=False,
        many=True,
        queryset=Location.objects.all(),
        slug_field='name'
    )
    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all()), check_domain])

    def is_valid(self, raise_exception=False):
        self._location = self.initial_data.pop("location")
        self._password = self.initial_data.pop("password")
        super().is_valid(raise_exception=raise_exception)

    def save(self):
        user = super().save()
        if self._password:
            user.set_password(self._password)

        for loc in self._location:
            obj, _ = Location.objects.get_or_create(name=loc)
            user.location.add(obj)

        user.save()
        return user

    class Meta:
        model = User
        fields = '__all__'


class UserDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id"]
