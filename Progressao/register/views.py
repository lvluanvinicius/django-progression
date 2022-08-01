from django.views.generic import TemplateView

# Create your views here.
class CreateView(TemplateView):
    template_name = "register/form-activity.html"