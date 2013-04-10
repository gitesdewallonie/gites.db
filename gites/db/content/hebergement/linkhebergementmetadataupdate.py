# -*- coding: utf-8 -*-
import sqlalchemy as sa
from gites.db.mapper import GitesMappedClassBase
from gites.db.content.hebergement.linkhebergementmetadata import \
    LinkHebergementMetadata
from gites.db.content.hebergement.metadata import Metadata


class LinkHebergementMetadataUpdate(GitesMappedClassBase):
    __tablename__ = u"link_hebergement_metadata_update"

    pk = sa.Column('pk', sa.Integer, nullable=False, primary_key=True,
                   unique=True)

    link_met_fk = sa.Column('link_met_fk', sa.Integer(),
                            sa.ForeignKey('link_hebergement_metadata.link_met_pk'),
                            nullable=False)

    metadata_fk = sa.Column('metadata_fk', sa.Integer(),
                            sa.ForeignKey('metadata.met_pk'),
                            nullable=False)

    link_met_value = sa.Column('link_met_value', sa.Boolean(), default=False)

    update_date = sa.Column('update_date', sa.DateTime(),
                            default=sa.func.current_timestamp())

    @classmethod
    def __declare_last__(cls):
        cls.link_metadata = sa.orm.relation(LinkHebergementMetadata,
                                            lazy=False)
        cls.metadata_info = sa.orm.relation(Metadata, lazy=False)

    @classmethod
    def get_updates(cls, heb_pk):
        query = cls._session().query(cls).join('link_metadata').filter(
            LinkHebergementMetadata.heb_fk == heb_pk)
        return query.all()
