"""
URL configuration for PAMS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pets.views import PetListCreateView, PetDetailView
from forumposts.views import (
    ForumPostListCreateView,
    ForumPostDetailView,
    ForumCommentListCreateView,
    ForumCommentDetailView,
)
from reports.views import (
    ReportListCreateView,
    ReportDetailView,
    LocationReportListCreateView,
    LocationReportDetailView,
)
from tutorials.views import (
    TutorialListCreateView,
    TutorialDetailView,
    TutorialCommentListCreateView,
    TutorialCommentDetailView,
)
from users.views import (
    UserSignupListCreateView,
    UserSignupDetailView,
    UserAccountListCreateView,
    UserAccountDetailView,
    ApplicationListCreateView,
    ApplicationDetailView,
    DonationListCreateView,
    DonationDetailView,
    DonationMethodListCreateView,
    DonationMethodDetailView,
    TrialListCreateView,
    TrialDetailView,
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/pets/', PetListCreateView.as_view(), name='pets-list-create'),
    path('api/forumposts/', ForumPostListCreateView.as_view(), name='forumposts-list-create'),
    path('api/forumcomments/', ForumCommentListCreateView.as_view(), name='forumcomments-list-create'),
    path('api/reports/', ReportListCreateView.as_view(), name='reports-list-create'),
    path('api/locationreports/', LocationReportListCreateView.as_view(), name='locationreports-list-create'),
    path('api/tutorials/', TutorialListCreateView.as_view(), name='tutorials-list-create'),
    path('api/tutorialcomments/', TutorialCommentListCreateView.as_view(), name='tutorialcomments-list-create'),
    path('api/users/signup/', UserSignupListCreateView.as_view(), name='users-signup-list-create'),
    path('api/users/account/', UserAccountListCreateView.as_view(), name='users-account-list-create'),
    path('api/applications/', ApplicationListCreateView.as_view(), name='applications-list-create'),
    path('api/donations/', DonationListCreateView.as_view(), name='donations-list-create'),
    path('api/donationmethods/', DonationMethodListCreateView.as_view(), name='donationmethods-list-create'),
    path('api/trials/', TrialListCreateView.as_view(), name='trials-list-create'),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
