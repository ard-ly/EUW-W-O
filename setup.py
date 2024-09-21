from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in euw/__init__.py
from euw import __version__ as version

setup(
	name="euw",
	version=version,
	description="EUW app for Workorder",
	author="Aseel Gh",
	author_email="aseel.gharbia@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
