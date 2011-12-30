import os
from setuptools import (
  setup,
  find_packages,
)
import cmsplugin_configurableproduct


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='cmsplugin-configurableproduct',
    version=cmsplugin_configurableproduct.__version__,
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
        'django-shop',
        'django-cms',
        'django-shop-configurableproduct',
    ),
    author='Zenobius Jiricek',
    author_email='airtonix@gmail.com',
    description='DjangoCMS plugin for django-shop-configurableproduct',
    long_description = read('README.md'),
    license='BSD',
    keywords='django-cms, plugin, django-shop, product',
    url='http://github.com/airtonix/cmsplugin-configurableproduct',
    include_package_data=True,
    zip_safe = False,
)
