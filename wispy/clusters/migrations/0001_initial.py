# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'VirtualEnvironment'
        db.create_table(u'clusters_virtualenvironment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'clusters', ['VirtualEnvironment'])


    def backwards(self, orm):
        # Deleting model 'VirtualEnvironment'
        db.delete_table(u'clusters_virtualenvironment')


    models = {
        u'clusters.virtualenvironment': {
            'Meta': {'object_name': 'VirtualEnvironment'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['clusters']