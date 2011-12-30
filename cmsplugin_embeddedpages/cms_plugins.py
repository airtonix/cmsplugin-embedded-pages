import os

from django.utils.translation import ugettext_lazy as _
from django.contrib import admin


from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin

from cms.models.pagemodel import Page

from .forms import PagePluginAdminForm

from .models import (
    PagePluginSettings,
#    Ruleset,
#    FilterRules,
    TEMPLATE_PATH,
)

class PagePlugin(CMSPluginBase):
    model = PagePluginSettings
    name = _("Embedded Pages")
    render_template = "cmsplugin_embeddedpages/base.html"
    default_template = os.path.join(TEMPLATE_PATH, "default.html")
    admin_preview = False
    filter_horizontal = ('placeholders', )
    form = PagePluginAdminForm

    fieldsets = (

      ('Display Template',
          {'fields': [ ('group_template', 'page_template', ),
                      ]}),
      ('Include',
          {'fields': [ ('root','include_root', ),
                       ('depth', ),
                       ('placeholders', )
                      ]}),

    )

    def render(self, context, instance, placeholder):
        root_page = None
        pages = list()
        # get the root

        try :

            if instance.include_root:
                # if settings say, attach root as well, then do it here.
                pages += (instance.root, )

            try :
                pages = Page.objects.filter(parent=instance.root,
                                             published=True,
                                             in_navigation=True)

#                if instance.filter_actions and instance.filter_attributes:
#                    pages = getattr(pages, instance.filter_actions)(reverse_id = instance.filter_attributes)

            except:
                pass

        except Exception, error:
            pass

        context.update({
          'EmbeddedPages': pages,
        })

        return context

plugin_pool.register_plugin(PagePlugin)
