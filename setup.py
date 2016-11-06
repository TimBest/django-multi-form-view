from distutils.core import setup
from setuptools import find_packages


setup(
    name='django-multi-form-view',
    version='1.0',
    author=u'Tim Best',
    packages=find_packages(),
    url='https://github.com/TimBest/django-multi-form-view',
    license='GNU licence, see LICENCE',
    description='Class based views for handling more than one form in a single view',
    long_description=open('README.md').read(),
    zip_safe=False,
)
