from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='gites.db',
      version=version,
      description="Db connexion for Gites de Wallonie",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
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
          'affinitic.pwmanager',
          'z3c.sqlalchemy'
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
