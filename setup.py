from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='upfrontaccounting.theme',
      version=version,
      description="UpfrontAccounting Theme",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='web zope plone theme upfront accounting',
      author='Upfront Systems',
      author_email='info@upfrontsystems.co.za',
      url='http://svn.plone.org/svn/collective/upfrontaccounting.theme',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['upfrontaccounting'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=["PasteScript"],
      paster_plugins = ["ZopeSkel"],
      )
