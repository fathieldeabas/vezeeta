from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.utils.text import slugify
# Create your models here.#
class Profile(models.Model):

    doctor_in=(

        ("ختصاص أمراض الأطفال","ختصاص أمراض الأطفال"),
        ("الصدر والجهاز التنفسي","الصدر والجهاز التنفسي"),
        ("طب الأشعة","طب الأشعة"),
        ("الأنف والأذن والحنجرة","الأنف والأذن والحنجرة"),
        ("طب الأعصاب وجراحتها","طب الأعصاب وجراحتها"),
        ("الطب النفسي","الطب النفسي"),
        (" الجراحة التجميلية"," الجراحة التجميلية"),
        ("طب الأعصاب وجراحتها","طب الأعصاب وجراحتها")
              
              )
    user= models.OneToOneField(User,verbose_name=_("user"),on_delete=models.CASCADE, related_name="Profile")
    name= models.CharField(_("الاسم :"),max_length=50,null=True)
    subtitle= models.CharField(_("نبذه عنك:") ,max_length=50, null=True)
    address = models.CharField(_("المحافطه:") , max_length=50, null=True)
    address_details= models.CharField(_("العنوان بالتفاصيل:"),max_length=50, null=True)
    number_phone = models.IntegerField(_("الهاتف:"), null=True)
    working_hours= models.CharField(_("عدد ساعات العمل:"),max_length=50)
    waiting_time=models.IntegerField(_("مده الانتظار:"),null=True)
    doctor = models.CharField(_("دكتور ؟"),choices=doctor_in,max_length=50,null=True)
    specialist_doctor= models.CharField(_("متخصص في ؟"),max_length=50,null=True)
    who_i= models.TextField(_("من انا:"),max_length=250 ,null=True)
    price = models.IntegerField(_(":سعر الكشف"),null=True)
    image = models.ImageField(_("الضوره الشخصيه:"), upload_to="profile" ,null=True)
    slug= models.CharField(_("slug"),blank=True,null=True,max_length=50)
    facebook = models.CharField(max_length=100,null=True)
    twitter = models.CharField(max_length=100,null=True)
    google = models.CharField(max_length=100,null=True)


    def save(self, *args, **kwargs):
        if not self.slug :
            self.slug= slugify(self.user.username) 
        super(Profile, self).save(*args, **kwargs) # Call the real save() method
    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")

    def __str__(self):
        return  '%s'% self.user.username


def create_profile(sender, **kwargs):
    if kwargs["created"]:
        Profile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile,sender=User)   


doctor_date=(

    ("1","1"),
    ("2","2"),("3","3"),("4","4"),("5","5"),("6","6"),("7","7"),
)


class Order(models.Model):
    patient=models.CharField(_("اسم المريض:"),max_length=50,null=True)
    completed= models.BooleanField()
    profile= models.ForeignKey(Profile, on_delete=models.CASCADE)
    date= models.CharField(_("المعاد:"),choices=doctor_date, max_length=50)
    time_order=models.TimeField(_("وقت تنفيذ الاوردر"), auto_now=False, auto_now_add=True)
    patient_email=models.CharField(_("حساب المريض:"),max_length=50,null=True)


    def __str__(self):
        return  self.patient
    