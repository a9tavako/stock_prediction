from setuptools import setup, find_packages

setup(
    name="stock_prediction",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "flask",
        "flask-cors",
        "numpy",
        "pandas",
        "pydantic",
        "pytest",
        "pytest-cov",
        "python-dotenv",
        "requests"
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "my_stock_prediction=stock_prediction.app:main",
        ],
    },
)
