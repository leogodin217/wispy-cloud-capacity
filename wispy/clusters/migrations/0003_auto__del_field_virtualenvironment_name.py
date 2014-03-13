# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'VirtualEnvironment.name'
        db.delete_column(u'clusters_virtualenvironment', 'name')


    def backwards(self, orm):
        # Adding field 'VirtualEnvironment.name'
        db.add_column(u'clusters_virtualenvironment', 'name',
                      self.gf('django.db.models.fields.CharField')(default='ve1', max_length=100),
                      keep_default=False)


    models = {
        u'clusters.virtualenvironment': {
            'Meta': {'object_name': 'VirtualEnvironment'},
            'application_layer': ('django.db.models.fields.CharField', [], {'default': "'General'", 'max_length': '64'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'market': ('django.db.models.fields.CharField', [], {'default': "'DCU'", 'max_length': '64'}),
            'notes': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'pipe': ('django.db.models.fields.CharField', [], {'default': "'General'", 'max_length': '64'}),
            'segment': ('django.db.models.fields.CharField', [], {'default': "'Internal'", 'max_length': '64'}),
            'site': ('django.db.models.fields.CharField', [], {'default': "'Folsom'", 'max_length': '64'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'Available'", 'max_length': '64'})
        }
    }

    complete_apps = ['clusters']