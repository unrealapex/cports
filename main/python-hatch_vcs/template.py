pkgname = "python-hatch_vcs"
pkgver = "0.5.0"
pkgrel = 0
build_style = "python_pep517"
make_check_args = [
    "--deselect",
    "tests/test_build.py::test_basic",
    "--deselect",
    "tests/test_build.py::test_write",
    "--deselect",
    "tests/test_build.py::test_fallback",
    "--deselect",
    "tests/test_build.py::test_root",
    "--deselect",
    "tests/test_build.py::test_metadata",
]
hostmakedepends = ["python-build", "python-installer", "python-hatchling"]
depends = ["python-hatchling", "python-setuptools_scm"]
checkdepends = ["python-pytest", "git", *depends]
pkgdesc = "Hatch plugin for VCS versioning"
license = "MIT"
url = "https://github.com/ofek/hatch-vcs"
source = f"$(PYPI_SITE)/h/hatch_vcs/hatch_vcs-{pkgver}.tar.gz"
sha256 = "0395fa126940340215090c344a2bf4e2a77bcbe7daab16f41b37b98c95809ff9"
# cycle
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.txt")
