from setuptools import setup

setup(
    name='jupyterhub-authenticator',
    version='1.1',
    description='Authenticator Implementations for JupyterHub',
    url='https://github.com/hokiegeek2/jupyterhub-authenticator',
    author='John Yost',
    author_email='hokiegeek2@gmail.com',
    license='3 Clause BSD',
    packages=['jupyterhubauthenticator'],
    install_requires=[
        'jupyterhub',
    ]
)

