import sys
from numpy.distutils.core import Extension, setup
from mkldiscover import mkl_exists

__author__ = "Marco Krummenacher"
__copyright__ = "Copyright 2022"
__credits__ = ["Marco Krummenacher (2022) https://github.com/KrumaKruma/bazant_ase_calculator"]
__license__ = "GNU"
__version__ = "1.0"
__maintainer__ = "Marco Krummenacher"
__email__ = "marcokrummenacher2@gmail.com"
__status__ = "Beta"
__description__ = "ASE Bazant Force Field"
__url__ = "https://github.com/KrumaKruma/bazant_ase_calculator"


FORTRAN = "f90"

# GNU (default)
COMPILER_FLAGS = ["-O3", "-fopenmp", "-m64"]
LINKER_FLAGS = ["-lgomp"]
MATH_LINKER_FLAGS = ["-lblas", "-llapack"]

# # UNCOMMENT TO FORCE LINKING TO MKL with GNU compilers:
if mkl_exists(verbose=True):
    LINKER_FLAGS = ["-lgomp", " -lpthread", "-lm", "-ldl"]
    MATH_LINKER_FLAGS = ["-L${MKLROOT}/lib/intel64", "-lmkl_rt"]

# # For clang without OpenMP: (i.e. most Apple/mac system)
if sys.platform == "darwin" and all(["gnu" not in arg for arg in sys.argv]):
    COMPILER_FLAGS = ["-O3", "-m64"]
    LINKER_FLAGS = []
    MATH_LINKER_FLAGS = ["-lblas", "-llapack"]

# # Intel
if any(["intelem" in arg for arg in sys.argv]):
    COMPILER_FLAGS = ["-O3", "-qopenmp"]
    LINKER_FLAGS = ["-liomp5", " -lpthread", "-lm", "-ldl"]
    MATH_LINKER_FLAGS = ["-L${MKLROOT}/lib/intel64", "-lmkl_rt"]


bazant_module = Extension(name = 'bazant',
                          sources = [
                                'asebazant/bazant_lib.f90',
                            ],
                          extra_f90_compile_args = COMPILER_FLAGS,
                          extra_f77_compile_args = COMPILER_FLAGS,
                          extra_compile_args = COMPILER_FLAGS ,
                          extra_link_args = LINKER_FLAGS + MATH_LINKER_FLAGS,
                          language = FORTRAN)#,
                          #f2py_options=['--quiet'])



# use README.md as long description
def readme():
    with open('README.md') as f:
        return f.read()



def setup_pepytools():

    setup(

        name="asebazant",
        packages=['asebazant'],

        # metadata
        version=__version__,
        author=__author__,
        author_email=__email__,
        platforms = 'Any',
        description = __description__,
        long_description = readme(),
        keywords = ['Atomic Simulation Environment', 'ASE extension', 'Silicon Force Field'],
        classifiers = [],
        url = __url__,

        # set up package contents

        ext_package = 'asebazant',
        ext_modules = [
            bazant_module
        ],

        install_requires=[
            'numpy',
            'ase'
        ]
)

if __name__ == '__main__':
    setup_pepytools()

