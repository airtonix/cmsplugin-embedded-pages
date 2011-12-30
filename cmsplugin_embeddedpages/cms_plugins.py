import os

from django.utils.translation import ugettext_lazy as _
from django.contrib import admin

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from cms.models.pagemodel import Page

from .models import (
    Settings,
    Ruleset,
    FilterRules,
    TEMPLATE_PATH,
)

from .forms import EmbedPagesAdminForm

class EmbedPages(CMSPluginBase):
    model = Settings
    name = _("Embedded Pages")
    render_template = "cmsplugin_embeddedpages/base.html"
    default_template = os.path.join(TEMPLATE_PATH, "default.html")
    admin_preview = False
#    form = EmbedPagesAdminForm
#    filter_horizontal = ('placeholders',)
#    inlines = (EmbeddedPageFilterInlineAdmin, )

#    fieldsets = (
#      ('',
#          {'fields': [ ('include_root', 'page_id'),
#                       ('placeholders', )
#                      ]}),

#      ('Display Template',
#          {'fields': [ ('template', ),
#                      ]}),

#    )

    def render(self, context, instance, placeholder):
        root_page = None
        pages = list()
        # get the root

        try :
            root_page = Page.objects.get(reverse_id = instance.page_id)

            if instance.include_root:
                # if settings say, attach root as well, then do it here.
                pages += (root_page, )

            try :
                pages = Page.objects.filter(parent=root_page,
                                             published=True,
                                             in_navigation=True)

#                if instance.filter_actions and instance.filter_attributes:
#                    pages = getattr(pages, instance.filter_actions)(reverse_id = instance.filter_attributes)

                for page in pages:
                    pages += (page, )

            except:
                pass

        except Page.DoesNotExist, error:
            # no root page matching set id, bail out here.
            context['error'] = error
        except Exception, error:
            # no root page matching set id, bail out here.
            context['error'] = error

        context.update({
          'EmbededPages': pages,
#          'Template' : instance.template if instance.template else self.default_template
        })

        return context

plugin_pool.register_plugin(EmbedPages)
