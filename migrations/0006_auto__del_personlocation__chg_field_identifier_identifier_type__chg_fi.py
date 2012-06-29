# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting model 'PersonLocation'
        db.delete_table('person_personlocation')

        # Changing field 'Identifier.identifier_type'
        db.alter_column('person_identifier', 'identifier_type_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['person.IdentifierType'], null=True))

        # Changing field 'Identifier.person'
        db.alter_column('person_identifier', 'person_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['person.Person'], null=True))

        # Changing field 'Identifier.identifier'
        db.alter_column('person_identifier', 'identifier', self.gf('django.db.models.fields.CharField')(max_length=150, null=True))


    def backwards(self, orm):
        
        # Adding model 'PersonLocation'
        db.create_table('person_personlocation', (
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['person.Person'], null=True, blank=True)),
            ('area_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['simple_locations.Area'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('person', ['PersonLocation'])

        # Changing field 'Identifier.identifier_type'
        db.alter_column('person_identifier', 'identifier_type_id', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['person.IdentifierType']))

        # Changing field 'Identifier.person'
        db.alter_column('person_identifier', 'person_id', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['person.Person']))

        # Changing field 'Identifier.identifier'
        db.alter_column('person_identifier', 'identifier', self.gf('django.db.models.fields.CharField')(default=None, max_length=150))


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
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'e128b722-ff18-4eaa-b3af-b42f1779200f'", 'unique': 'True', 'max_length': '36', 'primary_key': 'True', 'db_index': 'True'}),
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
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'022e143f-a024-4206-b587-e7151be65031'", 'unique': 'True', 'max_length': '36', 'primary_key': 'True', 'db_index': 'True'}),
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
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'ec4427d2-47dd-4975-a13b-370b89cafb33'", 'unique': 'True', 'max_length': '36', 'primary_key': 'True', 'db_index': 'True'}),
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
            'identifier': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'identifier_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['person.IdentifierType']", 'null': 'True', 'blank': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['person.Person']", 'null': 'True', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'9a347cc4-3dca-4da7-94d8-5cb87d51a9e9'", 'unique': 'True', 'max_length': '36', 'primary_key': 'True', 'db_index': 'True'}),
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
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'2515932b-8ff1-45b0-9280-cec20683d86e'", 'unique': 'True', 'max_length': '36', 'primary_key': 'True', 'db_index': 'True'}),
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
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'620e4ae8-faca-4d6a-b5a9-562a0b54a125'", 'unique': 'True', 'max_length': '36', 'primary_key': 'True', 'db_index': 'True'}),
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
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'8ef95c30-e7e1-4106-9891-baf305f5b7ec'", 'unique': 'True', 'max_length': '36', 'primary_key': 'True', 'db_index': 'True'}),
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
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'607627ad-33be-48d7-be88-403392a69851'", 'unique': 'True', 'max_length': '36', 'primary_key': 'True', 'db_index': 'True'}),
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
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'d7d1a319-f47f-4975-bf76-b1c14ebed7c4'", 'unique': 'True', 'max_length': '36', 'primary_key': 'True', 'db_index': 'True'}),
            'void_reason': ('django.db.models.fields.CharField', [], {'max_length': '765', 'blank': 'True'}),
            'voided': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'voided_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'relationtype_voided_by_related'", 'null': 'True', 'to': "orm['auth.User']"})
        }
    }

    complete_apps = ['person']
