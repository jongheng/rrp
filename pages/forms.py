from django import forms
from .models import TestDescription
# from .models import UserProfileInfo
# from .models import MailingList
# from django.contrib.auth.models import User

# class UserForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput()) 

# class Meta():
#     model = User
#     fields =('useranme', 'password', 'email')

# class UserProfileInfoForm(forms.ModelForm):
#     class Meta():
#         pass   

# class MailingListForm(forms.ModelForm):
    
#     class Meta:
#         model = MailingList
#         fields = ["email"]

class TestDescriptionForm(forms.ModelForm):
    class Meta:
        model = TestDescription
        # fields = ["id", "publish_at", "media_name", "version_number",
        #           "test_duration", "memory", "hard_disk_interface",
        #           "cpu_turbo", "os_version", "video_format",
        #           "cores", "display_resolution"  
        
        # ]
        fields = '__all__'

          