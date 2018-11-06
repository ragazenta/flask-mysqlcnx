"""
Flask-MySQL-Connector
----------------

MySQL Connector extension for Flask
"""
from setuptools import setup


setup(
    name='Flask-MySQL-Connector',
    version='0.1.0',
    url='https://github.com/ragazenta/flask-mysqlcnx',
    license='MIT',
    author='Alexandre Ferland',
    author_email='aferlandqc@gmail.com',
    maintainer='Renjaya Raga Zenta',
    maintainer_email='ragazenta@gmail.com',
    description='MySQL Connector extension for Flask',
    long_description=__doc__,
    packages=['flask_mysqlcnx'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask>=0.10.1',
        'mysql-connector-python'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
