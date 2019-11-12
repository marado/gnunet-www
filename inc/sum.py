def sha256sum(_):
    sha256 = hashlib.sha256()
    with io.open(_, mode="rb") as fd:
        content = fd.read()
        sha256.update(content)
    return sha256.hexdigest()


def walksum(_):
    sha256 = hashlib.sha256()
    x = Path(_)
    if not x.exists():
        return -1
    try:
        for root, directories, files in os.walk(_):
            for names in sorted(files):
                filepath = os.path.join(root, names)
                try:
                    fl = open(filepath, 'rb')
                except:
                    fl.close()
                    continue
                while 1:
                    buf = fl.read(4096)
                    if not buf:
                        break
                    sha256.update(hashlib.sha256(buf).hexdigest())
                fl.close()
    except:
        import traceback
        traceback.print_exc()
        return -2
    return sha256.hexdigest()


