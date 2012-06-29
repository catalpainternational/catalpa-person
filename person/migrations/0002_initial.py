# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Person'
        db.create_table('person_person', (
            ('uuid', self.gf('django.db.models.fields.CharField')(default='c5abeae2-0651-496d-8b95-cc4aa3797d7b', unique=True, max_length=36, primary_key=True, db_index=True)),
            ('creator', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='person_creator_related', null=True, to=orm['auth.User'])),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('changed_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='person_changed_by_related', null=True, to=orm['auth.User'])),
            ('date_changed', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('voided', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('voided_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='person_voided_by_related', null=True, to=orm['auth.User'])),
            ('date_voided', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('void_reason', self.gf('django.db.models.fields.CharField')(max_length=765, blank=True)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('birthdate', self.gf('django.db.models.fields.DateField')(db_index=True)),
            ('birthdate_estimated', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('deathdate', self.gf('django.db.models.fields.DateField')(db_index=True, blank=True)),
        ))
        db.send_create_signal('person', ['Person'])

        # Adding model 'PersonName'
        db.create_table('person_personname', (
            ('uuid', self.gf('django.db.models.fields.CharField')(default='68c2c706-209d-42de-86af-8f5f09cfe561', unique=True, max_length=36, primary_key=True, db_index=True)),
            ('creator', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='personname_creator_related', null=True, to=orm['auth.User'])),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('changed_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='personname_changed_by_related', null=True, to=orm['auth.User'])),
            ('date_changed', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('voided', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('voided_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='personname_voided_by_related', null=True, to=orm['auth.User'])),
            ('date_voided', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('void_reason', self.gf('django.db.models.fields.CharField')(max_length=765, blank=True)),
            ('person', self.gf('django.db.models.fields.related.OneToOneField')(blank=True, related_name='name', unique=True, null=True, to=orm['person.Person'])),
            ('prefix', self.gf('django.db.models.fields.CharField')(max_length=150, blank=True)),
            ('given_name', self.gf('django.db.models.fields.CharField')(max_length=150, db_index=True)),
            ('middle_name', self.gf('django.db.models.fields.CharField')(max_length=150, blank=True)),
            ('family_name_prefix', self.gf('django.db.models.fields.CharField')(max_length=150, blank=True)),
            ('family_name', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=150, blank=True)),
            ('family_name2', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=150, blank=True)),
            ('family_name_suffix', self.gf('django.db.models.fields.CharField')(max_length=150, blank=True)),
            ('degree', self.gf('django.db.models.fields.CharField')(max_length=150, blank=True)),
        ))
        db.send_create_signal('person', ['PersonName'])

        # Adding model 'PersonAddress'
        db.create_table('person_personaddress', (
            ('address_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['location.Address'], unique=True, primary_key=True)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['person.Person'], null=True, blank=True)),
            ('preferred', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('person', ['PersonAddress'])

        # Adding model 'RelationType'
        db.create_table('person_relationtype', (
            ('uuid', self.gf('django.db.models.fields.CharField')(default='38cb4e50-48a7-4055-b808-9ab4e986e359', unique=True, max_length=36, primary_key=True, db_index=True)),
            ('creator', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='relationtype_creator_related', null=True, to=orm['auth.User'])),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('changed_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='relationtype_changed_by_related', null=True, to=orm['auth.User'])),
            ('date_changed', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('voided', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('voided_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='relationtype_voided_by_related', null=True, to=orm['auth.User'])),
            ('date_voided', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('void_reason', self.gf('django.db.models.fields.CharField')(max_length=765, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, db_index=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=765, blank=True)),
            ('inverse_relation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['person.RelationType'], null=True, blank=True)),
        ))
        db.send_create_signal('person', ['RelationType'])

        # Adding model 'Relation'
        db.create_table('person_relation', (
            ('uuid', self.gf('django.db.models.fields.CharField')(default='99b07c3d-a4d2-4ebf-8a31-831b2a483cb0', unique=True, max_length=36, primary_key=True, db_index=True)),
            ('creator', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='relation_creator_related', null=True, to=orm['auth.User'])),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('changed_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='relation_changed_by_related', null=True, to=orm['auth.User'])),
            ('date_changed', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('voided', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('voided_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='relation_voided_by_related', null=True, to=orm['auth.User'])),
            ('date_voided', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('void_reason', self.gf('django.db.models.fields.CharField')(max_length=765, blank=True)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['person.Person'])),
            ('relation', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'relatives', null=True, to=orm['person.Person'])),
            ('relation_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['person.RelationType'], null=True, blank=True)),
        ))
        db.send_create_signal('person', ['Relation'])

        # Adding model 'ContactType'
        db.create_table('person_contacttype', (
            ('uuid', self.gf('django.db.models.fields.CharField')(default='4092a20d-7edb-4ace-8d25-9c2f4e4e45c3', unique=True, max_length=36, primary_key=True, db_index=True)),
            ('creator', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='contacttype_creator_related', null=True, to=orm['auth.User'])),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('changed_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='contacttype_changed_by_related', null=True, to=orm['auth.User'])),
            ('date_changed', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('voided', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('voided_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='contacttype_voided_by_related', null=True, to=orm['auth.User'])),
            ('date_voided', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('void_reason', self.gf('django.db.models.fields.CharField')(max_length=765, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, db_index=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=765, blank=True)),
        ))
        db.send_create_signal('person', ['ContactType'])

        # Adding model 'Contact'
        db.create_table('person_contact', (
            ('uuid', self.gf('django.db.models.fields.CharField')(default='6cac1d9c-09ba-4477-8c9a-51d8b512e9fa', unique=True, max_length=36, primary_key=True, db_index=True)),
            ('creator', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='contact_creator_related', null=True, to=orm['auth.User'])),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('changed_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='contact_changed_by_related', null=True, to=orm['auth.User'])),
            ('date_changed', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('voided', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('voided_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='contact_voided_by_related', null=True, to=orm['auth.User'])),
            ('date_voided', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('void_reason', self.gf('django.db.models.fields.CharField')(max_length=765, blank=True)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['person.Person'], null=True, blank=True)),
            ('contact_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['person.ContactType'])),
            ('detail', self.gf('django.db.models.fields.CharField')(max_length=150)),
        ))
        db.send_create_signal('person', ['Contact'])

        # Adding model 'IdentifierType'
        db.create_table('person_identifiertype', (
            ('uuid', self.gf('django.db.models.fields.CharField')(default='479c8812-9b40-4f93-993a-388b53f2f7de', unique=True, max_length=36, primary_key=True, db_index=True)),
            ('creator', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='identifiertype_creator_related', null=True, to=orm['auth.User'])),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('changed_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='identifiertype_changed_by_related', null=True, to=orm['auth.User'])),
            ('date_changed', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('voided', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('voided_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='identifiertype_voided_by_related', null=True, to=orm['auth.User'])),
            ('date_voided', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('void_reason', self.gf('django.db.models.fields.CharField')(max_length=765, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, db_index=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=765, blank=True)),
        ))
        db.send_create_signal('person', ['IdentifierType'])

        # Adding model 'Identifier'
        db.create_table('person_identifier', (
            ('uuid', self.gf('django.db.models.fields.CharField')(default='fe5eccdd-da25-47ba-9855-e47942b0eeb0', unique=True, max_length=36, primary_key=True, db_index=True)),
            ('creator', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='identifier_creator_related', null=True, to=orm['auth.User'])),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('changed_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='identifier_changed_by_related', null=True, to=orm['auth.User'])),
            ('date_changed', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('voided', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('voided_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='identifier_voided_by_related', null=True, to=orm['auth.User'])),
            ('date_voided', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('void_reason', self.gf('django.db.models.fields.CharField')(max_length=765, blank=True)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['person.Person'])),
            ('identifier_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['person.IdentifierType'])),
            ('identifier', self.gf('django.db.models.fields.CharField')(max_length=150)),
        ))
        db.send_create_signal('person', ['Identifier'])


    def backwards(self, orm):
        
        # Deleting model 'Person'
        db.delete_table('person_person')

        # Deleting model 'PersonName'
        db.delete_table('person_personname')

        # Deleting model 'PersonAddress'
        db.delete_table('person_personaddress')

        # Deleting model 'RelationType'
        db.delete_table('person_relationtype')

        # Deleting model 'Relation'
        db.delete_table('person_relation')

        # Deleting model 'ContactType'
        db.delete_table('person_contacttype')

        # Deleting model 'Contact'
        db.delete_table('person_contact')

        # Deleting model 'IdentifierType'
        db.delete_table('person_identifiertype')

        # Deleting model 'Identifier'
        db.delete_table('person_identifier')


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
        'location.address': {
            'Meta': {'object_name': 'Address'},
            'address1': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'address2': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'changed_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'address_changed_by_related'", 'null': 'True', 'to': "orm['auth.User']"}),
            'city_village': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '150', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '150', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'address_creator_related'", 'null': 'True', 'to': "orm['auth.User']"}),
            'date_changed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_voided': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'postal_code': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '150', 'blank': 'True'}),
            'state_province': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '150', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'05ca2537-a6dd-4408-8d0a-d07a60b9dff0'", 'unique': 'True', 'max_length': '36', 'primary_key': 'True', 'db_index': 'True'}),
            'void_reason': ('django.db.models.fields.CharField', [], {'max_length': '765', 'blank': 'True'}),
            'voided': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'voided_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'address_voided_by_related'", 'null': 'True', 'to': "orm['auth.User']"})
        },
        'person.contact': {
            'Meta': {'object_name': 'Contact'},
            'changed_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'contact_changed_by_related'", 'null': 'True', 'to': "orm['auth.User']"}),
            'contact_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['person.ContactType']"}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'contact_creator_related'", 'null': 'True', 'to': "orm['auth.User']"}),
            'date_changed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_voided': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'detail': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['person.Person']", 'null': 'True', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'7d11d1f3-c45d-4164-b7f5-eccc4233b348'", 'unique': 'True', 'max_length': '36', 'primary_key': 'True', 'db_index': 'True'}),
            'void_reason': ('django.db.models.fields.CharField', [], {'max_length': '765', 'blank': 'True'}),
            'voided': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'voided_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'contact_voided_by_related'", 'null': 'True', 'to': "orm['auth.User']"})
        },
        'person.contacttype': {
            'Meta': {'object_name': 'ContactType'},
            'changed_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'contacttype_changed_by_related'", 'null': 'True', 'to': "orm['auth.User']"}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'contacttype_creator_related'", 'null': 'True', 'to': "orm['auth.User']"}),
            'date_changed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_voided': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '765', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'75ee0516-1e48-4aea-84fe-58da82476c21'", 'unique': 'True', 'max_length': '36', 'primary_key': 'True', 'db_index': 'True'}),
            'void_reason': ('django.db.models.fields.CharField', [], {'max_length': '765', 'blank': 'True'}),
            'voided': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'voided_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'contacttype_voided_by_related'", 'null': 'True', 'to': "orm['auth.User']"})
        },
        'person.identifier': {
            'Meta': {'object_name': 'Identifier'},
            'changed_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'identifier_changed_by_related'", 'null': 'True', 'to': "orm['auth.User']"}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'identifier_creator_related'", 'null': 'True', 'to': "orm['auth.User']"}),
            'date_changed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_voided': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'identifier': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'identifier_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['person.IdentifierType']"}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['person.Person']"}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'1a04ea60-fb04-4b32-aded-f73e6a1b7027'", 'unique': 'True', 'max_length': '36', 'primary_key': 'True', 'db_index': 'True'}),
            'void_reason': ('django.db.models.fields.CharField', [], {'max_length': '765', 'blank': 'True'}),
            'voided': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'voided_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'identifier_voided_by_related'", 'null': 'True', 'to': "orm['auth.User']"})
        },
        'person.identifiertype': {
            'Meta': {'object_name': 'IdentifierType'},
            'changed_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'identifiertype_changed_by_related'", 'null': 'True', 'to': "orm['auth.User']"}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'identifiertype_creator_related'", 'null': 'True', 'to': "orm['auth.User']"}),
            'date_changed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_voided': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '765', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'1d568bb4-00b1-479b-9413-3ee1c7b5c241'", 'unique': 'True', 'max_length': '36', 'primary_key': 'True', 'db_index': 'True'}),
            'void_reason': ('django.db.models.fields.CharField', [], {'max_length': '765', 'blank': 'True'}),
            'voided': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'voided_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'identifiertype_voided_by_related'", 'null': 'True', 'to': "orm['auth.User']"})
        },
        'person.person': {
            'Meta': {'object_name': 'Person'},
            'birthdate': ('django.db.models.fields.DateField', [], {'db_index': 'True'}),
            'birthdate_estimated': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'changed_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'person_changed_by_related'", 'null': 'True', 'to': "orm['auth.User']"}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'person_creator_related'", 'null': 'True', 'to': "orm['auth.User']"}),
            'date_changed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_voided': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'deathdate': ('django.db.models.fields.DateField', [], {'db_index': 'True', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'43022cbc-a5df-4f97-a721-71b453ed02be'", 'unique': 'True', 'max_length': '36', 'primary_key': 'True', 'db_index': 'True'}),
            'void_reason': ('django.db.models.fields.CharField', [], {'max_length': '765', 'blank': 'True'}),
            'voided': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'voided_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'person_voided_by_related'", 'null': 'True', 'to': "orm['auth.User']"})
        },
        'person.personaddress': {
            'Meta': {'object_name': 'PersonAddress', '_ormbases': ['location.Address']},
            'address_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['location.Address']", 'unique': 'True', 'primary_key': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['person.Person']", 'null': 'True', 'blank': 'True'}),
            'preferred': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'person.personname': {
            'Meta': {'object_name': 'PersonName'},
            'changed_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'personname_changed_by_related'", 'null': 'True', 'to': "orm['auth.User']"}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'personname_creator_related'", 'null': 'True', 'to': "orm['auth.User']"}),
            'date_changed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_voided': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'degree': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'family_name': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '150', 'blank': 'True'}),
            'family_name2': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '150', 'blank': 'True'}),
            'family_name_prefix': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'family_name_suffix': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'given_name': ('django.db.models.fields.CharField', [], {'max_length': '150', 'db_index': 'True'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'person': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'name'", 'unique': 'True', 'null': 'True', 'to': "orm['person.Person']"}),
            'prefix': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'a8ee2e8b-7587-4747-9da4-7c474a47bf9c'", 'unique': 'True', 'max_length': '36', 'primary_key': 'True', 'db_index': 'True'}),
            'void_reason': ('django.db.models.fields.CharField', [], {'max_length': '765', 'blank': 'True'}),
            'voided': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'voided_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'personname_voided_by_related'", 'null': 'True', 'to': "orm['auth.User']"})
        },
        'person.relation': {
            'Meta': {'object_name': 'Relation'},
            'changed_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'relation_changed_by_related'", 'null': 'True', 'to': "orm['auth.User']"}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'relation_creator_related'", 'null': 'True', 'to': "orm['auth.User']"}),
            'date_changed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_voided': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['person.Person']"}),
            'relation': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'relatives'", 'null': 'True', 'to': "orm['person.Person']"}),
            'relation_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['person.RelationType']", 'null': 'True', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'7478c4e1-2e22-4f5f-91b2-d0ecc136db8f'", 'unique': 'True', 'max_length': '36', 'primary_key': 'True', 'db_index': 'True'}),
            'void_reason': ('django.db.models.fields.CharField', [], {'max_length': '765', 'blank': 'True'}),
            'voided': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'voided_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'relation_voided_by_related'", 'null': 'True', 'to': "orm['auth.User']"})
        },
        'person.relationtype': {
            'Meta': {'object_name': 'RelationType'},
            'changed_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'relationtype_changed_by_related'", 'null': 'True', 'to': "orm['auth.User']"}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'relationtype_creator_related'", 'null': 'True', 'to': "orm['auth.User']"}),
            'date_changed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_voided': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '765', 'blank': 'True'}),
            'inverse_relation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['person.RelationType']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'d462a4d6-8d67-4c7f-b2f1-f15d81b63b36'", 'unique': 'True', 'max_length': '36', 'primary_key': 'True', 'db_index': 'True'}),
            'void_reason': ('django.db.models.fields.CharField', [], {'max_length': '765', 'blank': 'True'}),
            'voided': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'voided_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'relationtype_voided_by_related'", 'null': 'True', 'to': "orm['auth.User']"})
        }
    }

    complete_apps = ['person']
