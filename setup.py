from setuptools import setup, find_packages
from causal_ops import __version__

setup(
    name="causal-ops-industrial",
    version=__version__,
    author="Industrial AI Team",
    description="Causal-Ops: 工业非计划停机因果诊断与自愈系统",
    packages=find_packages(),
    install_requires=open("requirements.txt").read().splitlines(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
)