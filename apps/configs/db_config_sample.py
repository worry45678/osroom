# -*-coding:utf-8-*-
__author__ = "Allen Woo"
DB_CONFIG = {
    "mongodb": {
        "mongo_sys": {
            "username": "root",
            "config": {
                "fsync": False,
                "replica_set": None
            },
            "password": "<Your password>",
            "dbname": "osr_sys",
            "host": [
                "127.0.0.1:27017"
            ]
        },
        "mongo_user": {
            "username": "root",
            "config": {
                "fsync": False,
                "replica_set": None
            },
            "password": "<Your password>",
            "dbname": "osr_user",
            "host": [
                "127.0.0.1:27017"
            ]
        },
        "mongo_web": {
            "username": "root",
            "config": {
                "fsync": False,
                "replica_set": None
            },
            "password": "<Your password>",
            "dbname": "osr_web",
            "host": [
                "127.0.0.1:27017"
            ]
        }
    },
    "redis": {
        "password": "<Your password>",
        "port": [
            "6379"
        ],
        "host": [
            "127.0.0.1"
        ]
    }
}