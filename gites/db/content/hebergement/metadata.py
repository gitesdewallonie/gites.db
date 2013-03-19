# -*- coding: utf-8 -*-
import sqlalchemy as sa
from gites.db.mapper import GitesMappedClassBase
from gites.db.content.hebergement.metadatatype import MetadataType


class Metadata(GitesMappedClassBase):
    __tablename__ = u'metadata'

    met_pk = sa.Column('met_pk', sa.Integer, nullable=False, primary_key=True,
                       unique=True)

    met_id = sa.Column('met_id', sa.String(), nullable=False)

    met_titre_fr = sa.Column('met_titre_fr', sa.String(), nullable=False)

    met_titre_en = sa.Column('met_titre_en', sa.String(), nullable=False)

    met_titre_nl = sa.Column('met_titre_nl', sa.String(), nullable=False)

    met_titre_it = sa.Column('met_titre_it', sa.String(), nullable=False)

    met_titre_de = sa.Column('met_titre_de', sa.String(), nullable=False)

    met_filterable = sa.Column('met_filterable', sa.Boolean(), default=False)

    met_editable = sa.Column('met_editable', sa.Boolean(), default=False)

    metadata_type_id = sa.Column('metadata_type_id', sa.String(),
                                 sa.ForeignKey('metadata_type.met_typ_id'),
                                 nullable=False)

    @classmethod
    def __declare_last__(cls):
        cls.type = sa.orm.relation(MetadataType)

    def getTitre(self, languageCode):
        if 'fr' in languageCode:
            return self.met_titre_fr
        elif 'nl' in languageCode:
            return self.met_titre_nl
        elif 'it' in languageCode:
            return self.met_titre_it
        elif 'de' in languageCode:
            return self.met_titre_de
        else:
            return self.met_titre_en
