# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'TimeStampedModel'
        db.create_table('core_timestampedmodel', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('core', ['TimeStampedModel'])

        # Adding model 'PortfolioItem'
        db.create_table('core_portfolioitem', (
            ('timestampedmodel_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.TimeStampedModel'], unique=True, primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal('core', ['PortfolioItem'])

        # Adding M2M table for field tag on 'PortfolioItem'
        db.create_table('core_portfolioitem_tag', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('portfolioitem', models.ForeignKey(orm['core.portfolioitem'], null=False)),
            ('portfoliotag', models.ForeignKey(orm['core.portfoliotag'], null=False))
        ))
        db.create_unique('core_portfolioitem_tag', ['portfolioitem_id', 'portfoliotag_id'])

        # Adding model 'PortfolioTag'
        db.create_table('core_portfoliotag', (
            ('timestampedmodel_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.TimeStampedModel'], unique=True, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
        ))
        db.send_create_signal('core', ['PortfolioTag'])


    def backwards(self, orm):
        
        # Deleting model 'TimeStampedModel'
        db.delete_table('core_timestampedmodel')

        # Deleting model 'PortfolioItem'
        db.delete_table('core_portfolioitem')

        # Removing M2M table for field tag on 'PortfolioItem'
        db.delete_table('core_portfolioitem_tag')

        # Deleting model 'PortfolioTag'
        db.delete_table('core_portfoliotag')


    models = {
        'core.portfolioitem': {
            'Meta': {'ordering': "('-date',)", 'object_name': 'PortfolioItem', '_ormbases': ['core.TimeStampedModel']},
            'date': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
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
