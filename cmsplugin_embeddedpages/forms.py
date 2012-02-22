from django.forms import ModelForm
from django.utils.safestring import SafeString
from django.forms import ModelChoiceField, ChoiceField

from .lib.choices import (
  DynamicTemplateChoices,
  )

from .models import (
  PagePluginSettings,
  TEMPLATE_PATH,
  GROUP_TEMPLATE_PATH,
  PAGE_TEMPLATE_PATH,
)


class PagePluginAdminForm(ModelForm):

    class Meta :
        model = PagePluginSettings

    def __init__(self, *args, **kwargs):
        super(PagePluginAdminForm, self).__init__(*args,**kwargs)

        self.fields['group_template'].choices = DynamicTemplateChoices(
                     path = GROUP_TEMPLATE_PATH,
                  include = '.html',
                  exclude = 'base')

        self.fields['page_template'].choices = DynamicTemplateChoices(
                     path = PAGE_TEMPLATE_PATH,
                  include = '.html',
                  exclude = 'base')

        choices = [self.fields['root'].choices.__iter__().next()]
        for page in self.fields['root'].queryset:
            choices.append(
                (page.id,
                 SafeString(''.join([u"&nbsp;&nbsp;&nbsp;"*page.level,
                   page.__unicode__()]))))

        self.fields['root'].choices = choices
