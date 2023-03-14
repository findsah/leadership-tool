from django.contrib import admin

from api.models import Question,Plan,UserProfile,UserSegment,Membership,UserAnswer,Subscription,LeadershipType
admin.site.register(Question)
# admin.site.register(Answer)
admin.site.register(Plan)
admin.site.register(UserProfile)
admin.site.register(UserSegment)
admin.site.register(Membership)
admin.site.register(UserAnswer)
admin.site.register(Subscription)
admin.site.register(LeadershipType)

