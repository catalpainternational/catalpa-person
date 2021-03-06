# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Person.deathdate'
        db.alter_column('person_person', 'deathdate', self.gf('django.db.models.fields.DateField')(null=True))


    def backwards(self, orm):
        
        # Changing field 'Person.deathdate'
        db.alter_column('person_person', 'deathdate', self.gf('django.db.models.fields.DateField')(default=None))


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
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'4c65b2c1-6a2b-41c5-827d-0e95503d0c96'", 'unique': 'True', 'max_length': '36', 'primary_key': 'True', 'db_index': 'True'}),
            'void_reason': ('django.db.models.fields.CharField', [], {'max_length': '765', 'blank': 'True'}),
            'voided': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'voided_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'address_voided_by_related'", 'null': 'True', 'to': "orm['auth.User']"})
        },
        'person.contact': {
            'Meta': {'object_name': 'Contact'},
            'changed_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'contact_changed_by_related'", 'null': 'True', 'to': "orm['auth.User']"}),
            'contact_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['person.ContactType']", 'null': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'contact_creator_related'", 'null': 'True', 'to': "orm['auth.User']"}),
            'date_changed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_voided': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'detail': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['person.Person']", 'null': 'True', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'aa15f54b-1091-4dab-83b1-2947b93f426e'", 'unique': 'True', 'max_length': '36', 'primary_key': 'True', 'db_index': 'True'}),
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
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'9b4c7bc9-f0e8-4092-94f1-91773bd4d3a9'", 'unique': 'True', 'max_length': '36', 'primary_key': 'True', 'db_index': 'True'}),
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
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'8e300fc0-f44f-4b85-aa1a-63816eca97a1'", 'unique': 'True', 'max_length': '36', 'primary_key': 'True', 'db_index': 'True'}),
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
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'c01f2560-752e-4715-8b7a-73d5ff686c46'", 'unique': 'True', 'max_length': '36', 'primary_key': 'True', 'db_index': 'True'}),
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
            'deathdate': ('django.db.models.fields.DateField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'916c6db7-102b-46df-9b1d-d3d172f4b44e'", 'unique': 'True', 'max_length': '36', 'primary_key': 'True', 'db_index': 'True'}),
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
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'e2ad1025-fc73-4a32-b4c6-d94d6ad2d9ea'", 'unique': 'True', 'max_length': '36', 'primary_key': 'True', 'db_index': 'True'}),
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
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'c43119e0-8e16-4aab-8bbc-908fe12889c4'", 'unique': 'True', 'max_length': '36', 'primary_key': 'True', 'db_index': 'True'}),
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
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'e3d1f6cc-914f-42f5-92db-bb12ff313885'", 'unique': 'True', 'max_length': '36', 'primary_key': 'True', 'db_index': 'True'}),
            'void_reason': ('django.db.models.fields.CharField', [], {'max_length': '765', 'blank': 'True'}),
            'voided': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'voided_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'relationtype_voided_by_related'", 'null': 'True', 'to': "orm['auth.User']"})
        }
    }

    complete_apps = ['person']
