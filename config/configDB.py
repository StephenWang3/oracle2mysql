import sys
import cx_Oracle
import pymysql
from dbutils.pooled_db import PooledDB

import readConfig

config = readConfig.ReadConfig()

# MySQL read config
mysql_host = config.get_mysql('host')
mysql_port = int(config.get_mysql('port'))
mysql_user = config.get_mysql('user')
mysql_passwd = config.get_mysql('passwd')
mysql_database = config.get_mysql('database')
mysql_dbchar = config.get_mysql('dbchar')

# Oracle read config
oracle_host = config.get_oracle('host')
oracle_port = config.get_oracle('port')
oracle_user = config.get_oracle('user')
oracle_passwd = config.get_oracle('passwd')
oracle_service_name = config.get_oracle('service_name')


MySQLPOOL = PooledDB(
    creator=pymysql,  
    # Modules that use linked databases
    maxconnections=0,  
    # Maximum number of connections allowed by the connection pool, 
    # 0 and None means no limitation on the number of connections
    mincached=10,  
    # At initialisation, at least one free link is created in the link pool, 
    # 0 means no link is created.
    maxcached=0,  
    # Maximum number of idle links in the link pool, 
    # 0 and None are unlimited
    maxshared=3,
    # Maximum number of shared links in the link pool, 
    # 0 and None means all shared
    blocking=True,  
    # Whether to block waiting if there are no available connections in the connection pool. 
    # True: wait；False: No wait and then error
    maxusage=None,  
    # The maximum number of times a link can be reused, None means no limit.
    setsession=['SET AUTOCOMMIT=0;','SET foreign_key_checks=0;'],  
    # List of commands to execute before starting a session. 
    # Use connection pooling to execute dml, here you need to explicitly specify commit, tested and passed
    ping=0,
    # ping MySQL server to check if the service is available.
    host=mysql_host,
    port=mysql_port,
    user=mysql_user,
    password=mysql_passwd,
    database=mysql_database,
    charset=mysql_dbchar
)

class OraclePool:

    def __init__(self):
        '''
        Todo
        '''
        return None
        
    @staticmethod
    def __get_pool():
        '''
        Todo
        '''
        return None

    def __get_conn(self):
        '''
        Todo
        '''
        return None
    
    @staticmethod
    def __reset_conn(conn, cursor):
        '''
        Todo
        '''
        return None

    def __execute(self, sql, args=None):
        '''
        Todo
        '''
        return None
    
    def fetch_all(self, sql, args=None):
        '''
        Todo
        '''
        return None
    
    def fetch_many(self, sql, size=None):
        '''
        Todo
        '''
        return None

    def execute_sql(self, sql, args=None):
        '''
        Todo
        '''
        return None

    def __del__(self):
        '''
        Todo
        '''
        return None
