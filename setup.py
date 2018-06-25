from setuptools import setup
from setuptools import find_packages

version = '0.0.1'

install_requires = [

]

dev_extras = [
    'pep8',
    'tox',
    'pypandoc',
]

docs_extras = [
    'Sphinx>=1.0',  # autodoc_member_order = 'bysource', autodoc_default_flags
    'sphinx_rtd_theme',
    'sphinxcontrib-programoutput',
]


try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
    long_description = long_description.replace("\r", '')

except(IOError, ImportError):
    import io
    with io.open('README.md', encoding='utf-8') as f:
        long_description = f.read()

setup(
    name='chacha20poly1305',
    version=version,
    description='Chacha20Poly1305',
    long_description=long_description,
    url='https://github.com/ph4r05/py-chacha20poly1305',
    author='Dusan Klinec',
    author_email='dusan.klinec@gmail.com',
    license='LGPL',
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Security',
    ],

    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    extras_require={
        'dev': dev_extras,
        'docs': docs_extras,
    },
)
