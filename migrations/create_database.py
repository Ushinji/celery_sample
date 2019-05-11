import os
from sqlalchemy import create_engine


database_user = os.getenv('DATABASE_USER')
database_password = os.getenv('DATABASE_PASSWORD')
database_host = os.getenv('DATABASE_HOST')
mysql_engine = create_engine(
    f'mysql://{database_user}:{database_password}@{database_host}:3306')


# Create Database for development if it did not exist
database_name_development = 'celery_sample_development'
existing_databases = mysql_engine.execute("SHOW DATABASES;")
if database_name_development not in [d[0] for d in existing_databases]:
    mysql_engine.execute(
        f'''CREATE DATABASE {database_name_development}
            DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;''')
    print("Created database : {0}".format(database_name_development))


# Create Database for test if it did not exist
database_name_test = 'celery_sample_test'
existing_databases = mysql_engine.execute("SHOW DATABASES;")
if database_name_test not in [d[0] for d in existing_databases]:
    mysql_engine.execute(
        f'''CREATE DATABASE {database_name_test}
            DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;''')
    print("Created database : {0}".format(database_name_test))
