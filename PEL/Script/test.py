import commands

scpython = "H:\\SystemFile\\Desktop\\PyE-Lang\\PEL\\Script\\SCPythonForPEL\\SCPython.py"
testscript = "H:\\SystemFile\\Desktop\\PyE-Lang\\PEL\\Script\\新建文本文档.txt"
print(f"python {scpython} {testscript}")
a = commands.getoutput(f"python {scpython} {testscript}")
print()