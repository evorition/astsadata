from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="astsadata",
    version="0.0.4",
    author="Maxim Makovskiy",
    author_email="makovskiyms@gmail.com",
    description="Python package that contains all datasets from R astsa package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="GPLv3",
    url="https://github.com/evorition/astsadata",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=["pandas"],
    python_requires=">=3.6",
)
