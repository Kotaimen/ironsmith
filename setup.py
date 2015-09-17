import os
import sys
import re
import codecs


from setuptools import setup, find_packages

WHERE_AM_I = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    return codecs.open(os.path.join(WHERE_AM_I, *parts), 'r').read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError('Unable to find version string.')


py_modules = []

ext_modules = []

package_data = {

}


entry_points = '''
[console_scripts]
ironsmith=ironsmith.__main__:cli
ironsmith%d=ironsmith.__main__:cli
''' % sys.version_info.major


install_requires = [
    'Flask>=0.10',
    'Click>=4.0',
    'gunicorn>=19.0.0',
    'six>=1.9.0',
]

test_requires = [
    'nose>=1.3.0',
    'coverage>=3.7.0',
]

cmdclass = {}

setup(
    name='ironsmith',
    version=find_version('ironsmith', '__init__.py'),
    description='Map annotation using mapnik.',
    long_description='',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Operating System :: POSIX',
        'License :: OSI Approved :: MIT License',
        'Topic :: Scientific/Engineering :: GIS',
        'Topic :: Multimedia :: Graphics',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],
    keywords='map mapnik annotation',
    author='K&R',
    author_email='kotaimen.c@gmail.com, gliese.q@gmail.com',
    url='http://github.com/kotaimen/ironsmith',
    license='MIT',

    py_modules=py_modules,
    ext_modules=ext_modules,
    packages=find_packages(exclude=['tests', 'tests.*']),
    include_package_data=True,
    package_data=package_data,
    entry_points=entry_points,

    install_requires=install_requires,
    tests_require=test_requires,
    test_suite='tests',
    zip_safe=True,
    cmdclass=cmdclass,

    extras_require={
        'testing': test_requires,
    }

)
