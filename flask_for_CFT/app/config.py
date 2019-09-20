class Configuration(object):
	DEBUG = True
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:password@localhost/test1'
	SECRET_KEY = 'secret'

	#### Flask security
	SECURITY_PASSWORD_SALT = 'salt'
	SECURITY_PASSWORD_HASH = 'sha512_crypt'