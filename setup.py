from os import path
from io import open
from setuptools import setup

from model_grpc_service import __name__, __version__, __doc__

# Get the long description from the README file
here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name=__name__,
    version=__version__,
    description=__doc__,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/schmidtbri/grpc-ml-model-deployment",
    author="Brian Schmidt",
    author_email="6666331+schmidtbri@users.noreply.github.com",
    packages=["model_grpc_service"],
    python_requires=">=3.5",
    install_requires=["iris-model@git+https://github.com/schmidtbri/ml-model-abc-improvements#egg=iris_model@master",
                      "nameko==2.12.0",
                      "nameko-grpc==1.0.1",
                      "grpcio-tools==1.26.0",
                      "Jinja2==2.10.3"],
    tests_require=['pytest', 'pytest-html', 'pylama', 'coverage', 'coverage-badge', 'bandit', 'safety']
)
