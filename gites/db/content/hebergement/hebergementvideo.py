# -*- coding: utf-8 -*-
import sqlalchemy as sa
from affinitic.db import mapper
from gites.db.mapper import GitesMappedClassBase
from gites.db.content.hebergement.hebergement import Hebergement


class HebergementVideo(GitesMappedClassBase):
    """
    Table permettant de gérer les vidéos des hébergements ???
    """

    __tablename__ = u'hebergement_video'

    heb_vid_pk = sa.Column('heb_vid_pk', sa.Integer,
                           primary_key=True,
                           doc=u"Identifiant unique pour une vidéo d'un hébergement ???")

    heb_vid_url = sa.Column('heb_vid_url', sa.String(),
                            doc=u"URL de la vidéo")

    heb_vid_date = sa.Column('heb_vid_date', sa.Date(),
                             default=sa.func.current_timestamp(),
                             doc=u"Date de la vidéo ???")

    heb_vid_heb_fk = sa.Column('heb_vid_heb_fk', sa.Integer,
                               sa.ForeignKey('hebergement.heb_pk'),
                               doc=u"Numéro d'identifiant unique vers la table hébergement")

    @mapper.Relation
    def hebergement(cls):
        return sa.orm.relation(Hebergement,
                               lazy=True,
                               uselist=False,
                               backref=sa.orm.backref('video', uselist=False))
