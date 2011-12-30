# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'FilterRule'
        db.create_table('cmsplugin_embeddedpages_filterrule', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('attribute_name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('attribute_operation', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('attribute_value', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('query_action', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal('cmsplugin_embeddedpages', ['FilterRule'])

        # Adding model 'Ruleset'
        db.create_table('cmsplugin_embeddedpages_ruleset', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('rule', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cmsplugin_embeddedpages.FilterRule'])),
            ('view', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cmsplugin_embeddedpages.Settings'])),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal('cmsplugin_embeddedpages', ['Ruleset'])

        # Adding model 'Settings'
        db.create_table('cmsplugin_settings', (
            ('cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('page_id', self.gf('django.db.models.fields.CharField')(default='home', max_length=50)),
            ('include_root', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('levels_deep', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('placeholders', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('template', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
        ))
        db.send_create_signal('cmsplugin_embeddedpages', ['Settings'])


    def backwards(self, orm):
        
        # Deleting model 'FilterRule'
        db.delete_table('cmsplugin_embeddedpages_filterrule')

        # Deleting model 'Ruleset'
        db.delete_table('cmsplugin_embeddedpages_ruleset')

        # Deleting model 'Settings'
        db.delete_table('cmsplugin_settings')


    models = {
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'cmsplugin_embeddedpages.filterrule': {
            'Meta': {'object_name': 'FilterRule'},
            'attribute_name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'attribute_operation': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'attribute_value': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'query_action': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'cmsplugin_embeddedpages.ruleset': {
            'Meta': {'object_name': 'Ruleset'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rule': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cmsplugin_embeddedpages.FilterRule']"}),
            'view': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cmsplugin_embeddedpages.Settings']"})
        },
        'cmsplugin_embeddedpages.settings': {
            'Meta': {'object_name': 'Settings', 'db_table': "'cmsplugin_settings'", '_ormbases': ['cms.CMSPlugin']},
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'filters': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['cmsplugin_embeddedpages.FilterRule']", 'through': "orm['cmsplugin_embeddedpages.Ruleset']", 'symmetrical': 'False'}),
            'include_root': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'levels_deep': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'page_id': ('django.db.models.fields.CharField', [], {'default': "'home'", 'max_length': '50'}),
            'placeholders': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'template': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['cmsplugin_embeddedpages']
