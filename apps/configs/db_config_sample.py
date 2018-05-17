# -*-coding:utf-8-*-
__author__ = "Allen Woo"
DB_CONFIG = {
    "mongodb": {
        "mongo_web": {
            "username": "work",
            "dbname": "osr_web",
            "host": [
                "127.0.0.1:27017"
            ],
            "password": "<Your password>",
            "config": {
                "fsync": False,
                "replica_set": None
            }
        },
        "mongo_user": {
            "username": "work",
            "dbname": "osr_user",
            "host": [
                "127.0.0.1:27017"
            ],
            "password": "<Your password>",
            "config": {
                "fsync": False,
                "replica_set": None
            }
        },
        "mongo_sys": {
            "username": "work",
            "dbname": "osr_sys",
            "host": [
                "127.0.0.1:27017"
            ],
            "password": "<Your password>",
            "config": {
                "fsync": False,
                "replica_set": None
            }
        }
    },
    "redis": {
        "port": [
            "6379"
        ],
        "host": [
            "127.0.0.1"
        ],
        "password": "<Your password>"
    }
}