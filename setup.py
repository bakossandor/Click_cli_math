from setuptools import setup


setup(
    name="math1",
    version="0.1",
    py_modules=["playing_with_math"],
    install_requires=[
        "Click",
    ],
    entry_points="""
        [console_scripts]
        math1=playing_with_math:cli
    """
)