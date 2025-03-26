pkgname = "faust"
pkgver = "2.79.3"
pkgrel = 0
archs = ["aarch64", "ppc64le", "ppc64", "riscv64", "x86_64"]
build_style = "makefile"
make_build_args = ["GENERATOR=Ninja"]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
depends = ["bash"]
pkgdesc = "Functional programming language for real-time signal processing"
license = "GPL-2.0-or-later"
url = "https://faust.grame.fr"
source = f"https://github.com/grame-cncm/faust/releases/download/{pkgver}/faust-{pkgver}.tar.gz"
sha256 = "ca2171cb136f135960be10fee2c1728304865a5d5190e9a03cace88b4936c558"
# skip execinfo
tool_flags = {"CXXFLAGS": ["-DALPINE"]}
# no check target
options = ["!cross", "!check"]


def post_install(self):
    self.rename("usr/share/faust", "usr/lib/faust", relative=False)
    self.install_link("usr/share/faust", "../lib/faust")
    self.uninstall("usr/lib/libOSCFaust.a")
    self.uninstall("usr/lib/ios-libsndfile.a")
    self.uninstall("usr/lib/faust/max-msp/sndfile")
    self.uninstall("usr/lib/faust/android/app/lib/libsndfile")
