import sys
from cx_Freeze import setup, Executable
import senha_lib
import banner

"""
base = None
if sys.platform == "win32":
    base = "Win32GUI"
"""
executables = [
        Executable("save_senha.py", base=None)
]

buildOptions = dict(
        packages = [],
        includes = ["senha_lib", "banner"],
        include_files = [],
        excludes = []
)




setup(
    name = "Save senha",
    version = "1.0",
    description = "Gerenciador de senhas by Hydra-07",
    options = dict(build_exe = buildOptions),
    executables = executables
 )
