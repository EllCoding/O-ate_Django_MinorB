from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Report, locationReport
from .serializers import ReportSerializer, LocationReportSerializer


class ReportListCreateView(generics.ListCreateAPIView):
    queryset = Report.objects.all().order_by('-timestamp')
    serializer_class = ReportSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(reporter=self.request.user)


class ReportDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Report.objects.all().order_by('-timestamp')
    serializer_class = ReportSerializer
    permission_classes = [permissions.IsAuthenticated]


class LocationReportListCreateView(generics.ListCreateAPIView):
    queryset = locationReport.objects.all()
    serializer_class = LocationReportSerializer
    permission_classes = [permissions.IsAuthenticated]


class LocationReportDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = locationReport.objects.all()
    serializer_class = LocationReportSerializer
    permission_classes = [permissions.IsAuthenticated]