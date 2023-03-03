from setuptools import setup, find_namespace_packages

setup(
    name='Sorting Files',
    version='0.0.2',
    description='Sorting files by extensions',
    author='Alexander Klobukov',
    author_email='lokist80@gmail.com',
    url='https://github.com/lokist80/GoIT_hw07',
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT",
        "Operation System :: OS Independent"
    ],
    packages=find_namespace_packages(),
    entry_points={'console_scripts': [
        'sortf = clean_folder.clean:main',
    ]}
)
