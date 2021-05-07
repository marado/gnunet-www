import sys
from pathlib import Path
from talerbuildconfig import *

b = BuildConfig()
b.enable_prefix()
b.enable_configmk()
b.use(Option("variant", "Variant (used as output directory)"))

# Base URL for the site.  Per default, the URL is the protocol-relative
# root path.
b.use(Option("baseurl", "Base URL that the site will run on", default="//", required=False))
b.add_tool(PythonTool())
b.add_tool(PyBabelTool())
b.add_tool(PosixTool("cp"))
b.add_tool(PosixTool("echo"))
b.add_tool(PosixTool("env"))
b.add_tool(PosixTool("printf"))
b.add_tool(PosixTool("grep"))
b.add_tool(PosixTool("mkdir"))
b.add_tool(PosixTool("rm"))
b.add_tool(PosixTool("sh"))
b.add_tool(PosixTool("msgmerge"))
b.add_tool(PosixTool("git"))
b.add_tool(BrowserTool())
b.run()
