from django.forms import ModelForm
from django.utils.safestring import SafeString
<<<<<<< HEAD

from .models import (
  EmbedPagesPlugin,
=======
from django.forms import ModelChoiceField, ChoiceField

from .lib.choices import (
  DynamicTemplateChoices,
  )

from .models import (
  PagePluginSettings,
  TEMPLATE_PATH,
  GROUP_TEMPLATE_PATH,
  PAGE_TEMPLATE_PATH,
>>>>>>> b1cbd94f3893f05a316f8f78d619677c297adeb1
)


class PagePluginAdminForm(ModelForm):

<<<<<<< HEAD
    class Meta:
        model = EmbedPagesPlugin

    def __init__(self, *args, **kwargs):
        super(EmbedPagesAdminForm, self).__init__(*args, **kwargs)
        choices = [self.fields['root'].choices.__iter__().next()]
        for page in self.fields['root'].queryset:
            choices.append(
                (page.id,
                 SafeString(''.join([u"&nbsp;&nbsp;&nbsp;"*page.level,
                   page.__unicode__()]))))

=======
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

>>>>>>> b1cbd94f3893f05a316f8f78d619677c297adeb1
        self.fields['root'].choices = choices
