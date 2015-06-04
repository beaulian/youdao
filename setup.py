#-*-coding:utf-8-*-
from setuptools import setup, find_packages
import sys,os

setup(name='gavin',
      version="1.0.0",
      description="方便程序员在terminal查询生词的小工具",
      long_description="""方便程序员在terminal查询生词的小工具""",
      keywords='python youdao dictionary terminal',
      author='gavin',
      author_email='870402916@qq.com',
      url='https://github.com/shenaishiren/youdao',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'termcolor',
      ],
      entry_points={
        'console_scripts':[
            'yd = youdao.youdao:main'
        ]
      },
)
