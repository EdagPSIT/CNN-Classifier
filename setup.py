import setuptools

with open("README.md", 'r', encoding='utf-8') as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "CNN_Classifier"
AUTHOR_USER_NAME = "EdagPSIT"
SRC_REPO = "CNN-Classifier"
AUTHOR_EMAIL = 'vhanamaneramesh@gmail.com'

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    long_description=long_description,
    long_description_content='text/markdown',
    url="https://github.com/{}/{}".format(AUTHOR_USER_NAME,REPO_NAME),
    project_urls={
        'Bug Tracker':"https://github.com/{}/{}/issues".format(AUTHOR_USER_NAME,REPO_NAME)
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where='src')
)