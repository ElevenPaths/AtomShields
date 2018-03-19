# -*- coding: utf-8 -*-
u"""
Copyright 2018 ElevenPaths - Telefonica Digital España

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

# from setuptools import setup
from setuptools import find_packages
from distutils.core import setup

def read_file(filename):
    with open(filename) as f:
        return f.read()

package_name = 'atomshields'

setup(
  name = package_name,
  version = read_file('VERSION').strip(),
  install_requires=read_file('requirements.txt').splitlines(),
  packages = find_packages(),
  author = 'ElevenPaths',
  description = """Framework de pruebas de seguridad en repositorios de código fuente. Dispone de un sistema 
  flexible para la realización de pruebas de seguridad y comunicación de resultados.""",
  long_description=open('README.rst').read(),
  author_email = 'diego.fernandez@11paths.com, david.amrani@11paths.com',
  url = 'https://github.com/ElevenPaths/AtomShields',
  project_urls={
      "Documentation": "https://atomshields.readthedocs.io",
      "Source Code": "https://github.com/ElevenPaths/AtomShields",
  },
  download_url = 'https://github.com/ElevenPaths/AtomShields/tarball/0.1',
  keywords = 'security, source code, analysis',
  license='Apache 2.0',
  classifiers=[
      'Development Status :: 4 - Beta',
      'Intended Audience :: Developers',
      'Intended Audience :: Other Audience',
      'License :: OSI Approved :: Apache Software License',
      'Natural Language :: English',
      'Operating System :: OS Independent',
      'Programming Language :: Python :: 2.7',
      'Topic :: Software Development :: Libraries :: Python Modules',
      'Topic :: Software Development :: Quality Assurance',
      'Topic :: Software Development :: Testing',
  ],
)


# Setup files

from atomshields.scanner import AtomShieldsScanner

AtomShieldsScanner.setup()

