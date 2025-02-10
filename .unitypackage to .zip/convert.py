#!/usr/bin/env python3

import sys
import tarfile
import zipfile
from pathlib import Path

src = sys.argv[1]
dst = Path(src).name + ".zip"

with tarfile.open(sys.argv[1], "r:gz") as tar:
  with zipfile.ZipFile(dst, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as z:
    while True:
      i = tar.next()
      if not i:
        break
      if i.isdir():
        asset = meta = pathname = None
      elif i.isfile() and i.name != ".icon.png":
        name = Path(i.name).name
        if name == "asset":
          asset = tar.extractfile(i).read()
        elif name == "asset.meta":
          meta = tar.extractfile(i).read()
        elif name == "pathname":
          pathname = tar.extractfile(i).read()

        if asset is not None and pathname is not None and meta is not None:
          pathname = pathname.rstrip().decode("utf-8").split("\n")[0]
          print(pathname)
          z.writestr(pathname, asset)
          z.writestr(pathname + ".meta", meta)
          asset = meta = pathname = None
