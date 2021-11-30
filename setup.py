from setuptools import setup
from version import get_git_version

try:
    version = get_git_version()
    assert version is not None
except (AttributeError, AssertionError):
    version = '0.0.0'

setup(name='testutils',
      version=version,
      url='http://github.com/ovrocaltech/test-deploy',
      packages=['testutils'],
      package_data = {
          },
      tests_require=[
          ],
      entry_points='''
      ''',      
      zip_safe=False)
