import setuptools


setuptools.setup(
    author="Siddharth Khattak",
    author_email="siddharth.khattak@aptusdatalabs.com",
    name='InvoiceService',
    license="MIT",
    description='InvoiceService is a package for invoice module',
    version='v0.0.1',
    long_description='',
    url='https://github.com/Siddharth0803/InvoiceService.git',
    packages=["InvoiceService"],
    python_requires=">=3.5",
    install_requires=['requests', 'json', 'pathlib'],
    classifiers=[
        # Trove classifiers
        # (https://pypi.python.org/pypi?%3Aaction=list_classifiers)
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
    ],
)