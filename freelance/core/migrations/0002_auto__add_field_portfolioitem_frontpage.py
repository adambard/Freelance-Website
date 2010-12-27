# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'PortfolioItem.frontpage'
        db.add_column('core_portfolioitem', 'frontpage', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'PortfolioItem.frontpage'
        db.delete_column('core_portfolioitem', 'frontpage')


    models = {
        'core.portfolioitem': {
            'Meta': {'ordering': "('-date',)", 'object_name': 'PortfolioItem', '_ormbases': ['core.TimeStampedModel']},
            'date': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'frontpage': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'tag': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['core.PortfolioTag']", 'null': 'True', 'blank': 'True'}),
            'timestampedmodel_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.TimeStampedModel']", 'unique': 'True', 'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'core.portfoliotag': {
            'Meta': {'ordering': "('name',)", 'object_name': 'PortfolioTag', '_ormbases': ['core.TimeStampedModel']},
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'timestampedmodel_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.TimeStampedModel']", 'unique': 'True', 'primary_key': 'True'})
        },
        'core.timestampedmodel': {
            'Meta': {'object_name': 'TimeStampedModel'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['core']
