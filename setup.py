"""
To upload the package to PyPi, follow these steps:
  1. Create a directory named 'invoicing,' for example, and put inside the module 'py' file of your module created. Then create a new 'py' file inside that directory named '__init__'.
  2. Execute in terminal 'python setup.py sdist' to generate the directory 'dist'.
  3. Execute 'pip install twine' to intall twine package.
  4. Create an account on PyPi webpage.
  5. Execute in terminal 'twine upload --skip-existing dist/*'. If everything goes well, you have created and uploaded your package successfully.
"""

from setuptools import setup

setup(
  name = 'invoicing-CVS-11-2024',             #* Your package will have this name
  packages = ['invoicing'],                   #* Name the package again
  version = '1.0.0',                          #* To be increased every time your change your library
  license='MIT',                              # Type of license. More here: https://help.github.com/articles/licensing-a-repository
  description = 'This package can be used to convert Excel invoices to PDF invoices.',    # Short description of your library
  author = 'Cristian Vlaicu Solomon',         # Your name
  author_email = 'airflyt_fly@hotmail.com',   # Your email
  url = 'https://example.com',                # Homepage of your library (e.g., GitHub or your website)
  keywords = ['invoice', 'excel', 'pdf'],     # Keywords users can search on pypi.org
  install_requires=['pandas', 'fpdf', 'openpyxl'],                 # Other 3rd-party libs that pip needs to install
  classifiers=[
    'Development Status :: 3 - Alpha',        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',        # Who is the audience for your library?
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License', # Type a license again
    'Programming Language :: Python :: 3.8',  # Python versions that your library supports
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11',
    'Programming Language :: Python :: 3.12',
  ],
)
