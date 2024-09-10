import setuptools

with open('requirements.txt') as f:
    requirements = f.read().splitlines()


setuptools.setup(
    name="ookatuk",
    version="1.0.0",
    install_requires = requirements,
    entry_points={
        'console_scripts': [
            'weatherforecast=weatherforecast:main',
        ],
    },
    packages=setuptools.find_packages(),
    description="sample packages by legacy-setup.py",
    author="author",
    # author_email="sample@example.com",
    python_requires='>=3.21',
)
