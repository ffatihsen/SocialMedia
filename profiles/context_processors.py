from .models import Profile,Relationship


#Eğer kullanıcı sisteme giriş yapmış ise , sistemdeki kullanıcıyı user a atıyoruz ve kullanıcının avatar dediğimiz değişkeni
#yani foto sunu pşic değişkenine atıyoruz ve geriye dönderiyoruz. Sisteme giriş yapmadı ise de geriye boş değer dönderiyoruz.
def profile_pic(request):
    if request.user.is_authenticated:
        profile_obj=Profile.objects.get(user=request.user)
        pic=profile_obj.avatar
        return {"picture":pic}
    return {}



#Eğer kullanıcı sisteme giriş yapmış ise ,  sistemdeki kullanıcıyı user a atıyoruz  ve kullanıcıya gönderilmiş arkadaşlık
#isteklerinin sayısını geriye dönderiyoruz
def invatations_received_no(request):
    if request.user.is_authenticated:
        profile_obj = Profile.objects.get(user=request.user)
        qs_count=Relationship.objects.invatations_recived(profile_obj).count()
        return {"invities_num":qs_count}
    return {}