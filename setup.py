from setuptools import setup, find_packages

setup(
    name='buckshot-orm',
    version='0.1.0',
    packages=find_packages(exclude=['tests']),
    url='https://github.com/RiceKab/JenkinsDevTest',
    license='MIT',
    author='Kevin CYT',
    author_email='kevin@cyborn.be',
    description='A python package that does absolutely nothing of note to experiment with Jenkins.',
    install_requires=['click'],
    tests_requires=['pytest'],
    python_requires='>=2.7',
    # entry_points='''
    #     [console_scripts]
    #     jenky=jenky.cli:cli_entry
    # '''
)
