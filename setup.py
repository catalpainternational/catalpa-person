from setuptools import setup

setup(
    name='catalpa-person',
    version='1.0',
    license="",

    install_requires = [
        "catalpa-aihun",

],

    description="The common project used for representing a Person across catalpa's health related projects.",
    long_description=open('README.md').read(),
    author='Anders Hofstee, Nicoas Hoibian',
    author_email='a.hofstee@catalpainternational.org',

    url='https://github.com/catalpainternational/catalpa-person',
    include_package_data=True,

    packages=['person'],
    package_data={'aihun':['README.md']},
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ]
)