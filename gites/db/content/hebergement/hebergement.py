# -*- coding: utf-8 -*-
"""
gites.db

Licensed under the GPL license, see LICENCE.txt for more details.
Copyright by Affinitic sprl

$Id: event.py 67630 2006-04-27 00:54:03Z jfroche $
"""
import sqlalchemy
import geoalchemy
from geoalchemy.postgis import PGComparator
from zope.interface import implements
from affinitic.db import mapper
from affinitic.db.cache import FromCache
from gites.db.content.hebergement.metadata import Metadata
from gites.db.content.charge import Charge
from gites.db.content.proprio.proprio import Proprio
from gites.db.content.hebergement.typehebergement import TypeHebergement
from gites.db.interfaces import IHebergement
from gites.db.mapper import GitesMappedClassBase
from OFS.Traversable import Traversable


class Hebergement(GitesMappedClassBase, Traversable):
    """
    Description d'un hébergement
    """

    implements(IHebergement)
    __tablename__ = u"hebergement"

    heb_pk = sqlalchemy.Column('heb_pk',
                               sqlalchemy.Integer,
                               primary_key=True,
                               doc=u"Identifiant unique pour un hébergement")

    heb_nom = sqlalchemy.Column('heb_nom',
                                sqlalchemy.String(),
                                doc=u"Nom de l'hébergement")

    heb_commercialisation_actif = sqlalchemy.Column('heb_commercialisation_actif',
                                                    sqlalchemy.Boolean(),
                                                    doc=u"Hébergement en mode commercialisation")

    heb_commercialisation_id = sqlalchemy.Column('heb_commercialisation_id',
                                                 sqlalchemy.String(),
                                                 doc=u"Identifiant pour la commercialisation")

    heb_code_cgt = sqlalchemy.Column('heb_code_cgt',
                                     sqlalchemy.String(),
                                     doc=u"Code CGT de l'hébergement")

    heb_url = sqlalchemy.Column('heb_url',
                                sqlalchemy.String(),
                                doc=u"Url du site privé de l'hébergement")

    heb_cgt_cap_max = sqlalchemy.Column('heb_cgt_cap_max',
                                        sqlalchemy.Integer(),
                                        doc=u"Capacité maximale de l'hébergement")

    heb_code_gdw = sqlalchemy.Column('heb_code_gdw',
                                     sqlalchemy.String(),
                                     doc=u"Code GDW de l'hébergement")

    heb_site_public = sqlalchemy.Column('heb_site_public',
                                        sqlalchemy.String(),
                                        doc=u"Hébergement publié sur le site GDW  (oui/non")

    heb_charge_fk = sqlalchemy.Column('heb_charge_fk',
                                      sqlalchemy.Integer,
                                      sqlalchemy.ForeignKey('charge.cha_pk'),
                                      doc=u"Type de charge")

    heb_com_fk = sqlalchemy.Column('heb_com_fk',
                                   sqlalchemy.Integer,
                                   sqlalchemy.ForeignKey('commune.com_pk'),
                                   doc=u"Commune de l'hébergement")

    heb_typeheb_fk = sqlalchemy.Column('heb_typeheb_fk',
                                       sqlalchemy.Integer,
                                       sqlalchemy.ForeignKey('type_heb.type_heb_pk'),
                                       doc=u"Type de l'hébergement")

    heb_pro_fk = sqlalchemy.Column('heb_pro_fk',
                                   sqlalchemy.Integer,
                                   sqlalchemy.ForeignKey('proprio.pro_pk'),
                                   doc=u"Propriétaire de l'hébergement")

    heb_calendrier_proprio = sqlalchemy.Column('heb_calendrier_proprio',
                                               sqlalchemy.String(),
                                               doc=u"Etat du calendrier du proprio (actif / non-actif / bloqué)")

    heb_calendrier_proprio_date_maj = sqlalchemy.Column('heb_calendrier_proprio_date_maj',
                                                        sqlalchemy.Date,
                                                        doc=u"Date de la dernière mise à jour du calendrier par le proprio")

    heb_desactivation_alloch = sqlalchemy.Column('heb_desactivation_alloch',
                                                 sqlalchemy.Boolean(),
                                                 default=False,
                                                 doc=u"Désactivation de l'application Allo Chambre Hôte (t/f)")

    heb_gps_lat = sqlalchemy.Column('heb_gps_lat',
                                    sqlalchemy.Float(),
                                    doc=u"Coordonnées GPS en latitude")

    heb_gps_long = sqlalchemy.Column('heb_gps_long',
                                     sqlalchemy.Float(),
                                     doc=u"Coordonnées GPS en longitude")

    heb_location = geoalchemy.GeometryColumn('heb_location',
                                             geoalchemy.Geometry(dimension=2, srid=3447),
                                             comparator=PGComparator,
                                             doc=u"Gélocalisation de l'hébergement")

    heb_groupement_pk = sqlalchemy.Column('heb_groupement_pk',
                                          sqlalchemy.Integer(),
                                          doc=u"Identifiant unique pour un groupement d'hébergement")

    heb_tarif_charge = sqlalchemy.Column('heb_tarif_charge',
                                         sqlalchemy.String(),
                                         doc=u"Charge de l'hébergement")

    @property
    def REQUEST(self):
        from zope.globalrequest import getRequest
        request = getRequest()
        return request

    def Title(self):
        language = self.REQUEST.get('LANGUAGE', 'en')
        typeHeb = self.type.getTitle(language)
        return u"%s - %s - %s" % (typeHeb, self.heb_nom, self.heb_localite)

    def getUrl(self):
        return self.REQUEST.ACTUAL_URL

    def getVignette(self):
        return "%s00.jpg" % (self.heb_code_gdw)

    def getProprioName(self):
        return self.proprio.pro_nom1

    proprioName = property(getProprioName)

    def getMaisonTourisme(self):
        return self.maisonTourisme[0]

    def getSituation(self, languageCode):
        if 'fr' in languageCode:
            return self.heb_pointfort_fr
        elif 'nl' in languageCode:
            return self.heb_pointfort_nl
        elif 'it' in languageCode:
            return self.heb_pointfort_it
        elif 'de' in languageCode:
            return self.heb_pointfort_de
        else:
            return self.heb_pointfort_uk

    def getDescription(self, languageCode):
        if 'fr' in languageCode:
            return self.heb_descriptif_fr
        elif 'nl' in languageCode:
            return self.heb_descriptif_nl
        elif 'it' in languageCode:
            return self.heb_descriptif_it
        elif 'de' in languageCode:
            return self.heb_descriptif_de
        else:
            return self.heb_descriptif_uk

    def getDistribution(self, languageCode):
        if 'fr' in languageCode:
            return self.heb_distribution_fr
        elif 'nl' in languageCode:
            return self.heb_distribution_nl
        elif 'it' in languageCode:
            return self.heb_distribution_it
        elif 'de' in languageCode:
            return self.heb_distribution_de
        else:
            return self.heb_distribution_uk

    def getSeminaireVert(self, languageCode):
        if 'fr' in languageCode:
            return self.heb_seminaire_vert_fr
        elif 'nl' in languageCode:
            return self.heb_seminaire_vert_nl
        elif 'it' in languageCode:
            return self.heb_seminaire_vert_it
        elif 'de' in languageCode:
            return self.heb_seminaire_vert_de
        else:
            return self.heb_seminaire_vert_uk

    def _get_metadata(self, metadata_id):
        from gites.db.content.hebergement.linkhebergementmetadata import LinkHebergementMetadata
        query = self.session.query(LinkHebergementMetadata.link_met_value)
        query = query.options(FromCache('gdw'))
        query = query.join('hebergement').join('metadata_info')
        query = query.filter(Hebergement.heb_pk == self.heb_pk)
        return query.filter(Metadata.met_id == metadata_id).scalar()

    def epis_nombre(self):
        from gites.db.content import LinkHebergementEpis
        query = self.session.query(LinkHebergementEpis.heb_nombre_epis)
        query = query.options(FromCache('gdw'))
        query = query.filter_by(heb_pk=self.heb_pk)
        query = query.limit(1)
        return query.scalar()

    @property
    def heb_nombre_epis(self):
        return self.epis_nombre()

    def is_smoker(self):
        return self._get_metadata('heb_fumeur')

    @property
    def heb_fumeur(self):
        return self.is_smoker()

    def accept_dogs(self):
        return self._get_metadata('heb_animal')

    @property
    def heb_animal(self):
        return self.accept_dogs()

    @mapper.Relation
    def type(cls):
        return sqlalchemy.orm.relation(TypeHebergement, lazy=True)

    @mapper.Relation
    def proprio(cls):
        return sqlalchemy.orm.relation(Proprio, lazy=True,
                                       backref='hebergements')

    @mapper.RelationImport('gites.db.content:ReservationProprio')
    @mapper.Relation
    def reservations(cls, ReservationProprio):
        return sqlalchemy.orm.relation(ReservationProprio, lazy=True,
                                       backref='hebergement')

    @mapper.Relation
    def charge(cls):
        return sqlalchemy.orm.relation(Charge, lazy=True)

    @mapper.RelationImport('gites.db.content:Commune')
    @mapper.Relation
    def commune(cls, Commune):
        return sqlalchemy.orm.relation(Commune, lazy=True)

    @mapper.RelationImport('gites.db.content:LinkHebergementEpis')
    @mapper.Relation
    def epis(cls, LinkHebergementEpis):
        return sqlalchemy.orm.relation(LinkHebergementEpis, lazy=True)

    @mapper.RelationImport('gites.db.content:Province',
                           'gites.db.content:Commune')
    @mapper.Relation
    def province(cls, Province, Commune):
        return sqlalchemy.orm.relation(Province,
                                       secondary=Commune.__tablename__,
                                       lazy=True)

    @mapper.RelationImport('gites.db.content:MaisonTourisme',
                           'gites.db.content:Commune')
    @mapper.Relation
    def maisonTourisme(cls, MaisonTourisme, Commune):
        return sqlalchemy.orm.relation(MaisonTourisme,
                                       secondary=Commune.__tablename__,
                                       lazy=True)

    @mapper.RelationImport('gites.db.content:Metadata',
                           'gites.db.content:LinkHebergementMetadata')
    @mapper.Relation
    def activeMetadatas(cls, Metadata, LinkHebergementMetadata):
        return sqlalchemy.orm.relation(
            Metadata,
            secondary=LinkHebergementMetadata.__tablename__,
            primaryjoin=sqlalchemy.and_(
                cls.heb_pk == LinkHebergementMetadata.heb_fk,
                LinkHebergementMetadata.link_met_value == True),
            lazy=True)

    @property
    def heb_gid_access_tous(self):
        return self._get_metadata('heb_gid_access_tous')

    @mapper.RelationImport('gites.db.content:Metadata',
                           'gites.db.content:LinkHebergementMetadata')
    @mapper.Relation
    def metadatas(cls, Metadata, LinkHebergementMetadata):
        return sqlalchemy.orm.relation(
            Metadata,
            secondary=LinkHebergementMetadata.__tablename__,
            primaryjoin=(cls.heb_pk == LinkHebergementMetadata.heb_fk),
            lazy=True)

    @classmethod
    def get_last_changes(cls, date, session=None, cgt_not_empty=False):
        """Return the modified lines since the given date"""
        if not session:
            session = cls._session()
        query = session.query(cls)
        query = query.filter(cls.heb_date_modification >= date)
        if cgt_not_empty:
            query = query.filter(cls.heb_code_cgt != u'')
        return query.all()
