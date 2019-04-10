#!/usr/bin/python3
# -*- coding:utf-8 -*- 
# @author FH
# @email: capricorn1203@126.com
# @time: 2019/3/15 19:39
"""doctest
    >> import shelve
    >> db = shelve.open(DB_NAME)
    >> if CONFERENCE not in db:
    ...     load(db)
    ...

    >> DbRecord.set_db(db)
    >> event = DbRecord.fetch('event.33950')
    >> event
    <Event 'There *Will* Be Bugs'>
    >> event.venue
    <DbRecord serial='venue.1449'>
    >> event.venue.name
    'Portland 251'
    >> for spkr in event.speakers:
    ... print('{0.serial}: {0.name}'.format(spkr))
    ...
    speaker.3471: Anna Martelli Ravenscroft
    speaker.5199: Alex Martelli
"""
import warnings
import inspect

import ch19_osconfeed as osconfeed

DB_NAME = 'E:\wksp\\fluent_python_examples\chapter_19\data\schedule2.db'
CONFERENCE = 'conference.115'


class Record:

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __eq__(self, other):
        if isinstance(other, Record):
            return self.__dict__ == other.__dict__
        else:
            raise NotImplemented


class MissingDatabaseError(RuntimeError):
    """"""


class DbRecord(Record):

    __db = None

    @staticmethod
    def set_db(db):
        DbRecord.__db = db

    @staticmethod
    def get_db():
        return DbRecord.__db

    @classmethod
    def fetch(cls, ident):
        db = cls.get_db()
        try:
            return db[ident]
        except TypeError:
            if db is None:
                msg = "database not set; call '{}.set_db(my_db)'"
                raise MissingDatabaseError(msg.format(cls.__name__))
            else:
                raise

    def __repr__(self):
        if hasattr(self, 'serial'):
            cls_name = self.__class__.__name__
            return '<{} serial={!r}>'.format(cls_name, self.serial)
        else:
            super().__repr__()


class Event(DbRecord):

    @property
    def venue(self):
        key = 'venue.{}'.format(self.venue_serial)
        return self.__class__.fetch(key)

    @property
    def speakers(self):
        if not hasattr(self, '_speaker_objs'):
            spk_serials = self.__dict__['speakers']
            fetch = self.__class__.fetch
            self._speaker_objs = [fetch('speaker.{}'.format(key)) for key in spk_serials]
        return self._speaker_objs

    def __repr__(self):
        if hasattr(self, 'name'):
            cls_name = self.__class__.__name__
            return '<{} serial={!r}>'.format(cls_name, self.name)
        else:
            super().__repr__()


def load_db(db):
    raw_feed = osconfeed.load()
    warnings.warn('loading ' + DB_NAME)
    for collection, rec_list in raw_feed['Schedule'].items():
        record_type = collection[:-1]
        cls_name = record_type.capitalize()
        cls = globals().get(cls_name, DbRecord)

        if isinstance(cls, DbRecord) or issubclass(cls, Record):
            factory = cls
        else:
            factory = DbRecord

        for record in rec_list:
            key = '{}.{}'.format(record_type, record['serial'])
            record['serial'] = key
            db[key] = factory(**record)
