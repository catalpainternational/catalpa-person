from django.db import models
from django.utils.translation import ugettext_lazy as _

# where does address come from ????
#from location.models import Address
from aihun.models import Model, ModelType


GENDER_CHOICES = (
        ('M', _('Male')),
        ('F', _('Female')),
    )


class Person(Model):
    gender = models.CharField(_('gender'), max_length=1, choices=GENDER_CHOICES)
    birthdate = models.DateField(_('birthdate'), db_index=True)
    birthdate_estimated = models.BooleanField(_('birthdate estimated'))
    deathdate = models.DateField(_('date of death'), db_index=True, null=True, blank=True,)
    
    class Meta:
        verbose_name = _('person')
        verbose_name_plural = _('persons')
        
    def __unicode__(self,):
        if self.name is not None:
            return u"%s, %s, %s" % (self.name, self.gender, self.birthdate)
        else:
            return u"%s, %s" % (self.gender, self.birthdate,)
    
    
class PersonName(Model):
    person = models.OneToOneField(Person, null=True, blank=True, verbose_name=_('person'), related_name='name')
    #preferred = models.BooleanField(_('preferred'))
    prefix = models.CharField(_('prefix'), max_length=150, blank=True)
    given_name = models.CharField(_('first name'), max_length=150, db_index=True)
    middle_name = models.CharField(_('middle name'), max_length=150, blank=True)
    family_name_prefix = models.CharField(_('family name prefix'), max_length=150, blank=True)
    family_name = models.CharField(_('family name'), max_length=150, blank=True, db_index=True)
    family_name2 = models.CharField(_('second family name'), max_length=150, blank=True, db_index=True)
    family_name_suffix = models.CharField(_('family name suffix'), max_length=150, blank=True)
    degree = models.CharField(_('degree'), max_length=150, blank=True)
    
    class Meta:
        verbose_name = _("person's name")
        verbose_name_plural = _("person's name")
    
    def __unicode__(self,):
        return u"%s %s %s %s" % (self.given_name, self.middle_name, self.family_name, self.family_name2)


# class PersonAddress(Address):
#     person = models.ForeignKey(Person, null=True, blank=True, verbose_name=_('person'))
#     preferred = models.BooleanField(_('preferred'), blank=True,)
    
#     class Meta:
#         verbose_name = _("person's address")
#         verbose_name_plural = _("person's address")

#     def __unicode__(self,):
#         return u"%s %s %s" % (self.address1, self.city_village, self.state_province,)


class RelationType(ModelType):
    inverse_relation = models.ForeignKey('self', verbose_name=_('inverse relation'), null=True, blank=True)
    
    class Meta:
        verbose_name = _('relation type')
        verbose_name_plural = _('relation types')
    
    def __unicode__(self,):
        return u"%s" % (self.name)


class Relation(Model):
    person = models.ForeignKey(Person, verbose_name=_('person'), null=True, blank=True)   
    relation = models.ForeignKey(Person, verbose_name=_('family member'), related_name=_('relatives'), null=True, blank=True)   
    relation_type = models.ForeignKey(RelationType, verbose_name=_('relation type'), null=True, blank=True)
    
    class Meta:
        verbose_name = _('Family Member')
        verbose_name_plural = _('Family Members')

    def __unicode__(self,):
        try:
           return u"%s is a %s of %s" % (self.relation, self.relation_type.name, self.person)
        except:
           return u'Unspecified Relation'

class ContactType(ModelType):
    class Meta:
        verbose_name = _('contact detail type')
        verbose_name_plural = _('contact detail types')
    
    def __unicode__(self,):
        return u"%s" % (self.name)


class Contact(Model):
    person = models.ForeignKey(Person, verbose_name=_('person'), blank=True, null=True,)   
    contact_type = models.ForeignKey(ContactType, verbose_name=_('contact type'), null=True, blank=True)
    detail = models.CharField(_('detail'), max_length=150, null=True, blank=True)
    
    class Meta:
        verbose_name = _('contact detail')
        verbose_name_plural = _('contact details')

    def __unicode__(self,):
        return u"%s: %s" % (self.person, self.detail)


class IdentifierType(ModelType):
    class Meta:
        verbose_name = _('identifier type')
        verbose_name_plural = _('identifier types')
    
    def __unicode__(self,):
        return u"%s" % (self.name)


class Identifier(Model):
    person = models.ForeignKey(Person, verbose_name=_('person'), blank=True, null=True,)   
    identifier_type = models.ForeignKey(IdentifierType, verbose_name=_('identifier type'), blank=True, null=True,)
    identifier = models.CharField(_('identifier'), max_length=150, blank=True, null=True,)
    
    class Meta:
        verbose_name = _('identifier')
        verbose_name_plural = _('identifiers')

    def __unicode__(self,):
        return u"%s : %s" % (self.identifier_type.name, self.identifier)


