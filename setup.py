import io
import os
from setuptools import find_packages, setup


def read(*paths, **kwargs):
    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="litellm-core",
    version=read("", "VERSION"),
    description="LiteLLM core completions and generation functions.",
    url="https://github.com/JohnnyRacer/litellm-core/",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="JohnnyRacer",
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=read_requirements("requirements.txt"),
)
