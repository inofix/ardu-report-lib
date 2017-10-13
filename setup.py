"""Setup the ardu-report-lib library module.

See:
https://github.com/inofix/ardu-report-lib

Note:
Based on the https://github.com/pypa/sampleproject/blob/master/setup.py.
Consult that for comments and description..
"""

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='ardu-report-lib',
    version='1.0.2.dev4+gda9cdd7',
    description='Get sensor data over the serial line and send it to an URL (JSON).',
    long_description=long_description,

    url='https://github.com/inofix/ardu-report-lib',
    author='Michael Lustenberger',
    author_email='mic@inofix.ch',

    license='GPLv3',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 5 - Production/Stable',

        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries :: Python Modules',

        'License :: OSI Approved :: GNU General Public License (GPL)',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    keywords='arduino sensor serial json',

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    install_requires=[
        'httplib2',
        'jsonschema',
        'pyserial',
        'requests',
        'urllib3',
    ],

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    extras_require={
#        'dev': ['check-manifest'],
        'test': ['unittest2'],
    },

    package_data={
        'meta_schema': ['schemas/meta-schema.json'],
        'default_schema': ['schemas/default-schema.json'],
    },

    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files # noqa
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
#    data_files=[('my_data', ['data/data_file'])],

)
