from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='linode-dyndns',
      version='0.1',
      description='Linode dynamic dns',
      long_description=readme(),
      classifiers=[
            'License :: MIT License',
            'Programming Language :: Python :: 2.7',
            'Topic :: Dynamic DNS',
      ],
      keywords='linode dynamic dns dyndns',
      url='https://github.com/bedoron/linode-dydns',
      author='Doron Ben Elazar',
      author_email='b.e.doron@gmail.com',
      license='MIT',
      packages=['linode-dyndns'],
      install_requires=[
          'linode-cli==2.0.6',
      ],
      install_package_data=True,
      zip_safe=False)
