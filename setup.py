# -*- coding: utf-8 -*-
import os

from distutils.core import setup
from setuptools import find_packages


with open(os.path.join(os.path.dirname(__file__), 'README.md'), 'rb') as readme:
    readme_text = readme.read().decode('utf-8')

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-bootstrap-pagination',
    version='1.7.2',
    keywords="django bootstrap pagination templatetag",
    author=u'Jason McClellan<jason@jasonmcclellan.io>, Koert van der Veer<koert@ondergetekende.nl>',
    author_email='jason@jasonmccllelan.io',
    packages=find_packages(),
    url='https://github.com/jmcclell/django-bootstrap-pagination',
    license='MIT licence, see LICENCE',
    description='Render Django Page objects as Bootstrap 3.x/4.x Pagination compatible HTML',
    long_description=readme_text,
    long_description_content_type='text/markdown',
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Framework :: Django",
        "Framework :: Django :: 3.2.*",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ]
)
