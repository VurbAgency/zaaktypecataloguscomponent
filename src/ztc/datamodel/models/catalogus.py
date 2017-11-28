from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Catalogus(models.Model):
    """
    De verzameling van ZAAKTYPEn - incl. daarvoor relevante objecttypen - voor
    een Domein die als één geheel beheerd wordt.

    Toelichting objecttype
    Voor de inzet van de CATALOGUS in één uitvoerende organisatie (bijv. een gemeente) gaat
    KING ervan uit dat binnen de organisatie één CATALOGUS wordt gebruikt met alle ZAAKTYPEn
    van de organisatie. De unieke identificatie in dit voorbeeld wordt dan de combinatie van het
    Domein 'Gemeente', gevolgd door het RSIN van de betreffende gemeente. Standaardiserende
    organisaties zullen mogelijk meerdere catalogi willen publiceren en beheren. Denk aan een
    ministerie dat voor meerdere sectoren een CATALOGUS aanlegt. Via het Domein-attribuut
    krijgt zo elke CATALOGUS toch een unieke identificatie.
    KING bepaalt niet op voorhand welke waarden 'Domein' kan aannemen, maar registreert wel
    alle gebruikte waarden
    """
    mnemonic = 'CAT'

    domein = models.CharField(  # waardenverzameling hoofdletters
        _('domein'), max_length=5, validators=[RegexValidator('^[A-Z]*$')],
        help_text=_('Een afkorting waarmee wordt aangegeven voor welk domein in een CATALOGUS'))
    # rsin is gespecificeerd als N9, ivm voorloopnullen gekozen voor CharField. Geen waardenverzameling gedefinieerd
    rsin = models.CharField(
        _('rsin'), max_length=9, help_text=_('Het door een kamer toegekend uniek nummer voor de INGESCHREVEN '
                                             'NIET-NATUURLIJK PERSOON die de eigenaar is van een CATALOGUS.'))
    contactpersoon_beheer_naam = models.CharField(
        _('contactpersoon beheer naam'), max_length=40,
        help_text=_('De naam van de contactpersoon die verantwoordelijk is voor het beheer van de CATALOGUS.'))
    contactpersoon_beheer_telefoonnummer = models.CharField(
        _('contactpersoon beheer telefoonnummer'), max_length=20, blank=True, null=True,
        help_text=_('Het telefoonnummer van de contactpersoon die verantwoordelijk is voor het beheer van de CATALOGUS.'))
    contactpersoon_beheer_emailadres = models.EmailField(  # specificatie waardenverzameling conform RFC 5321 en RFC 5322
        _('contactpersoon beheer emailadres'), max_length=254, blank=True, null=True,
        help_text=_('Het emailadres van de contactpersoon die verantwoordelijk is voor het beheer van de CATALOGUS.'))

    class Meta:
        unique_together = ('domein', 'rsin')
