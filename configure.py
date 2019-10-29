import sys
from pathlib import Path

base_dir = Path(__file__, "../build-system/taler-build-scripts").resolve()

if not base_dir.exists():
    print(f"build system directory (${base_dir}) missing", file=sys.stderr)
    sys.exit(1)

sys.path.insert(0, str(base_dir))

from talerbuildconfig import *

b = BuildConfig()
b.enable_prefix()
b.enable_configmk()
b.add_tool(PythonTool())
b.add_tool(PyBabelTool())
b.add_tool(PosixTool("cp"))
b.add_tool(PosixTool("echo"))
b.add_tool(PosixTool("env"))
b.add_tool(PosixTool("printf"))
b.add_tool(PosixTool("grep"))
b.add_tool(PosixTool("ln"))
b.add_tool(PosixTool("mkdir"))
b.add_tool(PosixTool("rm"))
b.add_tool(PosixTool("sh"))
b.add_tool(PosixTool("msgmerge"))
b.add_tool(PosixTool("tsc"))
b.add_tool(PosixTool("git"))
b.add_tool(PosixTool("docker"))
b.add_tool(PosixTool("sassc"))
#b.add_tool(BrowserTool())
b.run()
