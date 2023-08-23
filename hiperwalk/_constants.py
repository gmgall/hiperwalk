__version__ = '2.0b0'

from sys import modules as sys_modules

__USING_PDB__ = 'pdb' in sys_modules
__GENERATING_DOCS__ = 'sphinx' in sys_modules
# ignores debug print messages when generating docs
__DEBUG__ = __debug__ and __USING_PDB__ and not __GENERATING_DOCS__

PYNEBLINA_IMPORT_ERROR_MSG =  (
    "Could not import pyneblina interface. "
    + "Do you have neblina-core and pyneblina installed?"
    + "\n#######################\n"
    + "Continuing without hpc."
    + "\n#######################\n" )
