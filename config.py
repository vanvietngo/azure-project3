import os

app_dir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig:
    DEBUG = True
    POSTGRES_URL="techconfdb-servername.postgres.database.azure.com"  #TODO: Update value
    POSTGRES_USER="adminuser" #TODO: Update value
    POSTGRES_PW="aA123456789000"   #TODO: Update value
    POSTGRES_DB="techconfdb"   #TODO: Update value
    DB_URL = 'postgresql://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB)
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI') or DB_URL
    CONFERENCE_ID = 1
    SECRET_KEY = 'LWd2tzlprdGHCIPHTd4tp5SBFgDszm'
    SERVICE_BUS_CONNECTION_STRING ='Endpoint=sb://notificationqueueservicebusfpt.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=H0RhxsZJMdajAy1TwDFR+9VWi/bGa8oKZ+ASbFFHfqQ=' #TODO: Update value
    SERVICE_BUS_QUEUE_NAME ='notificationqueueservicebusfpt'
    ADMIN_EMAIL_ADDRESS: 'viet.ngovanviet@gmail.com'
    SENDGRID_API_KEY = '' #Configuration not required, required SendGrid Account

class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False