from django.views.generic import TemplateView

# Create your views here.
class LoginView(TemplateView):
    template_name = "login/form.html"