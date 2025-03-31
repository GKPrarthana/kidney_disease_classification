import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
    
__version__ = "0.0.0"
REPO_NAME = "kidney_disease_classification"
AUTHOR_USER_NAME = "GKPrarthana"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "39-dba-0025@kdu.ac.lk"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)
