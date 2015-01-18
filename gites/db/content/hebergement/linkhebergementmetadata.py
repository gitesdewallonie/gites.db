# -*- coding: utf-8 -*-
import sqlalchemy as sa
from affinitic.db import mapper
from gites.db.mapper import GitesMappedClassBase
from gites.db.content.hebergement.hebergement import Hebergement
from gites.db.content.hebergement.metadata import Metadata


class LinkHebergementMetadata(GitesMappedClassBase):
    """
    Table de jointure permettant de gérer les métadata d'un hébergement
    """

    __tablename__ = u'link_hebergement_metadata'

    link_met_pk = sa.Column('link_met_pk', sa.Integer,
                            nullable=False,
                            primary_key=True,
                            unique=True,
                            doc=u"Numéro d'identifiant")

    heb_fk = sa.Column('heb_fk', sa.Integer(),
                       sa.ForeignKey('hebergement.heb_pk'),
                       nullable=False,
                       doc=u"Numéro d'identifiant unique vers la table hébergement")

    metadata_fk = sa.Column('metadata_fk', sa.Integer(),
                            sa.ForeignKey('metadata.met_pk'),
                            nullable=False,
                            doc=u"Numéro d'identifiant unique vers la table métadata")

    link_met_value = sa.Column('link_met_value', sa.Boolean(),
                               default=False,
                               doc=u"???")

    @mapper.Relation
    def metadata_info(cls):
        return sa.orm.relation(Metadata, lazy=False)

    @mapper.Relation
    def hebergement(cls):
        return sa.orm.relation(Hebergement, lazy=True)

    @classmethod
    def get_metadata(cls, heb_pk, language, value=None, editable=None,
                     type=None):
        """ Returns the associated metadata to the hebergement """
        from gites.db.content.hebergement.metadata import Metadata
        title_column = u'met_titre_fr'
        if hasattr(cls, u'met_titre_%s' % language):
            title_column = u'met_titre_%s' % language
        query = cls._session().query(
            cls.metadata_fk.label('pk'),
            cls.link_met_value.label('value'),
            Metadata.met_id.label('id'),
            getattr(Metadata, title_column).label('title'))
        query = query.join('metadata_info')
        query = query.filter(cls.heb_fk == heb_pk)
        if editable is not None:
            query = query.filter(Metadata.met_editable == editable)
        if type is not None:
            query = query.filter(Metadata.metadata_type_id == type)
        if value is not None:
            query = query.filter(cls.link_met_value == value)
        return query.all()
