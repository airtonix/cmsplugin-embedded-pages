from django.forms import ModelForm
from django.forms import ModelChoiceField, ChoiceField

from .lib.choices import (
  DynamicTemplateChoices,
  PlaceholdersDynamicChoices
)

from .models import (
  TEMPLATE_PATH,
  EmbedPagesPlugin,
)


class EmbedPagesAdminForm(ModelForm):

    class Meta :
        model = EmbedPagesPlugin

    def __init__(self, *args, **kwargs):
        super(EmbedPagesAdminForm, self).__init__(*args,**kwargs)
        self.fields['template'].choices = DynamicTemplateChoices(
                     path = TEMPLATE_PATH,
                  include = '.html',
                  exclude = 'base')

        self.fields['placeholders'].choices = PlaceholdersDynamicChoices()
