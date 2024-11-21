from django.views.generic import TemplateView
import requests
import json


address = 'http://_api.internal:4280/v1/apps/python-django/machines'
val = "Bearer dummytoken"
r = requests.get(address, headers={"Authorization": val}).text
obj = json.loads(r)[0]

class HomepageView(TemplateView):
    template_name = "homepage.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['machines'] = obj
        return context
