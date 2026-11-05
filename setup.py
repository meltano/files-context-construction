from setuptools import setup, find_packages

setup(
    name="files-context-construction",
    version="0.1.0",
    description="Meltano Cloud industry context for construction: datasets for AI assistants and analysts.",
    packages=find_packages(),
    # bundle/ is copied verbatim into the workspace repository; ship every file under it
    include_package_data=True,
)
