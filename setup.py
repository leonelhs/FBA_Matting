import re
from setuptools import setup, find_packages


def get_version():
    filename = "FBA_Matting/__init__.py"
    with open(filename) as f:
        match = re.search(
            r"""^__version__ = ['"]([^'"]*)['"]""", f.read(), re.M
        )
    if not match:
        raise RuntimeError("{} doesn't contain __version__".format(filename))
    version = match.groups()[0]
    return version


def get_install_requires():
    with open("requirements.txt") as req:
        return req.read().split("\n")


def get_long_description():
    with open("README.md") as f:
        return f.read()


def main():
    setup(
        name='FBA_Matting',
        version=get_version(),
        long_description=get_long_description(),
        long_description_content_type="text/markdown",
        packages=find_packages(),
        url='https://github.com/MarcoForte/FBA_Matting',
        license='MIT',
        author='Marco Forte and François Pitié',
        author_email='ortemarco.irl@gmail.com',
        description='Image alpha matting',
        install_requires=get_install_requires(),
        package_data={"FBA_Matting": []},
        entry_points={"console_scripts": ["FBA_Matting=FBA_Matting.__main__:main"]},
        classifiers=[
            "Development Status :: 5 - Production/Stable",
            "Intended Audience :: Developers",
            "Intended Audience :: Science/Research",
            "Natural Language :: English",
            "Operating System :: OS Independent",
            "Programming Language :: Python",
            "Programming Language :: Python :: 3.5",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: 3 :: Only",
        ],
    )


if __name__ == "__main__":
    main()
