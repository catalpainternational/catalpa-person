from datetime import datetime

from django.contrib import admin
from django.utils.translation import ugettext as _

from person import models

from lib.autocomplete_admin import FkAutocompleteAdmin, InlineAutocompleteAdmin


class ContactAdmin(admin.TabularInline):
    model = models.Contact
    extra = 1


class ContactTypeAdmin(admin.ModelAdmin):
    model = models.ContactType


class IdentifierAdmin(admin.TabularInline):
    model = models.Identifier
    extra = 1


class IdentifierTypeAdmin(admin.ModelAdmin):
    model = models.IdentifierType


class RelationAdmin(InlineAutocompleteAdmin):
    model = models.Relation
    fk_name = 'person'
    related_search_fields = {'relation': ('name__given_name','name__family_name','name__family_name2'),}
    extra = 1


class RelationTypeAdmin(admin.ModelAdmin):
    model = models.RelationType

    def save_model(self, request, obj, form, change):
        super(RelationTypeAdmin, self).save_model(request, obj, form, change)
        inverse_relation_id = request.POST.get('inverse_relation')

        try: 
            #import pdb; pdb.set_trace()       
            inverse_relation = self.model.objects.get(id=inverse_relation_id)
            inverse_relation.inverse_relation = obj
            inverse_relation.save()
        except ValueError:
            pass
            

class PersonNameAdmin(Admin, admin.TabularInline):
    model = models.PersonName
    fields = ['given_name', 'family_name',]
    max_num = 1

class PersonAddressAdmin(Admin, admin.TabularInline):
    model = models.PersonAddress
    max_num = 1


class PersonAdmin(Admin, FkAutocompleteAdmin):
    model = models.Person
    fields = ['gender', 'birthdate', 'birthdate_estimated','deathdate',]
    search_fields = ['personname__given_name','personname__family_name',]


    inlines = [
                #PersonNameAdmin,
                #PersonAddressAdmin,
                #IdentifierAdmin,
                #ContactAdmin,
                #RelationAdmin,
              ]

    
    def save_formset(self, request, form, formset, change):
            instances = formset.save(commit=False)
            for instance in instances:
                if instance.__class__ == models.Relation:
                    try:
                        relative = ''
                        if instance.person.relatives.filter(uuid=instance.relation.uuid).count() == 0:
                            relative = models.Relation()
                        else:
                            relative = instance.person.relatives.get(uuid=instance.relation.uuid)
                        relative.person = instance.relation
                        relative.relation = instance.person
                        relative.relation_type = instance.relation_type.inverse_relation
                        relative.creator = request.user
                        relative.date_created = datetime.now()
                        relative.save()
                    except:
                        pass
                instance.creator = request.user
                instance.date_created = datetime.now()
                instance.save()
            formset.save_m2m()


admin.site.register(models.ContactType, ContactTypeAdmin)
admin.site.register(models.IdentifierType, IdentifierTypeAdmin)
admin.site.register(models.RelationType, RelationTypeAdmin)
admin.site.register(models.Person, PersonAdmin)
