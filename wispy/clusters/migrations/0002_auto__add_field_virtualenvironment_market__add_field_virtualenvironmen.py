# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'VirtualEnvironment.market'
        db.add_column(u'clusters_virtualenvironment', 'market',
                      self.gf('django.db.models.fields.CharField')(default='DCU', max_length=64),
                      keep_default=False)

        # Adding field 'VirtualEnvironment.site'
        db.add_column(u'clusters_virtualenvironment', 'site',
                      self.gf('django.db.models.fields.CharField')(default='Folsom', max_length=64),
                      keep_default=False)

        # Adding field 'VirtualEnvironment.segment'
        db.add_column(u'clusters_virtualenvironment', 'segment',
                      self.gf('django.db.models.fields.CharField')(default='Internal', max_length=64),
                      keep_default=False)

        # Adding field 'VirtualEnvironment.application_layer'
        db.add_column(u'clusters_virtualenvironment', 'application_layer',
                      self.gf('django.db.models.fields.CharField')(default='General', max_length=64),
                      keep_default=False)

        # Adding field 'VirtualEnvironment.pipe'
        db.add_column(u'clusters_virtualenvironment', 'pipe',
                      self.gf('django.db.models.fields.CharField')(default='General', max_length=64),
                      keep_default=False)

        # Adding field 'VirtualEnvironment.notes'
        db.add_column(u'clusters_virtualenvironment', 'notes',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)

        # Adding field 'VirtualEnvironment.status'
        db.add_column(u'clusters_virtualenvironment', 'status',
                      self.gf('django.db.models.fields.CharField')(default='Available', max_length=64),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'VirtualEnvironment.market'
        db.delete_column(u'clusters_virtualenvironment', 'market')

        # Deleting field 'VirtualEnvironment.site'
        db.delete_column(u'clusters_virtualenvironment', 'site')

        # Deleting field 'VirtualEnvironment.segment'
        db.delete_column(u'clusters_virtualenvironment', 'segment')

        # Deleting field 'VirtualEnvironment.application_layer'
        db.delete_column(u'clusters_virtualenvironment', 'application_layer')

        # Deleting field 'VirtualEnvironment.pipe'
        db.delete_column(u'clusters_virtualenvironment', 'pipe')

        # Deleting field 'VirtualEnvironment.notes'
        db.delete_column(u'clusters_virtualenvironment', 'notes')

        # Deleting field 'VirtualEnvironment.status'
        db.delete_column(u'clusters_virtualenvironment', 'status')


    models = {
        u'clusters.virtualenvironment': {
            'Meta': {'object_name': 'VirtualEnvironment'},
            'application_layer': ('django.db.models.fields.CharField', [], {'default': "'General'", 'max_length': '64'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'market': ('django.db.models.fields.CharField', [], {'default': "'DCU'", 'max_length': '64'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'ve1'", 'max_length': '100'}),
            'notes': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'pipe': ('django.db.models.fields.CharField', [], {'default': "'General'", 'max_length': '64'}),
            'segment': ('django.db.models.fields.CharField', [], {'default': "'Internal'", 'max_length': '64'}),
            'site': ('django.db.models.fields.CharField', [], {'default': "'Folsom'", 'max_length': '64'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'Available'", 'max_length': '64'})
        }
    }

    complete_apps = ['clusters']