from pymongo import MongoClient

# Para correr la base de datos de mondo desde consola:
# C:\Program Files> MongoDB\Server\6.0\bin\mongod.exe --dbpath="data\db"

# Base de Datos Local
# db_client = MongoClient().local

# Base de Datos Remota
db_client = MongoClient(
    "mongodb+srv://test:BeirasTester492@cluster0.xmrdzp9.mongodb.net/?retryWrites=true&w=majority").test
