import os

from setuptools import setup  # type: ignore


def read(fname: str) -> str:
    with open(os.path.join(os.path.dirname(__file__), fname)) as _f:
        return _f.read()


setup(
    author="Nikita Sivakov",
    author_email="sivakov512@gmail.com",
    classifiers=[
        "Framework :: AsyncIO",
        "Framework :: Pytest",
        "Framework :: Pytest",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python",
        "Topic :: Software Development :: Testing",
    ],
    description="Pytest `client` fixture for the Aiohttp",
    entry_points={"pytest11": ["pytest_aiohttp_client = pytest_aiohttp_client"]},
    keywords=["pytest", "fixture", "aiohttp", "client", "api"],
    license="MIT",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    name="pytest-aiohttp-client",
    py_modules=["pytest_aiohttp_client"],
    python_requires=">=3.6",
    install_requires=["pytest>=6", "aiohttp>=3"],
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    url="https://github.com/sivakov512/pytest-aiohttp-client",
    version="0.0.1",
)
