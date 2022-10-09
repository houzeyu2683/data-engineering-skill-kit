
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='desk',
    version='0.0.0',
    author='Greg Hou',
    author_email='houzeyu2683@gmail.com',
    description='Data Engineering Skill Kit',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/houzeyu2683/desk',
    project_urls = {
        "Bug Tracker": "https://github.com/houzeyu2683/desk/issues"
    },
    license='MIT',
    packages=['desk'],
    install_requires=['pandas']
)