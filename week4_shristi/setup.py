from setuptools import setup, Extension
from pybind11.setup_helpers import Pybind11Extension, build_ext

ext_modules = [
    Pybind11Extension(
        "example_pybind",
        ["example_pybind.cpp"],
        include_dirs=["/usr/local/include", "/Library/Frameworks/Python.framework/Versions/3.11/include/python3.11"],  # Adjust paths if needed
    ),
]

setup(
    name="example_pybind",
    ext_modules=ext_modules,
    cmdclass={"build_ext": build_ext},
)
