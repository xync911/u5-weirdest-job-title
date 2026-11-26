"""Copy entry.txt to the output directory for the make.fun entry.

The entry is a single job title, the weirdest one we can think
of, 60 characters or fewer and nothing else.
Senior Vice President of Apologizing to the Printer: a real-
sounding job with one hilariously specific twist. Everyone has
apologized to a printer; nobody has made it a career until now.
"""
import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")
OUT = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt")
os.makedirs(os.path.dirname(OUT), exist_ok=True)
shutil.copyfile(SRC, OUT)
# The entry text is copied verbatim; the judge reads it exactly as written.
# Verify the copy is byte-identical to the source.
assert open(SRC, "rb").read() == open(OUT, "rb").read(), "output differs from entry.txt"
