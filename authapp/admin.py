from django.contrib import admin
from authapp.models import Contact,Enrollment,Trainer,MembershipPlan,Gellery,Attendance, Otp
# Register your models here.
admin.site.register(Contact)
admin.site.register(Enrollment)
admin.site.register(Trainer)
admin.site.register(MembershipPlan)
admin.site.register(Gellery)
admin.site.register(Attendance)
admin.site.register(Otp)
