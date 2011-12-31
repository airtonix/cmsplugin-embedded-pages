import os
from setuptools import (
  setup,
  find_packages,
)
import cmsplugin_embeddedpages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='cmsplugin-embedded-pages',
    version=cmsplugin_embeddedpages.__version__,
    classifiers = (
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ),
    packages=find_packages(),
    install_requires=(
        'django-cms',
    ),
    author='Zenobius Jiricek',
    author_email='airtonix@gmail.com',
    description='DjangoCMS plugin that allows for embedding other pages in placeholders',
    long_description = read('README.md'),
    license='BSD',
    keywords='django-cms, plugin, pages',
    url='http://github.com/airtonix/cmsplugin-embedded-pages',
    include_package_data=True,
)
