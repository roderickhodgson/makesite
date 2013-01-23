from setuptools import setup

setup(name='makesite',
      version='0.1',
      description='A simple python script for creating a template HTML5 web page and associated javascript and css files inside the current directory.',
      long_description=open('README.md').read(),
      url='http://github.com/roderickhodgson/makesite',
      author='Roderick Hodgson',
      author_email='roderick.hodgson@googlemail.com',
      license='MIT',
      scripts=['makesite'],
      zip_safe=False)

