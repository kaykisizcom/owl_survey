# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Cities'
        db.create_table(u'owl_cities', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', max_length=15)),
            ('cdate', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'owl', ['Cities'])

        # Adding model 'SocialData'
        db.create_table(u'owl_socialdata', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('account_type', self.gf('django.db.models.fields.CharField')(default='0', max_length=1)),
            ('account_id', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('account_token', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('cdate', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'owl', ['SocialData'])

        # Adding model 'Audience'
        db.create_table(u'owl_audience', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', max_length=400)),
            ('cdate', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'owl', ['Audience'])

        # Adding model 'Users'
        db.create_table(u'owl_users', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('profile_photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('gender', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('birthday', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(default='', max_length=11, null=True, blank=True)),
            ('school', self.gf('django.db.models.fields.CharField')(default='', max_length=50)),
            ('jobs', self.gf('django.db.models.fields.CharField')(default='', max_length=50)),
            ('been', self.gf('django.db.models.fields.related.ForeignKey')(related_name='bean', to=orm['owl.Cities'])),
            ('lives_in', self.gf('django.db.models.fields.related.ForeignKey')(related_name='live_in', to=orm['owl.Cities'])),
            ('cdate', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'owl', ['Users'])

        # Adding M2M table for field audience on 'Users'
        m2m_table_name = db.shorten_name(u'owl_users_audience')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('users', models.ForeignKey(orm[u'owl.users'], null=False)),
            ('audience', models.ForeignKey(orm[u'owl.audience'], null=False))
        ))
        db.create_unique(m2m_table_name, ['users_id', 'audience_id'])

        # Adding model 'Survey'
        db.create_table(u'owl_survey', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('name', self.gf('django.db.models.fields.CharField')(default='', max_length=200)),
            ('description', self.gf('django.db.models.fields.CharField')(default='', max_length=1000)),
            ('cdate', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'owl', ['Survey'])

        # Adding M2M table for field audience on 'Survey'
        m2m_table_name = db.shorten_name(u'owl_survey_audience')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('survey', models.ForeignKey(orm[u'owl.survey'], null=False)),
            ('audience', models.ForeignKey(orm[u'owl.audience'], null=False))
        ))
        db.create_unique(m2m_table_name, ['survey_id', 'audience_id'])

        # Adding model 'Question'
        db.create_table(u'owl_question', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question_type', self.gf('django.db.models.fields.CharField')(default='ST', max_length=2)),
            ('question', self.gf('django.db.models.fields.CharField')(default='', max_length=400)),
            ('description', self.gf('django.db.models.fields.CharField')(default='', max_length=200)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('max_limit', self.gf('django.db.models.fields.SmallIntegerField')(blank=True)),
            ('survey', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['owl.Survey'])),
            ('cdate', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'owl', ['Question'])

        # Adding model 'Option'
        db.create_table(u'owl_option', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', max_length=400)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('question', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['owl.Question'])),
            ('cdate', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'owl', ['Option'])

        # Adding model 'WrittenResponse'
        db.create_table(u'owl_writtenresponse', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', max_length=400)),
            ('cdate', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'owl', ['WrittenResponse'])

        # Adding model 'TableDegree'
        db.create_table(u'owl_tabledegree', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', max_length=400)),
            ('question', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['owl.Question'])),
            ('cdate', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'owl', ['TableDegree'])

        # Adding model 'UserOption'
        db.create_table(u'owl_useroption', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('option', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['owl.Option'])),
            ('cdate', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'owl', ['UserOption'])

        # Adding model 'UserWR'
        db.create_table(u'owl_userwr', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['owl.Question'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('wr', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['owl.WrittenResponse'])),
            ('cdate', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'owl', ['UserWR'])

        # Adding model 'UserTD'
        db.create_table(u'owl_usertd', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', max_length=400)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('td', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['owl.TableDegree'])),
            ('cdate', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'owl', ['UserTD'])


    def backwards(self, orm):
        # Deleting model 'Cities'
        db.delete_table(u'owl_cities')

        # Deleting model 'SocialData'
        db.delete_table(u'owl_socialdata')

        # Deleting model 'Audience'
        db.delete_table(u'owl_audience')

        # Deleting model 'Users'
        db.delete_table(u'owl_users')

        # Removing M2M table for field audience on 'Users'
        db.delete_table(db.shorten_name(u'owl_users_audience'))

        # Deleting model 'Survey'
        db.delete_table(u'owl_survey')

        # Removing M2M table for field audience on 'Survey'
        db.delete_table(db.shorten_name(u'owl_survey_audience'))

        # Deleting model 'Question'
        db.delete_table(u'owl_question')

        # Deleting model 'Option'
        db.delete_table(u'owl_option')

        # Deleting model 'WrittenResponse'
        db.delete_table(u'owl_writtenresponse')

        # Deleting model 'TableDegree'
        db.delete_table(u'owl_tabledegree')

        # Deleting model 'UserOption'
        db.delete_table(u'owl_useroption')

        # Deleting model 'UserWR'
        db.delete_table(u'owl_userwr')

        # Deleting model 'UserTD'
        db.delete_table(u'owl_usertd')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'owl.audience': {
            'Meta': {'object_name': 'Audience'},
            'cdate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '400'})
        },
        u'owl.cities': {
            'Meta': {'object_name': 'Cities'},
            'cdate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '15'})
        },
        u'owl.option': {
            'Meta': {'object_name': 'Option'},
            'cdate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '400'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['owl.Question']"})
        },
        u'owl.question': {
            'Meta': {'object_name': 'Question'},
            'cdate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'max_limit': ('django.db.models.fields.SmallIntegerField', [], {'blank': 'True'}),
            'question': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '400'}),
            'question_type': ('django.db.models.fields.CharField', [], {'default': "'ST'", 'max_length': '2'}),
            'survey': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['owl.Survey']"})
        },
        u'owl.socialdata': {
            'Meta': {'object_name': 'SocialData'},
            'account_id': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'account_token': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'account_type': ('django.db.models.fields.CharField', [], {'default': "'0'", 'max_length': '1'}),
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'cdate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'owl.survey': {
            'Meta': {'object_name': 'Survey'},
            'audience': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['owl.Audience']", 'symmetrical': 'False'}),
            'cdate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'owl.tabledegree': {
            'Meta': {'object_name': 'TableDegree'},
            'cdate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '400'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['owl.Question']"})
        },
        u'owl.useroption': {
            'Meta': {'object_name': 'UserOption'},
            'cdate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'option': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['owl.Option']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'owl.users': {
            'Meta': {'object_name': 'Users'},
            'audience': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['owl.Audience']", 'symmetrical': 'False'}),
            'been': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'bean'", 'to': u"orm['owl.Cities']"}),
            'birthday': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'cdate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'gender': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jobs': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'}),
            'lives_in': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'live_in'", 'to': u"orm['owl.Cities']"}),
            'phone': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '11', 'null': 'True', 'blank': 'True'}),
            'profile_photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'school': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'owl.usertd': {
            'Meta': {'object_name': 'UserTD'},
            'cdate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '400'}),
            'td': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['owl.TableDegree']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'owl.userwr': {
            'Meta': {'object_name': 'UserWR'},
            'cdate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['owl.Question']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'wr': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['owl.WrittenResponse']"})
        },
        u'owl.writtenresponse': {
            'Meta': {'object_name': 'WrittenResponse'},
            'cdate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '400'})
        }
    }

    complete_apps = ['owl']