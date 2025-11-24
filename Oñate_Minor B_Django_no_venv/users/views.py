from django.shortcuts import render
from rest_framework import generics, permissions
from .models import UserAccount, UserSignup, Application, Donation, DonationMethod, Trial
from .serializers import (
    UserAccountSerializer,
    UserSignupSerializer,
    ApplicationSerializer,
    DonationSerializer,
    DonationMethodSerializer,
    TrialSerializer,
)


class UserAccountListCreateView(generics.ListCreateAPIView):
    queryset = UserAccount.objects.all()
    serializer_class = UserAccountSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserAccountDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserAccount.objects.all()
    serializer_class = UserAccountSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserSignupListCreateView(generics.ListCreateAPIView):
    queryset = UserSignup.objects.all()
    serializer_class = UserSignupSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserSignupDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserSignup.objects.all()
    serializer_class = UserSignupSerializer
    permission_classes = [permissions.IsAuthenticated]


class ApplicationListCreateView(generics.ListCreateAPIView):
    queryset = Application.objects.all().order_by('-submitted_at')
    serializer_class = ApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]


class ApplicationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Application.objects.all().order_by('-submitted_at')
    serializer_class = ApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]


class DonationListCreateView(generics.ListCreateAPIView):
    queryset = Donation.objects.all().order_by('-timestamp')
    serializer_class = DonationSerializer
    permission_classes = [permissions.IsAuthenticated]


class DonationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Donation.objects.all().order_by('-timestamp')
    serializer_class = DonationSerializer
    permission_classes = [permissions.IsAuthenticated]


class DonationMethodListCreateView(generics.ListCreateAPIView):
    queryset = DonationMethod.objects.all()
    serializer_class = DonationMethodSerializer
    permission_classes = [permissions.IsAuthenticated]


class DonationMethodDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DonationMethod.objects.all()
    serializer_class = DonationMethodSerializer
    permission_classes = [permissions.IsAuthenticated]


class TrialListCreateView(generics.ListCreateAPIView):
    queryset = Trial.objects.all()
    serializer_class = TrialSerializer
    permission_classes = [permissions.IsAuthenticated]


class TrialDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Trial.objects.all()
    serializer_class = TrialSerializer
    permission_classes = [permissions.IsAuthenticated]