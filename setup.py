import setuptools

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

__version__ = "0.0.0"

REPO_NAME = 'Chicken-Disease-Classification'
AUTHOR = 'EhsanKhosh'
SRC_REPO = 'cnnClassifier'
AUTHOR_EMAIL = 'ehsan.khoshakhlagh77@gmail.com'

setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description='A Python package for classifying Chicken Disease',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f'https://github.com/{AUTHOR}/{REPO_NAME}',
    project_urls={
        'Bug Tracker': f'https://github.com/{AUTHOR}/{REPO_NAME}/issues',
    },
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src')
)
