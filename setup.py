from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(name='linode-dyndns',
      version='0.1',
      description='Linode dynamic dns',
      long_description=readme(),
      classifiers=[
          'Programming Language :: Python :: 2.7',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Topic :: Internet :: Name Service (DNS)',
          'Topic :: Utilities',

      ],
      keywords='linode dynamic dns dyndns',
      url='https://github.com/bedoron/linode-dydns',
      author='Doron Ben Elazar',
      author_email='b.e.doron@gmail.com',
      license='MIT',
      packages=['linode-dyndns'],
      install_requires=[
          'linode-cli==2.0.6',
          'requests==2.19.1',
      ],
      install_package_data=True,
      zip_safe=False)
