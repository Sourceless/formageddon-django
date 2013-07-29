# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Senator'
        db.create_table('contact_senator_senator', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('contact_form_url', self.gf('django.db.models.fields.CharField')(max_length=1024)),
        ))
        db.send_create_signal('contact_senator', ['Senator'])


    def backwards(self, orm):
        # Deleting model 'Senator'
        db.delete_table('contact_senator_senator')


    models = {
        'contact_senator.senator': {
            'Meta': {'object_name': 'Senator'},
            'contact_form_url': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['contact_senator']