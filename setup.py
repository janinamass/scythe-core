from setuptools import setup, find_packages
setup(
        name='scythecore',
        version='0.0.1',
        author='Janina Mass',
        author_email='janina.mass@hhu.de',
        packages=find_packages(),
        scripts=['scythecore/scythecore'],
        license='GPLv3',
        url='',
        description='',
        long_description=open('README.txt').read(),
        include_package_data=True,
        install_requires=[''],
        classifiers=[
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
            'Topic :: Scientific/Engineering :: Bio-Informatics'
        ],
        )