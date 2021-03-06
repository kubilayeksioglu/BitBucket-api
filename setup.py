# -*- coding: utf-8 -*-
from distutils.core import setup

import bitbucket

if __name__ == "__main__":
    setup(
        name='bitbucket-api',
        version=bitbucket.__version__,
        description='Bitbucket API',
        long_description=open('README').read(),
        author='Baptiste Millou',
        author_email='kubilayeksioglu@vizeralabs.com',
        url='https://github.com/kubilayeksioglu/BitBucket-api',
        packages=[
            'bitbucket',
            'bitbucket.tests',
        ],
        license=open('LICENSE').read(),
        install_requires=['requests', 'sh', 'requests-oauthlib'],
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: ISC License (ISCL)',
            'Programming Language :: Python',
            'Natural Language :: English',
            'Operating System :: OS Independent',
            'Topic :: Software Development :: Libraries :: Python Modules',
        ],
    )
