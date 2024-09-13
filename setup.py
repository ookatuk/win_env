import setuptools

with open('requirements.txt') as f:
    requirements = f.read().splitlines()


setuptools.setup(
    name="win_env",
    version="1.0.2",
    install_requires = requirements,
    entry_points={
        'console_scripts': [
            'weatherforecast=weatherforecast:main',
        ],
    },
    packages=setuptools.find_packages(),
    description="sample packages by legacy-setup.py",
    author="ookatuk",
    author_email="okatuhumi@gmail.com",
    python_requires='>=3.12.3',
)
