import os

from django.db import models

from cms.models.pluginmodel import CMSPlugin

from .lib.choices import (
  DynamicTemplateChoices,
  PlaceholdersDynamicChoices,
#  PageIDsDynamicChoices,
#  PageAttributeDynamicChoices,
)

TEMPLATE_PATH = os.path.join("cmsplugin_embeddedpages","layouts")
GROUP_TEMPLATE_PATH = os.path.join(TEMPLATE_PATH, "groups")
PAGE_TEMPLATE_PATH = os.path.join(TEMPLATE_PATH, "pages")

#class FilterRule(models.Model):
#    QUERY_ACTION_CHOICES = (
#      ("filter", "Show only"),
#      ("exclude", "Hide"),
#    )
#    OPERATION_CHOICES = (
#      ("=", "Equal To"),
#      ("_lt =", "Less Than"),
#      ("_lte =", "Less than or Equal to"),
#      ("_gt =", "Greater than"),
#      ("_gte =", "Greater than or Equal to"),
#      ("_contains =", "Contains"),
#      ("_icontains =", "Contains (case insensitive)"),
#      ("_startswith =", "Starts with"),
#      ("_istartswith =", "Starts with (case insensitive)"),
#      ("_isnull =", "Is Null"),
#      ("_in =", "Is in the list"),
#    )

#    attribute_name = models.CharField("Attribute", max_length=128)

#    attribute_operation = models.CharField("Operator", max_length=128,
#      choices=OPERATION_CHOICES)

#    attribute_value = models.CharField("Value", max_length=128,
#      blank=True, null=True)

#    query_action = models.CharField("Action", max_length=128,
#      choices=QUERY_ACTION_CHOICES)

#class Ruleset(models.Model):
#    rule = models.ForeignKey('FilterRule')
#    view = models.ForeignKey('Settings')
#    description = models.CharField(max_length=128)



class PagePluginSettings(CMSPlugin):
    """ Stores options for cmsplugin that shows lists of ProductTypes
    """
    group_template = models.CharField(choices=DynamicTemplateChoices(
                                          path=GROUP_TEMPLATE_PATH,
                                          include='.html',
                                          exclude='base'),
      max_length=256, blank=True, null=True,
      help_text="""Select a template to render this
      list. Templates are stored in : {0}""".format(GROUP_TEMPLATE_PATH))

    page_template = models.CharField(choices=DynamicTemplateChoices(
                                          path=PAGE_TEMPLATE_PATH,
                                          include='.html',
                                          exclude='base'),
      max_length=256, blank=True, null=True,
      help_text="""Select a template to render this
      list. Templates are stored in : {0}""".format(PAGE_TEMPLATE_PATH))

    root = models.ForeignKey("cms.Page",
      help_text="""Start including pages at a page which has this ID""")

    placeholders = models.ManyToManyField('cms.Placeholder',
      blank=True, null=True, help_text="""Only render content
      within these placeholders.""")

    include_root = models.BooleanField(default=True,
      help_text="""Should the root page also be included in the output?
        If the root page is also the page where this plugin is being used then
        it will never be included. (to prevent recursion)""")

    depth = models.PositiveIntegerField(default=0,
      help_text="""How deep should menu traversal go?""")

#    filters = models.ManyToManyField('FilterRule',
#      through = Ruleset,
#      help_text="""Page attributes to perform filters on.""")

    def __unicode__(self):
        output = U"[{0}] {1}".format(
          self.root.id,
          self.root.get_slug(),
        )
        if self.depth >= 0:
          output = U"{0}, Traversing: {1} level".format(output, self.depth)
        return output
