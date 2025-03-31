from setuptools import setup, find_packages

setup(
    name="probability_distributions",
    version="1.0.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    entry_points={
        "console_scripts": [
            "p_dist=main:main",
        ],
    },
    install_requires=[],
    description="A module for probability distributions and related calculations.",
    author="Munashe Mukweya",
    author_email="munashemukweya2022@gmail.com",
    url="https://github.com/yourusername/probability_distributions",
)