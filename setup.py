from setuptools import setup, find_packages

with open("README.md") as file:
    description = file.read()

setup(
    name='jsondatafaker',
    version='1.0.0',
    description='A Python package to generate fake JSON',
    long_description = description,
    long_description_content_type = "text/markdown",
    author='Necati Arslan',
    author_email='necatia@gmail.com',
    packages=find_packages(),
    install_requires=[
        'faker',
        'pyyaml'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Topic :: Software Development :: Libraries',
    ],
    project_urls={
        "Documentation": "https://github.com/necatiarslan/json-datafaker/blob/main/README.md",
        "Source": "https://github.com/necatiarslan/json-datafaker",
    },
    entry_points={
        'console_scripts': [
            'jsondatafaker = jsondatafaker.cli:main',
        ],
    },
)