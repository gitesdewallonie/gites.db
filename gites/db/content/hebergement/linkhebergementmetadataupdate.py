# -*- coding: utf-8 -*-
import sqlalchemy as sa
from affinitic.db import mapper
from gites.db.mapper import GitesMappedClassBase
from gites.db.content.hebergement.linkhebergementmetadata import \
    LinkHebergementMetadata
from gites.db.content.hebergement.metadata import Metadata


class LinkHebergementMetadataUpdate(GitesMappedClassBase):
    """
    Table de jointure permettant de gérer les mises à jour des métadatas
    d'un hébergement par son propriétaire ???
    """

    __tablename__ = u"link_hebergement_metadata_update"

    pk = sa.Column('pk', sa.Integer,
                   nullable=False,
                   primary_key=True,
                   unique=True,
                   doc=u"Identifiant unique pour une mise à jour")

    link_met_fk = sa.Column('link_met_fk', sa.Integer(),
                            sa.ForeignKey('link_hebergement_metadata.link_met_pk'),
                            nullable=False,
                            doc=u"Numéro d'identifiant unique vers la table de jointure des métadata d'un hébergement")

    metadata_fk = sa.Column('metadata_fk', sa.Integer(),
                            sa.ForeignKey('metadata.met_pk'),
                            nullable=False,
                            doc=u"Numéro d'identifiant unique vers la table métadata")

    link_met_value = sa.Column('link_met_value', sa.Boolean(),
                               default=False,
                               doc=u"???")

    update_date = sa.Column('update_date', sa.DateTime(),
                            default=sa.func.current_timestamp(),
                            doc=u"Date de la mise à jour")

    @mapper.Relation
    def link_metadata(cls):
        return sa.orm.relation(LinkHebergementMetadata, lazy=False)

    @mapper.Relation
    def metadata_info(cls):
        return sa.orm.relation(Metadata, lazy=False)

    @classmethod
    def get_updates(cls, heb_pk):
        query = cls._session().query(cls).join('link_metadata').filter(
            LinkHebergementMetadata.heb_fk == heb_pk)
        return query.all()
