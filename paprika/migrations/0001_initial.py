# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Flow'
        db.create_table('paprika_flow', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('flow_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(related_name='flows', to=orm['auth.User'])),
        ))
        db.send_create_signal('paprika', ['Flow'])

        # Adding model 'Stage'
        db.create_table('paprika_stage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('stage_num', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('flow', self.gf('django.db.models.fields.related.ForeignKey')(related_name='stages', to=orm['paprika.Flow'])),
        ))
        db.send_create_signal('paprika', ['Stage'])

        # Adding model 'Order'
        db.create_table('paprika_order', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('flow', self.gf('django.db.models.fields.related.ForeignKey')(related_name='orders', to=orm['paprika.Flow'])),
            ('merchant', self.gf('django.db.models.fields.related.ForeignKey')(related_name='orders', to=orm['auth.User'])),
            ('order_code', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('current_stage', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['paprika.Stage'])),
            ('cust_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('cust_email', self.gf('django.db.models.fields.EmailField')(max_length=254)),
        ))
        db.send_create_signal('paprika', ['Order'])

        # Adding model 'BusinessProfile'
        db.create_table('paprika_businessprofile', (
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True, primary_key=True)),
            ('business_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('paprika', ['BusinessProfile'])


    def backwards(self, orm):
        # Deleting model 'Flow'
        db.delete_table('paprika_flow')

        # Deleting model 'Stage'
        db.delete_table('paprika_stage')

        # Deleting model 'Order'
        db.delete_table('paprika_order')

        # Deleting model 'BusinessProfile'
        db.delete_table('paprika_businessprofile')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'paprika.businessprofile': {
            'Meta': {'object_name': 'BusinessProfile'},
            'business_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True', 'primary_key': 'True'})
        },
        'paprika.flow': {
            'Meta': {'object_name': 'Flow'},
            'flow_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'flows'", 'to': "orm['auth.User']"})
        },
        'paprika.order': {
            'Meta': {'object_name': 'Order'},
            'current_stage': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['paprika.Stage']"}),
            'cust_email': ('django.db.models.fields.EmailField', [], {'max_length': '254'}),
            'cust_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'flow': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'orders'", 'to': "orm['paprika.Flow']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'merchant': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'orders'", 'to': "orm['auth.User']"}),
            'order_code': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        'paprika.stage': {
            'Meta': {'object_name': 'Stage'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'flow': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'stages'", 'to': "orm['paprika.Flow']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'stage_num': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['paprika']