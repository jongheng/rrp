from django.db import models
from django.urls import reverse
from django.forms import ModelForm
from django.utils import timezone

# class UserProfileInfo(models.Model):
    
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     portfolio_site = models.URLField(blank=True)
#     portfolio_pic = models.ImageField(upload_to='profile_pics', blank=True)

#     def __str__(self):
#         return self.user.username

# class MailingList(models.Model):
#     email = models.EmailField()
#     date_created = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.email

MEDIACCERATOR = (
        ('MARS VER 4.7.0.408', 'MARS VER 4.7.0.408'),
        ('Indigo Island VER 1.0', 'Indigo Island VER 1.0'),
        ('Other', 'Other')
    )

MARS = (
    ('Sawtooth Ridge', 'Sawtooth Ridge'),
    ('Arlington Ridge', 'Arlington Ridge')
)  

PRESETCONFIG = (
    ('DS Entry_Atom_Single 1080P video with overlay + Ticker', 'DS Entry_Atom_Single 1080P video with overlay + Ticker'),
    ('DS Mainstream_Core i3_4K 30 FPS overlay on 1080P + Ticker', 'DS Mainstream_Core i3_4K 30FPS overlay on 1080P + Ticker'),
    ('DS Performance_Core i5_Two Displays with one 4K 30 FPS and 2x4K images and ticker', 'DS Performance_Core i5_Two Displays with one 4K 30 FPS and 2x4K images and ticker'),
    ('DS Extreme_Core i7_2x4K@60@30 video + image + ticker', 'DS Extreme_Core i7_2x4K@60@30 video + image + ticker'),
    ('IWB Entry_Core i3_Entry Signage + Encode', 'IWB Entry_Core i3_Entry Signage + Encode'),
    ('IWB Mainstream_Core i5_Mainstream Signage + Encode', 'IWB Mainstream_Core i5_Mainstream Signage + Encode'),
    ('IWB Performance_Core i7/IRIS_Two Display, 4x1080@30, 1x4K@60, 1x4K@30 Encode', 'IWB Performance_Core i7/IRIS_Two Display, 4x1080@30, 1x4K@60, 1x4K@30 Encode')
)

TESTDURATION = (
        ('15', '00:00:15:00'),
        ('30', '00:00:30:00'),
        ('1:00', '00:01:00:00'),
        ('1:30', '00:01:30:00'),
        ('3:00', '00:03:00:00'),
        ('4:00', '00:04:00:00'),
        ('5:00', '00:05:00:00'),
        ('0', 'Overnight')
    )

MEMORY = (
        ('2', '2'),
        ('4', '4'),
        ('6', '8'),
        ('16', '16'),
        ('32', '32'),
        ('Other', 'Other'),

    )

HARDISKINTERFACE = (
        ('IDE', 'IDE'),
        ('SATA', 'SATA'),
        ('NVMe', 'NVMe'),
        ('Other', 'Other'),
    )

CPUTURBO = (
        ('on', 'ON'),
        ('off', 'OFF')
    )

OSVERSION = (
        ('Ubuntu 16.04 LTS 64bits', 'Ubuntu 16.04 LTS 64bits'),
        ('Ubuntu 18.11 LTS 64bits', 'Ubuntu 18.11 LTS 64bits'),
        ('Windows 10 x32', 'Windows 10 x32'),
        ('Windows 10 x64', 'Windows 10 x64'),
        ('Other', 'Other')
    )

VIDEOFORMAT = (
        ('H264', 'H264'),
        ('H265/HEVC', 'H265/HEVC'),
        ('Other', 'Other')
    )

CORES = (
        ('1', '1 Core'),
        ('2', '2 Core'),
        ('3', '3 Core'),
        ('4', '4 Core'),
        ('All', 'All')
    )

DISPLAYRESOLUTION = (
        ('1920x1080(FHD)', '1920x1080(FHD)'),
        ('2560x1440(4K)', '2560x1440(4K)'),
        ('3840x2160(4K)', '3840x2160(4K)'),
        ('7680x4320(7K)', '7680x4320(7K)'),
        ('Other', 'Other')
    )

class CodeBenchmark(models.Model):
    pass

class TestDescription(models.Model):
   
    # code_benchmark = models.ForeignKey(CodeBenchmark, on_delete=models.CASCADE)
    # publish_date   = models.DateField(blank=True, null=True)
    # id             = models.CharField(max_length=60, primary_key=True)
    publish_at     = models.DateTimeField(default=timezone.now)
    media_name     = models.CharField(max_length=300, verbose_name='Media Accelerator Reference Software', choices=MEDIACCERATOR)
    # version_number = models.CharField(max_length=300, choices=MEDIACCERATOR)
    preset_conf_file = models.CharField(max_length=500,verbose_name='Preset or Config File Name', choices=PRESETCONFIG)
    test_duration  = models.CharField(max_length=300, choices=TESTDURATION)
    memory         = models.CharField(max_length=300, choices=MEMORY)
    hard_disk_interface = models.CharField(max_length=100, choices=HARDISKINTERFACE)
    cpu_turbo      = models.CharField(max_length=300, choices=CPUTURBO)
    os_version     = models.CharField(max_length=300, choices=OSVERSION)
    video_format   = models.CharField(max_length=300, choices=VIDEOFORMAT)
    cores          = models.CharField(max_length=300, choices=CORES)
    display_resolution = models.CharField(max_length=300, choices=DISPLAYRESOLUTION)
    total_number_zone = models.CharField(max_length=300, verbose_name='Total Number Of Zones')
    total_number_ticker_zone = models.CharField(max_length=300, verbose_name='Total Number Of Ticker Zones')
    total_number_widget_zone = models.CharField(max_length=300, verbose_name='Total Number Of Widget Zones')
    total_number_html_zone = models.CharField(max_length=300, verbose_name='Total Number Of Html Zones')
    processor_name = models.CharField(max_length=300, verbose_name='Processor Name')
    processor_speed = models.CharField(max_length=300, verbose_name='Processor Speed')
    chipset = models.CharField(max_length=300, verbose_name='Chipset') 

    def __str__(self):
        return self.id

    # def get_absolute_url(self):
    #     # return reverse("model_detail", kwargs={"pk": self.pk})
    #     return reverse("pages:index")


