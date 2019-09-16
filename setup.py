# coding: utf-8

"""
    AVACloud API 1.10.0

    AVACloud API specification  # noqa: E501

    OpenAPI spec version: 1.10.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "avacloud-client-python"
VERSION = "1.10.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "certifi>=2017.4.17",
    "python-dateutil>=2.1",
    "six>=1.10",
    "urllib3>=1.23"
]
    

setup(
    name=NAME,
    version=VERSION,
    description="AVACloud API 1.10.0",
    author_email="",
    url="https://github.com/Dangl-IT/avacloud-client-python",
    keywords=["Swagger", "AVACloud API 1.10.0"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    AVACloud API specification  # noqa: E501
    """
)
