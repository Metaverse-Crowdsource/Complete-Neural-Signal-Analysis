from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='neural_signal_analysis',
    version='0.2.4',
    description='A comprehensive Python library for human brain/ cortical organoid/spheroid eeg/ecog/mea data analysis including FFT, Higuchi Fractal Dimension, Transfer Entropy, and more.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='soul_syrup',
    author_email='soul.syrup@yandex.com',
    url='https://soulsyrup.github.io/',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'scipy',
        'matplotlib',
        'minepy',
        'pyinform',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
