# Setup.py para pipeline_quantitativos
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="pipeline_quantitativos",
    version="1.0.0",
    author="Equipe de Engenharia de Dados",
    author_email="engenharia.dados@empresa.com",
    description="Pipeline automatizado para extração de quantitativos de projetos arquitetônicos",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/empresa/pipeline-quantitativos",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=['pandas>=1.5.0', 'numpy>=1.21.0', 'matplotlib>=3.5.0', 'seaborn>=0.11.0', 'psutil>=5.9.0', 'Flask>=2.0.0', 'Werkzeug>=2.0.0', 'dxfgrabber>=0.8.0', 'ezdxf>=0.17.0', 'PyYAML>=6.0'],
    entry_points={
        "console_scripts": [
            "pipeline-quantitativos=pipeline_quantitativos.cli:main",
        ],
    },
    include_package_data=True,
    package_data={
        "pipeline_quantitativos": ["config/*.yaml", "data/*.json"],
    },
)
