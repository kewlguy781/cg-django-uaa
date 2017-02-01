import distutils.cmd
from setuptools import setup, find_packages
import subprocess

from uaa_client import VERSION


class SimpleCommand(distutils.cmd.Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass


class DevDocsCommand(SimpleCommand):
    description = "Run development server for documentation"

    def run(self):
        subprocess.check_call(
            ['sphinx-autobuild', '.', '_build_html', '-p', '8001'],
            cwd='docs'
        )


class UltraTestCommand(SimpleCommand):
    description = "Run tests, code coverage, linting, etc."

    def run(self):
        subprocess.check_call(
            ['coverage', 'run', 'setup.py', 'test']
        )
        subprocess.check_call(
            ['flake8', 'uaa_client']
        )
        subprocess.check_call(
            ['coverage', 'report', '-m']
        )
        print("Success!")


setup(name='cg-django-uaa',
      cmdclass={
          'devdocs': DevDocsCommand,
          'ultratest': UltraTestCommand,
      },
      zip_safe=False,
      version=VERSION,
      description='A cloud.gov UAA authentication backend for Django',
      author='Atul Varma',
      author_email='atul.varma@gsa.gov',
      license='Public Domain',
      url='https://github.com/18F/cg-django-uaa',
      package_dir={'uaa_client': 'uaa_client'},
      include_package_data=True,
      packages=find_packages(),
      install_requires=[
          'django>=1.8,<2',
          'PyJWT>=1.4.2',
          'requests>=2.11.0'
      ],
      test_suite='uaa_client.runtests.run_tests',
      tests_require=[
          'httmock>=1.2.5',
      ],
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Environment :: Web Environment',
          'Framework :: Django',
          'Framework :: Django :: 1.8',
          'Framework :: Django :: 1.9',
          'Framework :: Django :: 1.10',
          'Intended Audience :: Developers',
          'License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Topic :: Utilities'],
      )
