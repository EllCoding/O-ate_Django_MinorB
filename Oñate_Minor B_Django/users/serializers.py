from rest_framework import serializers
from .models import User, UserAccount, UserSignup, Application, Donation, DonationMethod, Trial

class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ['id', 'user', 'address', 'city', 'state', 'zip_code', 'country']


class UserSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSignup
        fields = ['id', 'user', 'name', 'email', 'password', 'contact_number', 'gender', 'created_at']


class ApplicationSerializer(serializers.ModelSerializer):
    adopter_username = serializers.CharField(source='adopter.username', read_only=True)
    pet_name = serializers.CharField(source='pet.name', read_only=True)

    class Meta:
        model = Application
        fields = ['id', 'adopter', 'adopter_username', 'pet', 'pet_name', 'status', 'submitted_at']


class DonationMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonationMethod
        fields = ['id', 'donation', 'method', 'details']


class DonationSerializer(serializers.ModelSerializer):
    donor_username = serializers.CharField(source='donor.username', read_only=True)
    methods = DonationMethodSerializer(many=True, read_only=True)

    class Meta:
        model = Donation
        fields = ['id', 'donor', 'donor_username', 'amount', 'item_description', 'timestamp', 'methods']


class TrialSerializer(serializers.ModelSerializer):
    adopter_username = serializers.CharField(source='adopter.username', read_only=True)
    pet_name = serializers.CharField(source='pets.name', read_only=True)

    class Meta:
        model = Trial
        fields = ['id', 'pets', 'pet_name', 'adopter', 'adopter_username', 'start_date', 'end_date', 'feedback']