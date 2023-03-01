from django.contrib import admin

from qandA.models import Question,Answer,Plan,UserProfile,UserSegment,Membership,Response,Subscription,LeadershipType
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Plan)
admin.site.register(UserProfile)
admin.site.register(UserSegment)
admin.site.register(Membership)
admin.site.register(Response)
admin.site.register(Subscription)
admin.site.register(LeadershipType)

