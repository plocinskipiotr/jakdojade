"""
Contains class DBService which can be used to DB operations

    note:
        Uses Base object from db_model. Thanks to this object DB schema can be constructed

"""

import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.src.db_model import Base


class DBService():
    """This class is responsible for db communication

        arguments:
            path (str) : path to db config file
            db_type (str) : type of db (postgres,oracle etc.)

        attributes:
            conf (str) : configuration string based on configuration path
            db_type (str) : type of db (postgres,oracle etc.)
            conn_string (str) : connection string to db

        note:
            with build_schema user can create database which contains tables based on
            Base metadata

    """

    def __init__(self, path: str, db_type: str):
        self.conf = self.load_conf(path)
        self.db_type = db_type
        self.conn_string = self.get_conn_string()

    @staticmethod
    def load_conf(path: str) -> dict:
        """loads db configuration from file"""
        with open(path, 'r') as db_conf:
            data = json.load(db_conf)
        return data

    def get_conn_string(self) -> str:
        """gets db connection string"""
        parser = self.string_parser()
        return parser(self.conf[self.db_type])

    def get_sessionmaker(self) -> sessionmaker:
        """gets sessionmaker object"""
        engine = self.get_engine()
        session_maker = sessionmaker(engine)
        return session_maker

    def get_engine(self):
        """gets engine object"""
        engine = create_engine(self.conn_string)
        return engine

    def string_parser(self):
        """gets string parser"""
        if self.db_type == 'postgres':
            return DBService.postgres_parser
        else:
            raise ValueError('db_string error, db unknown: ' + self.db_type)

    def build_schema(self) -> None:
        """ build schema for database

            It uses Base object from db_model to construct the db schema.
        """
        engine = self.get_engine()
        #Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)

    @staticmethod
    def postgres_parser(params: dict) -> str:
        """postgres db string parser"""
        return params['dialect'] \
               + '://' \
               + params['user'] \
               + ':' \
               + params['passwd'] \
               + '@' \
               + params['host'] \
               + ':' \
               + params['port'] \
               + '/' \
               + params['db']
