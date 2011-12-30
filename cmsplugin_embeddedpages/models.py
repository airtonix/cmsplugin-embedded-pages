import os

from django.db import models
from cms.models.pluginmodel import CMSPlugin

from .lib.choices import (
  DynamicTemplateChoices,
  PlaceholdersDynamicChoices,
  PageIDsDynamicChoices,
  PageAttributeDynamicChoices,
)

TEMPLATE_PATH = os.path.join("cmsplugin_embeddedpages","layouts")

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

class Settings(CMSPlugin):
    """ Stores options for cmsplugin that shows lists of ProductTypes
    """

    TEMPLATE_CHOICES = DynamicTemplateChoices(
            path=TEMPLATE_PATH,
            include='.html',
            exclude='base')

    page_id = models.CharField("Show sub pages of",
      choices=PageIDsDynamicChoices(), max_length=50, default='home',
      help_text="""Start including pages at a page which has this ID""")

    include_root = models.BooleanField(default=True,
      help_text="""Should the root page also be included in the output?
        If the root page is also the page where this plugin is being used then
        it will never be included. (to prevent recursion)""")

#    levels_deep = models.PositiveIntegerField(default=0,
#      help_text="""How far down the tree should pages be included for
#      embedding?""")

#    placeholders = models.CharField(choices=PlaceholdersDynamicChoices(),
#      max_length=128, blank=True, null=True, help_text="""Only render content
#      within placeholders of these names.""")

#    filters = models.ManyToManyField('FilterRule',
#      through = Ruleset,
#      help_text="""Page attributes to perform filters on.""")

    template = models.CharField(choices=TEMPLATE_CHOICES,
      max_length=256, blank=True, null=True,
      help_text="""Select a template to render this
      list. Templates are stored in : {0}""".format(TEMPLATE_PATH))

#    def __unicode__(self):
#        return U"Root:{0}, levels: {1}, Placeholders: {2}".format(
#          self.page_id, self.levels_deep, self.placeholders)
