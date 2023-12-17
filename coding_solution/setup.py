from setuptools import setup, find_packages

setup(
    name="coding_assignment",
    version="1.0.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Flask==2.1.1",
        "Flask-RESTful==0.3.10",
        "Flask-SQLAlchemy==2.5.1",
        "Werkzeug==2.0.1",
        "SQLAlchemy==1.4.48",
        "Flask-JWT-Extended",
        "moviepy"
    ],
)
