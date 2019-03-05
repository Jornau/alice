from setuptools import setup, find_packages

setup(name='alice',
      version='0.1',
      description='Yandex.Dialogs non-official package.',
      long_description='Processing requests and sending responses for Yandex.Dialogs API.',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: MIT License',
        'Programming Language :: Python :: 3.7.2',
        'Topic :: API :: Bots',
      ],
      keywords='yandex dialogs alice skills',
      url='http://github.com/storborg/funniest',
      author='Alexander Surkov',
      author_email='jornau@yandex.ru',
      license='MIT',
      packages=find_packages(),
      install_requires=[
          'requests',
          'json'
      ],
      zip_safe=False)