#!/usr/bin/python3
# -*- coding:utf-8 -*- 
# @author FH
# @email: capricorn1203@126.com
# @time: 2019/3/15 18:38
"""
# BEGIN SCHEDULE1_DEMO
    >> import shelve
    >> db = shelve.open(DB_NAME)
    >> if CONFERENCE not in db:
    ...     load(db)
    ...
    >> speaker = db['speaker.3741']
    >> type(speaker)
    >> speaker.name, speaker.twitter
# EBD SCHEDULE1_DEMO
"""
import warnings

import ch19_osconfeed as osconfeed

CONFERENCE = 'conference.115'
DB_NAME = 'E:\wksp\\fluent_python_examples\chapter_19\data\schedule1.db'


class Record:

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


def load(db):
    raw_feed = osconfeed.load()
    warnings.warn('loading ' + DB_NAME)
    for collection, rec_list in raw_feed['Schedule'].items():
        record_type = collection[:-1]
        for record in rec_list:
            key = '{}.{}'.format(record_type, record['serial'])
            record['serial'] = key
            db[key] = Record(**record)
