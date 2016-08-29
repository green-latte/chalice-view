#!/usr/bin/env python
from setuptools import setup, find_packages


with open('README.md') as readme_file:
    README = readme_file.read()


install_requires = [
    'chalice==0.1.0',
]


setup(
    name='chalice_view',
    version='0.1.0',
    description="Chalice utils for developing views",
    long_description=README,
    author="Kousuke Takeuchi",
    author_email='k.takeuchi@warrantee.co.jp',
    url='https://github.com/green-latte/chalice-view',
    packages=find_packages(exclude=['tests']),
    install_requires=install_requires,
    license="Apache License 2.0",
    package_data={'chalice_view': ['*.json']},
    include_package_data=True,
    zip_safe=False,
    keywords='chalice-view',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
    ],
)
