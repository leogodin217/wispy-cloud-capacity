# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Cluster'
        db.create_table(u'clusters_cluster', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='cluster1', max_length=100)),
            ('notes', self.gf('django.db.models.fields.TextField')(default='N/A')),
            ('status', self.gf('django.db.models.fields.CharField')(default='Open', max_length=100)),
            ('virtual_environment', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['clusters.VirtualEnvironment'])),
        ))
        db.send_create_signal(u'clusters', ['Cluster'])


    def backwards(self, orm):
        # Deleting model 'Cluster'
        db.delete_table(u'clusters_cluster')


    models = {
        u'clusters.cluster': {
            'Meta': {'object_name': 'Cluster'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'cluster1'", 'max_length': '100'}),
            'notes': ('django.db.models.fields.TextField', [], {'default': "'N/A'"}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'Open'", 'max_length': '100'}),
            'virtual_environment': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['clusters.VirtualEnvironment']"})
        },
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