from setuptools import setup, find_packages

# requerments.txt path
req_file = 'requirements.txt'
with open(req_file) as f:
    requirements = f.read().splitlines()

readme_file = 'README.md'
with open(readme_file) as f:
    readme = f.read()

long_description = readme + '\n\n'

classifiers = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
]

setup(
    name='jb-wattpad-scraper',
    version='0.0.40',
    description='Get wattpad stories and chapters, and download them as ebook',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/josyelbuenos/jb-wattpad-scraper',
    author='Josyel Buenos',
    author_email='josyelbuenos@gmail.com',
    license='MIT',
    classifiers=classifiers,
    packages=find_packages(),
    install_requires=requirements,
)