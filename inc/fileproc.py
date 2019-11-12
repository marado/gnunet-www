from pathlib import Path

def copy_files(kind, conf, locale, inlist, ptarget):
    o = Path(ptarget)
    for item in conf[inlist]:
        i = Path(kind + "/" + item["file"])
        # print(i)
        for t in item["targets"]:
            d_loc = o / locale / t
            d = o / t
            # print(d)
            if i.is_file() is not False:
                d_loc.write_text(i.read_text())
                print("copied " + str(i) + " to " + str(d_loc) + "...")
                d.write_text(i.read_text())
                print("copied " + str(i) + " to " + str(d) + "...")


def rm_rf(directory):
    directory = Path(directory)
    for child in directory.glob('*'):
        if child.is_file():
            child.unlink()
        else:
            rm_rf(child)
    # directory.rmdir()


def fileop(infile, outfile, action):
    """
    infile: inputfile, Path object
    outfile: outputfile, Path object
    action: action if any, String
    """
    i = Path(infile)
    o = Path(outfile)
    outdir = Path("rendered")
    if i.is_file() is not False:
        if action == "copy":
            # Write content of i to o.
            o.write_text(i.read_text())
        if action == "link":
            o.symlink_to(i)


def write_name(filename, infile, locale, replacer):
    return "./rendered/" + locale + "/" + infile.replace(replacer,
                                                         '').rstrip(".j2")


def localized(filename, locale, *args):
    if len(args) == 0:
        return "../" + locale + "/" + filename
    ext = kwargs.get('ext', None)
    if ext is not None:
        lf = filename + "." + locale + "." + ext
        lp = Path(lf)
        if locale == "en" or not lp.is_file():
            return "../" + filename + "." + ext
        else:
            return "../" + lf


# This generates and switches sites generations, preventing
# in-place modification of the website.
# * save old generation directory name
# * jinja2 creates content in "rendered" (happened before calling this function)
# * calculate sum of "rendered"
# * move "rendered" to out/$sum
# * remove symlink "html_dir"
# * symlink out/$sum to "html_dir"
# * delete old generation directory
def generation_dir(htmldir):
    oldgen = Path(htmldir).resolve()
    # precondition: jinja2 has created the files in "rendered".
    newgen = Path("rendered")
    newgen_sum = walksum(newgen)
    outdir = Path("out")
    outdir.mkdir(parents=True, exist_ok=True)
    newgen_target = Path("out") / newgen_sum
    newgen.rename(newgen_target)
    html = Path(htmldir)
    html.unlink()
    fileop(newgen, html, "link")
    rm_rf(oldgen)
