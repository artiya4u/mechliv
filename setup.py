import sys

from setuptools import setup
from setuptools import find_packages

requirements = ['requests']
if sys.version_info < (2, 7):
    requirements.append('argparse')

setup(name='mechliv',
      version='0.0.1',
      description='Mechanical keyboard sound',
      long_description='Play mechanical keyboard sound in your System Tray.',
      keywords='mechanical keyboard mechliv',
      url='https://github.com/artiya4u/mechliv',
      author='Artiya Thinkumpang',
      author_email='artiya4u@gmail.com',
      license='MIT',
      packages=find_packages(),
      package_data={
          'mechliv.data': ['icon.png', 'press.wav']
      },
      install_requires=[
          'requests>=2.2.1',
          'pynput>=1.5.2',
          'playsound>=1.2.2'
      ],
      entry_points={
          'console_scripts': ['mechliv = mechliv:main'],
      },
      zip_safe=False)
