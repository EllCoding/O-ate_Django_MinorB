from django.contrib import admin
from .models import User, UserAccount, UserSignup, Application, Donation, DonationMethod, Trial

admin.site.register(User)
admin.site.register(UserAccount)
admin.site.register(UserSignup)
admin.site.register(Application)
admin.site.register(Donation)
admin.site.register(DonationMethod)
admin.site.register(Trial)