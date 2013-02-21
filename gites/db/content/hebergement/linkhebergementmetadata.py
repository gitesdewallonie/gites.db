# -*- coding: utf-8 -*-
import sqlalchemy as sa
from gites.db.mapper import GitesMappedClassBase
from gites.db.content.hebergement.hebergement import Hebergement
from gites.db.content.hebergement.metadata import Metadata


class LinkHebergementMetadata(GitesMappedClassBase):
    __tablename__ = u'link_hebergement_metadata'

    link_met_pk = sa.Column('link_met_pk', sa.Integer, nullable=False,
                            primary_key=True, unique=True)

    heb_fk = sa.Column('heb_fk', sa.Integer(),
                       sa.ForeignKey('hebergement.heb_pk'),
                       nullable=False)

    metadata_fk = sa.Column('metadata_fk', sa.Integer(),
                            sa.ForeignKey('metadata.met_pk'),
                            nullable=False)

    link_met_value = sa.Column('link_met_value', sa.Boolean(), default=False)

    @classmethod
    def __declare_last__(cls):
        cls.metadata = sa.orm.relation(Metadata, lazy=False),

        cls.hebergement = sa.orm.relation(Hebergement, lazy=True)
