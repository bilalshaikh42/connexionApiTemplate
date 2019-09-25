import setuptools
import os
name = 'crbm'
dirname = os.path.dirname(__file__)
setuptools.setup(
    name=name,
    entry_points={
        'console_scripts': ["crbm = crbm.app"],
    },
    packages=setuptools.find_packages(exclude=['tests', 'tests.*']),

)
