from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.views.generic import View, CreateView, TemplateView, UpdateView, DeleteView, ListView
# from hitcount.views import HitCountDetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views import generic


from django.conf import settings

from django.template import RequestContext
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.db.models import Q, F
# from post_office import mail
# from django.http import HttpResponse, HttpResponseRedirect
# from templated_mail.mail import BaseEmailMessage
from .models import TestDescription
from .models import HitCount
# from .models import TestDescription as TestModel
# from .models import HitCountModel
from .forms import TestDescriptionForm
from .filters import TestFilter   

html_message = render_to_string('html_mail.html', {'context':'value'})
subject = 'RBHE-SVE Email'
plain_message = strip_tags(html_message)
email_sender = 'giap.jongx.toh@intel.com'
email_receivers = ['giap.jongx.toh@intel.com','jongtoh23@gmail.com',]
# from .forms import MailingListForm
# from .models import MailingList
# from .emails import send_multiple_email


# def newsletter_subscribe(request):
#     if request.method == 'POST':
#         form = MailingListForm(request.POST)
#         if form.is_valid():
#             instance = form.save(commit=False) #we dont want to save just yet
#             if MailingList.objects.filter(email=instance.email).exists():
#                 messages.warning(request, "your Email Already exists in our database")
#             else:
#                 instance.save()
#                 messages.success(request, "your Email has been submitted to our database")
#                 send_multiple_email(instance.name, instance.email)
        
#         else:
#             form = MailingListForm()

#         context = {'form':form}
#         template = "newsletter/subscribe.html"
#         return render(request, template, context)

# def home(request):
#     return render(request, "home.html", {})

# def about(request):
#     return render(request, "about.html", {})

# def contact(request):
#     return render(request, "contact.html", {})
    
# def base(request):
#     return render(request, "base.html", {})

# def index(request):
#     return render(request, "index.html", {})

# def left_sidebar(request):
#     return render(request, "left-sidebar.html", {})

# def right_sidebar(request):
#     return render(request, "right-sidebar.html", {})

# def no_sidebar(request):
#     return render(request, "no-sidebar.html", {}) 

# class home(TemplateView):
#     def get(self, request, **kwargs):
#         return render(request, 'home.html', context=None)

# @login_required
# def home(request):
#     return render(request, "home.html", {})

# def email(request):
#     subject = 'Thank you for registering to our site'
#     message = 'It means a world to us'
#     email_from = settings.EMAIL_HOST_USER
#     recipient_list = ['giapjong@icloud.com',]
#     send_mail(subject, message, email_from, recipient_list)
#     return redirect('Point to a new page')
#     # return render(request, "home.html", {})  
  
# class EmailPageView(TemplateView):
#     # model = User
#     subject = 'Thank you for registering to our site'
#     message = 'It means a world to us'
#     email_from = settings.EMAIL_HOST_USER
#     recipient_list = ['giapjong@icloud.com',]
#     mail.send(
#     'jongtoh23@gmail.com','giapjong@icloud.com',
#     subject,
#     message,
#     html_message='<strong>Thank you for registering to our site</strong>'
#     )
#     template_name = "email.html" 

# class TextEmailMessage(BaseEmailMessage):
#     template_name = "text_mail.html"

# class HTMLEmailMessage(BaseEmailMessage):
#     template_name = "html_mail.html"

# class TextAndHTMLEmailMessage(BaseEmailMessage):
#     tenplate_name = "text_html_mail.html" 

# def text_mail_view(request):
#     recipient = ['jongtoh23@gmail.com']
#     TextEmailMessage(request).send(to=recipient)
#     return HttpResponse('Text email has been sent')

# def html_mail_view(request):
#     recipient = ['jongtoh23@gmail.com']
#     TextEmailMessage(request).send(to=recipient)
#     return HttpResponse('HTML email has been sent') 

# def text_html_mail_view(request):
#     recipient = ['jongtoh23@gmail.com']
#     TextEmailMessage(request).send(to=recipient)
#     return HttpResponse('Text and HTML email has been sent')   

class HomePageView(TemplateView):
    template_name = "home.html"        

class AboutPageView(TemplateView):
    template_name = "about.html" 

class ContactPageView(TemplateView):
    template_name = "contact.html" 

class PortfolioPageView(TemplateView):
    template_name = "portfolio.html" 

class AdminView(TemplateView):
    login_required = True
    template_name = "home.html"    

class CountPageView(TemplateView):
    template_name = "base.html"

    def countindex(self, request):

        try:
            hit = HitCount.objects.get(pk=1)
        except:
            hit = HitCount(count=0)
            hit.save()
            pass

        hit = HitCount.objects.filter(pk=1)
        hit.update(count=F('count') + 1)
        hit = HitCount.objects.get(pk=1)

        return render(request, self.template_name)    



# class SignUp(generic.CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'signup.html'

# class IndexTestView(generic.ListView):
#     model = TestDesciption
#     context_object_name = 'test_name'
#     template_name='index.html'

#     def get_queryset(self):
#         return TestDesciption.objects.all()

# class TestEntry(CreateView):
#     model = TestDesciption
#     fields = ['media_name', 'version_number', 'test_duration', 'memory', 
#               'hard_disk_interface', 'cpu_turbo', 'os_version', 'video_format',
#               'cores', 'display_resolution'  
#     ] 

# class TestUpdate(UpdateView):
#     model = TestDesciption
#     fields = ['media_name', 'version_number', 'test_duration', 'memory', 
#               'hard_disk_interface', 'cpu_turbo', 'os_version', 'video_format',
#               'cores', 'display_resolution'  
#     ] 

# class TestDelete(DeleteView):
#     model = TestDesciption
#     fields = ['media_name', 'version_number', 'test_duration', 'memory', 
#               'hard_disk_interface', 'cpu_turbo', 'os_version', 'video_format',
#               'cores', 'display_resolution'  
#     ] 
#     success_url = reverse_lazy('pages:index') 

# class PostCountHitDetailView(HitCountDetailView):
#     model = HitCountModel
#     count_hit = True
 
class TestForm(TemplateView):
    template_name = "testform.html"
    model = TestDescription

    def get(self, request):
        test_list = []
        test_form = TestDescriptionForm
        # tests = TestModel.objects.all()[:2]
        # tests = TestModel.objects.last()
        # tests = TestModel.objects.all()[:2]
        # tests = TestModel.objects.all()[TestModel.objects.count()-1]
        # for i in TestModel.objects.all():
        #     print(i)
        # entry_list = list(TestModel.objects.all())
        # print(entry_list)
        # tests = TestModel.objects.filter()
        tests = TestDescription.objects.last()
        # print(tests)

        # for test in tests:
        #     test_list.append({'publish_at':test.publish_at, 'media_name':test.media_name,
        #                       'preset_conf_file':test.preset_conf_file,   
        #                       'test_duration':test.test_duration,
        #                       'memory':test.memory, 'hard_disk_interface':test.hard_disk_interface,
        #                       'cpu_turbo':test.cpu_turbo, 'os_version':test.os_version, 'video_format':test.video_format,
        #                       'cores':test.cores, 'display_resolution':test.display_resolution,
        #                       'total_number_zone':test.total_number_zone,
        #                       'total_number_ticker_zone':test.total_number_ticker_zone,
        #                       'total_number_widget_zone':test.total_number_widget_zone,
        #                       'total_number_html_zone':test.total_number_html_zone,
        #                       'processor_name':test.processor_name,
        #                       'processor_speed':test.processor_speed,
        #                       'chipset':test.chipset

        #     })
        test_list.append({'publish_at':tests.publish_at, 'media_name':tests.media_name,
                              'code_name':tests.code_name,
                              'preset_conf_file':tests.preset_conf_file,   
                              'test_duration':tests.test_duration,
                              'memory':tests.memory, 'hard_disk_interface':tests.hard_disk_interface,
                              'cpu_turbo':tests.cpu_turbo, 'os_version':tests.os_version, 'video_format':tests.video_format,
                              'cores':tests.cores, 'display_resolution':tests.display_resolution,
                              'total_number_zone':tests.total_number_zone,
                              'total_number_ticker_zone':tests.total_number_ticker_zone,
                              'total_number_widget_zone':tests.total_number_widget_zone,
                              'total_number_html_zone':tests.total_number_html_zone,
                              'processor_name':tests.processor_name,
                              'processor_speed':tests.processor_speed,
                              'chipset':tests.chipset

            })    

        context = {
            
            'test_list': test_list,
            'test_form': test_form
            
        } 
            

        return render(request, self.template_name, context)                   

    def post(self, request):
        test_description = TestDescriptionForm(request.POST)
        if test_description.is_valid():
            id_save = test_description.save()
            print(id_save.id)
            # send_mail('RRP','http://goto.intel.com/RBHE_SVE_PG_Val', 'giap.jongx.toh@intel.com', ['giap.jongx.toh@intel.com','jongtoh23@gmail.com',])
            send_mail(subject + " --" + "id: " + str(id_save.id), plain_message, email_sender, email_receivers, html_message=html_message)
            return redirect('/testform/')
         
class SearchForm(TemplateView):
    template_name = "searchform.html"
    model = TestDescription

    # def get_context_data(self, **kwargs):
    #     context = super(SearchForm, self).get_context_data(**kwargs)

    #     return context

    # def get_queryset(self, request):
    #     query = self.request.GET.get('q')
    #     if query:
    #         return model.objects.filter(publish_at=query) 
    #     else:
    #         return model.objects.all()   

    # def search(self, request):
    #     user_list = model.objects.all()
    #     user_filter = TestFilter(self.request.GET, queryset=user_list)
    #     return render(request, self.template_name, {'filter':user_filter})
    def searchposts(self, request):
        
        if request.method == 'GET':
            query = request.GET.get('q')
            submitbutton = request.GET.get('submit')

            if query is not None:
                # lookups = Q(publish_at___icontains=query) | Q(media_name___icontains=query) | Q(id__icontains=query)
                # results = TestModel.objects.filter(lookups).distinct()
                results = TestDescription.objects.get(id=query)
                print(results) 
                context = {'results':results, 'submitbutton':submitbutton}
                return render(request, self.template_name, context)
            else:
                return render(request, self.template_name)
        else:
            return render(request, self.template_name)                 

# def search(request):
#     try:
#         q = request.GET['q']
#         posts = TestModel.objects.filter(cores__search=q) | \
#                 TestModel.objects.filter(memory__search=q) | \
#                 TestModel.objects.filter(chipset__search=q) 
#         return render(request, 'searchform.html', {'posts':posts, 'q':q})           
#     except KeyError:
#         return render(request, 'searchform.html')  

# def searchposts(request):
#     template_name = "searchform.html"
#     if request.method == 'GET':
#         query = request.GET.get('q')
#         submitbutton = request.GET.get('submit')

#         if query is not None:
#             lookups = Q(publish_at___icontains=query) | Q(media_name___icontains=query)
#             results = TestModel.objects.filter(lookups).distinct() 
#             context = {'results':results, 'submitbutton':submitbutton}
#             return render(request, template_name, context)
#         else:
#             return render(request, template_name)
#     else:
#         return render(request, template_name) 

class Search(ListView):
    template_name = "search.html"
    model = TestDescription

    def get_queryset(self):
        return TestDescription.objects.all().order_by("-publish_at")

    # def get_queryset(self):
    #     reult = super().get_queryset()
    #     query = self.request.GET.get('q')

class SearchView(TemplateView):
    template_name = "searchform.html"
    model = TestDescription

    def get(self, request, *args, **kwargs):
        q = request.GET.get('q', '')
        # self.results = TestDescription.objects.filter(id__icontains=q)
        self.results = TestDescription.objects.filter(id__iexact=q)
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(results=self.results, **kwargs)   
        return context
        
       
def home(request):
        count = User.objects.count()
        return render(request, 'home.html', 
    {
        'count': count
    })

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/login.html', {
        'form': form
    })

@login_required
def secret_page(request):
    return render(request, 'home.html')

class SecretPage(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'

   