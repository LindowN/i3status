import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="i3status",
    version="0.1",
    author="Sahra VADROT, Cécile HUGUET, Rémy PEYRE, Damien NIVAULT, Nathaël ARKI",
    author_email="sahra.vadrot@supinternet.fr",
    description=("A package to get some informations about your computer : its CPU temperature, its volume, its ping,"
                 " and so on and so on."),
    license="apache",
    keywords="i3status made in group",
    url="unregistered",
    packages=["interface_graphique"], # interface graphique
    long_description=read('README.rst'),
)
