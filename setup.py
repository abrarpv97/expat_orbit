from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in expat_orbit/__init__.py
from expat_orbit import __version__ as version

setup(
	name="expat_orbit",
	version=version,
	description="App to manager country services",
	author="abrarpv97@gmail.com",
	author_email="abrarpv97@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
