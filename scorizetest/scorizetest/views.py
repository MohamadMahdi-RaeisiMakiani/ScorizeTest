from django.views.generic import TemplateView
from django.templatetags.static import static


class MainPage(TemplateView):
    template_name = 'mainPage_index.html'
    website_name = 'Scorize'
    extra_context = {'name': website_name}
