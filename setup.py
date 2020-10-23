from setuptools import find_packages, setup

setup(
    name='src',
    packages=find_packages(),
    version='0.1.0',
    description="""**********************
    build a model to predict which category an unseen search term belongs. 
    comes with a labelled data set mapping many search terms and their categories.
    **********************""",
    author='oskar',
    license='MIT',
)
