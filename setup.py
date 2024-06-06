from setuptools import setup, find_packages

setup(
    name='OlympicKnowledge',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'requests',
        'beautifulsoup4',
        'fpdf',
        'schedule',
        'pillow',
        'fpdf',
    ],
    description='Provides comprehensive information about the history of handball in the Olympics.',
    author='Lanre Adetola',
    author_email='r0913836@student.thomasmore.be',
    url='https://github.com/LanreAdetola/olympicknowledge',
    license='ME',
)
