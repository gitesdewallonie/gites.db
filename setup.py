from setuptools import setup, find_packages
import os

version = '0.4.6'

setup(
    name='gites.db',
    version=version,
    description="Db connexion for Gites de Wallonie",
    long_description=open("README.txt").read() + "\n" +
    open(os.path.join("docs", "HISTORY.txt")).read(),
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules"],
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
        'geoalchemy',
        'Acquisition',
        'Zope2',
        'zope.component',
        'zope.interface',
        'z3c.sqlalchemy',
        'affinitic.caching',
        'affinitic.db [caching]',
        'affinitic.pwmanager',
        'Products.CMFCore',
        'Products.Archetypes'],
    extras_require=dict(
        test=[
            'affinitic.testing',
            'unittest2',
            'zope.testing',
            'plone.testing',
            'gocept.testdb'],
        scripts=[
            'alembic',
            'progressbar'],
        docs=['z3c.recipe.sphinxdoc',
              'docutils',
              'repoze.sphinx.autointerface',
              'affinitic.sphinxcontrib.sqlalchemy',
              'collective.sphinx.includechangelog',
              'collective.sphinx.includedoc']),
    entry_points={
        'console_scripts': [
            'gdw_db_migration = gites.db.migration.migration:main',
            'xml_heb_ch_mh_proprio = gites.db.scripts.xml_heb_ch_mh_proprio:main',
            'xml_heb_gr_proprio = gites.db.scripts.xml_heb_gr_proprio:main']})
