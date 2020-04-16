from setuptools import setup, find_packages

VERSION = '1.0'

setup(
    name='passphrase',
    version=VERSION,

    description='Generates a passphrase from English dicrionary words.',
        url='https://github.com/Videre-Research-LLC/python-passphrase',

    author='Christophe Gauge',
    author_email='chris@videreresearch.com',

    packages=['passphrase'],
    package_data={'passphrase': ['american-english']},

    include_package_data=True,

      entry_points={
          'console_scripts': [
              'passphrase = passphrase.__main__:main',
          ]
      },

)
