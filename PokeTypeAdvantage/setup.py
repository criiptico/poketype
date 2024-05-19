from setuptools import setup, find_packages

setup(
    name='PokeTypeAdvantage',
    version='0.1.0',
    packages=find_packages(),
    author='Adrian Quiroz - aka criiptico',
    author_email='adrianquiroz166@gmail.com',
    description='A package for evaluating Pokémon type advantages',
    install_requires=['pydantic', 'requests'],
    python_requires='>=3.10.12',
    # entry_points={
    #     'console_scripts': [
    #         'poketypeadvantage=poketypeadvantage.poketypeadvantage:main',
    #     ],
    # },
)