from setuptools import setup

setup(
    name='torch-recsys-metrics',
    version='0.0.1',
    author='Wonjun Oh',
    keywords=['pytorch', 'metrics', 'recsys', 'recommender systems'],
    description='A library of pytorch based recsys metrics supports efficient tensor calculation.',
    url='https://github.com/owj0421/torch-recsys-metrics',
    license='MIT License',
    python_requires='>=3.7',
    install_requires=[
        'numpy>=1.19.1',
        'torch>=1.6.1'
        ]
    )