import mysql.connector
from flask import _app_ctx_stack, current_app


class MySQL(object):

    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        """Initialize the `app` for use with this
        :class:`~flask_mysqlcnx.MySQL` class.
        This is called automatically if `app` is passed to
        :meth:`~MySQL.__init__`.

        :param flask.Flask app: the application to configure for use with
            this :class:`~flask_mysqlcnx.MySQL` class.
        """

        app.config.setdefault('MYSQL_HOST', 'localhost')
        app.config.setdefault('MYSQL_USER', None)
        app.config.setdefault('MYSQL_PASSWORD', None)
        app.config.setdefault('MYSQL_DB', None)
        app.config.setdefault('MYSQL_PORT', 3306)
        app.config.setdefault('MYSQL_UNIX_SOCKET', None)
        app.config.setdefault('MYSQL_CONNECT_TIMEOUT', 10)
        app.config.setdefault('MYSQL_USE_UNICODE', True)
        app.config.setdefault('MYSQL_CHARSET', 'utf8')
        app.config.setdefault('MYSQL_SQL_MODE', None)

        if hasattr(app, 'teardown_appcontext'):
            app.teardown_appcontext(self.teardown)

    @property
    def connect(self):
        kwargs = {}

        if current_app.config['MYSQL_HOST']:
            kwargs['host'] = current_app.config['MYSQL_HOST']

        if current_app.config['MYSQL_USER']:
            kwargs['user'] = current_app.config['MYSQL_USER']

        if current_app.config['MYSQL_PASSWORD']:
            kwargs['password'] = current_app.config['MYSQL_PASSWORD']

        if current_app.config['MYSQL_DB']:
            kwargs['database'] = current_app.config['MYSQL_DB']

        if current_app.config['MYSQL_PORT']:
            kwargs['port'] = current_app.config['MYSQL_PORT']

        if current_app.config['MYSQL_UNIX_SOCKET']:
            kwargs['unix_socket'] = current_app.config['MYSQL_UNIX_SOCKET']

        if current_app.config['MYSQL_CONNECT_TIMEOUT']:
            kwargs['connection_timeout'] = \
                current_app.config['MYSQL_CONNECT_TIMEOUT']

        if current_app.config['MYSQL_USE_UNICODE']:
            kwargs['use_unicode'] = current_app.config['MYSQL_USE_UNICODE']

        if current_app.config['MYSQL_CHARSET']:
            kwargs['charset'] = current_app.config['MYSQL_CHARSET']

        if current_app.config['MYSQL_SQL_MODE']:
            kwargs['sql_mode'] = current_app.config['MYSQL_SQL_MODE']

        return mysql.connector.connect(**kwargs)

    @property
    def connection(self):
        """Attempts to connect to the MySQL server.

        :return: Bound MySQL connection object if successful or ``None`` if
            unsuccessful.
        """

        ctx = _app_ctx_stack.top
        if ctx is not None:
            if not hasattr(ctx, 'mysql_cnx'):
                ctx.mysql_cnx = self.connect
            return ctx.mysql_cnx

    def teardown(self, exception):
        ctx = _app_ctx_stack.top
        if hasattr(ctx, 'mysql_cnx'):
            ctx.mysql_cnx.close()
