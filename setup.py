import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='Xdi8Translator',
    version='0.0.3',
    description='Multiway Xdi8 Translator',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/edward-martyr/Xdi8Translator',
    author='Edward Martyr',
    author_email='edwardmartyr@outlook.com',
    license='MIT',
    packages=setuptools.find_packages(),
    zip_safe=False
)