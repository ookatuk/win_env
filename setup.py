# -*- coding: utf-8 -*-
import setuptools

with open('requirements.txt', encoding="utf-8") as f:
    requirements = f.read().splitlines()
with open('README.md', 'r', encoding='utf-8') as fp:
    readme = fp.read()
LONG_DESCRIPTION = readme
LONG_DESCRIPTION_CONTENT_TYPE = 'text/markdown'
setuptools.setup(
    name="win_all_env",
    version="1.1.3",
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'weatherforecast=weatherforecast:main',
        ]
    },
    packages=setuptools.find_packages(),
    description="windows env",
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESCRIPTION_CONTENT_TYPE,
    author="ookatuk",
    author_email="okatuhumi@gmail.com",
    python_requires='>=3.12.3',
    url="https://github.com/akino11/win_env",
    keywords="win-env"
)
