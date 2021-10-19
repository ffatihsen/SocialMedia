from django.urls import path
from .views import my_profile_view,invities_recived_view,profile_list_view,invite_profiles_list_view,ProfileListView,\
    send_invatation,remove_from_friends,accept_invatation,reject_invatation,ProfileDetailView

app_name="profiles"

urlpatterns = [
    path('', ProfileListView.as_view(),name="al-profiles-view"),
    path('myprofile/', my_profile_view,name="my-profile-view"),
    path('my-invities/', invities_recived_view,name="my-invities-view"),
    path('to-invite/', invite_profiles_list_view,name="invite-profiles-view"),
    path('send-invite/', send_invatation,name="send-invite-view"),
    path('remove-friend/', remove_from_friends,name="remove-friend-view"),
    path('<slug>/', ProfileDetailView.as_view(),name="profile-detail-view"),
    path('my-invities/acctept/', accept_invatation,name="accept-invite"),
    path('my-invities/reject/', reject_invatation,name="reject-invite"),

]
