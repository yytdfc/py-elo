import sys

# Available at setup time due to pyproject.toml
from pybind11 import get_cmake_dir
from pybind11.setup_helpers import Pybind11Extension, build_ext
from setuptools import setup

__version__ = "0.0.1"

# The main interface is through Pybind11Extension.
# * You can add cxx_std=11/14/17, and then build_ext can be removed.
# * You can set include_pybind11=false to add the include directory yourself,
#   say from a submodule.
#
# Note:
#   Sort input source files if you glob sources to ensure bit-for-bit
#   reproducible builds (https://github.com/pybind/python_example/pull/53)

ext_modules = [
    Pybind11Extension("bayeselo",
        [   "src/main.cpp",
            "./BayesElo/version.cpp",
            "./BayesElo/pgnlex.cpp",
            "./BayesElo/str.cpp",
            "./BayesElo/const.cpp",
            "./BayesElo/date.cpp",
            "./BayesElo/pgnstr.cpp",
            "./BayesElo/move.cpp",
            "./BayesElo/consolui.cpp",
            "./BayesElo/clktimer.cpp",
            "./BayesElo/CTimeIO.cpp",
            "./BayesElo/chtime.cpp",
            "./BayesElo/readstr.cpp",
            "./BayesElo/ReadLineToString.cpp",
            "./BayesElo/CVector.cpp",
            "./BayesElo/CMatrix.cpp",
            "./BayesElo/CMatrixIO.cpp",
            "./BayesElo/CLUDecomposition.cpp",
            "./BayesElo/CBradleyTerry.cpp",
            "./BayesElo/CCDistribution.cpp",
            "./BayesElo/CCDistributionCUI.cpp",
            "./BayesElo/CCondensedResults.cpp",
            "./BayesElo/CDistribution.cpp",
            "./BayesElo/CDistributionCollection.cpp",
            "./BayesElo/CEloRatingCUI.cpp",
            "./BayesElo/CJointBayesian.cpp",
            "./BayesElo/CResultSet.cpp",
            "./BayesElo/CResultSetCUI.cpp",
            "./BayesElo/EloDataFromFile.cpp",
            "./BayesElo/CPredictionCUI.cpp",
        ],
        include_dirs = ["."],
        # Example: passing in the version to the compiled code
        define_macros = [('VERSION_INFO', __version__)],
        ),
]

setup(
    name="bayeselo",
    version=__version__,
    author="Sylvain Corlay",
    author_email="sylvain.corlay@gmail.com",
    url="https://github.com/pybind/python_example",
    description="A test project using pybind11",
    long_description="",
    ext_modules=ext_modules,
    extras_require={"test": "pytest"},
    # Currently, build_ext only provides an optional "highest supported C++
    # level" feature, but in the future it may provide more features.
    cmdclass={"build_ext": build_ext},
    zip_safe=False,
    python_requires=">=3.7",
)
