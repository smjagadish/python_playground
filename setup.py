from setuptools import setup, find_packages


setup(
    name="mypackage",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        # List your package dependencies here
    ],
    py_modules=["main"],  # needed since main is in project root
    include_package_data=True,  # needed as i want the data.txt file to also be included when packaging
    # package_data= {'org': ['data.txt']}, #not needed
    # data_files=[('', ['data.txt'])],
    entry_points={
        "console_scripts": ["my_script = main:call", "my_sum = excercises.sum_count:calc"]
    },  # module:function name
    author="Your Name",
    author_email="your.email@example.com",
    description="A simple example package",
    url="https://github.com/yourusername/my_package",
)
