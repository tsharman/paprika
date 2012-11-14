# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'OAuthConsumer'
        db.create_table('api_oauth_consumer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('key', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('secret', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('paprika', ['OAuthConsumer'])

        # Deleting field 'Order.notes'
        db.delete_column('paprika_order', 'notes')


    def backwards(self, orm):
        # Deleting model 'OAuthConsumer'
        db.delete_table('api_oauth_consumer')

        # Adding field 'Order.notes'
        db.add_column('paprika_order', 'notes',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=300, blank=True),
                      keep_default=False)


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
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'business'", 'unique': 'True', 'primary_key': 'True', 'to': "orm['auth.User']"})
        },
        'paprika.feedentry': {
            'Meta': {'object_name': 'FeedEntry'},
            'body': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'feeds'", 'to': "orm['paprika.Order']"}),
            'time_entered': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        'paprika.flow': {
            'Meta': {'object_name': 'Flow'},
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'flow_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'flows'", 'to': "orm['paprika.BusinessProfile']"})
        },
        'paprika.oauthconsumer': {
            'Meta': {'object_name': 'OAuthConsumer', 'db_table': "'api_oauth_consumer'"},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'secret': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'paprika.order': {
            'Meta': {'object_name': 'Order'},
            'current_stage': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['paprika.Stage']"}),
            'cust_email': ('django.db.models.fields.EmailField', [], {'max_length': '254'}),
            'cust_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'cust_phone': ('django.contrib.localflavor.us.models.PhoneNumberField', [], {'max_length': '20'}),
            'flow': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'orders'", 'to': "orm['paprika.Flow']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'merchant': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'orders'", 'to': "orm['paprika.BusinessProfile']"}),
            'state': ('django.db.models.fields.CharField', [], {'default': "'current'", 'max_length': '10'}),
            'time_entered': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        'paprika.stage': {
            'Meta': {'object_name': 'Stage'},
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'flow': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'stages'", 'to': "orm['paprika.Flow']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'stage_num': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['paprika']