#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

requirements = [ ]

test_requirements = [ ]

setup(
    author="Jelmer van der Saag",
    author_email='jelmervandersaag@me.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="The model-training repository of Team 8 for the Release Engineering for Machine Learning (CS4295) course at the TU Delft.",
    install_requires=requirements,
    license="MIT license",
    include_package_data=True,
    keywords='model_training',
    name='model_training',
    packages=find_packages(include=['model_training', 'model_training.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/JvanderSaag/model_training',
    version='0.2.0',
    zip_safe=False,
)
