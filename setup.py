from setuptools import setup, find_packages
import os

version = '0.4dev'

setup(
    name='gites.db',
    version=version,
    description="Db connexion for Gites de Wallonie",
    long_description=open("README.txt").read() + "\n" +
                     open(os.path.join("docs", "HISTORY.txt")).read(),
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
    keywords='',
    author='Affinitic',
    author_email='info@affinitic.be',
    url='http://svn.affinitic.be/plone/gites/gites.db',
    license='GPL',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['gites'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'psycopg2',
        'SQLAlchemy',
        'Acquisition',
        'Zope2',
        'zope.component',
        'zope.interface',
        'z3c.sqlalchemy',
        'affinitic.caching',
        'affinitic.db',
        'affinitic.pwmanager',
    ],
    extras_require=dict(
        test=[
            'unittest2',
            'zope.testing',
            'plone.testing',
        ],
        scripts=[
            'alembic',
    ]),
    entry_points={
        'console_scripts': [
            'xml_heb_ch_mh_proprio = gites.db.scripts.xml_heb_ch_mh_proprio:main',
            'xml_heb_gr_proprio = gites.db.scripts.xml_heb_gr_proprio:main']}
    )
