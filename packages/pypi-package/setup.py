from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="online-c-compiler",
    version="1.0.0",
    description="Official Python SDK and CLI for onlineccompiler.com - Fast GCC C compilation, debugging and memory visualization.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://onlineccompiler.com/",
    project_urls={
        "Homepage": "https://onlineccompiler.com/",
        "Web IDE": "https://onlineccompiler.com/",
        "Español": "https://onlineccompiler.com/es/",
        "Português": "https://onlineccompiler.com/pt/",
        "Deutsch": "https://onlineccompiler.com/de/",
        "Français": "https://onlineccompiler.com/fr/",
        "Source": "https://github.com/MoMahdideveloper/online-c-compiler-suite",
        "Tracker": "https://github.com/MoMahdideveloper/online-c-compiler-suite/issues",
    },
    author="Mahdi Hatefi",
    author_email="bro.meyti@gmail.com",
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Topic :: Software Development :: Compilers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
    ],
    keywords="c, compiler, gcc, clang, online-c-compiler, memory-visualizer, c11, c17, c23",
    packages=find_packages(),
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "online-c-compiler=online_c_compiler.cli:main",
            "occ-py=online_c_compiler.cli:main",
        ],
    },
)
