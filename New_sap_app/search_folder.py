import os
import subprocess


def is_tool(prog):
    for dir in os.environ['PATH'].split(os.pathsep):
        if os.path.exists(os.path.join(dir, prog)):
            try:
                subprocess.call([os.path.join(dir, prog)],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT)
            except OSError as e:
                return False
            return True
    return False


print(is_tool("Python"))