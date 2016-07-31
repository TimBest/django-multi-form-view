from distutils.core import setup
from setuptools import find_packages


setup(
    name='django-multi-form-view',
    version='0.0.1',
    author=u'Timothy Best',
    packages=find_packages(),
    url='https://github.com/TimothyBest/django-multi-form-view',
    license='GNU licence, see LICENCE',
    description='Class based views for handling more than one form in a view',
    long_description=open('README.md').read(),
    zip_safe=False,
)
