pkgname = "libxpm"
pkgver = "3.5.17"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-open-zfile"]
hostmakedepends = [
    "automake",
    "gettext",
    "pkgconf",
    "slibtool",
    "xorg-util-macros",
]
makedepends = ["xorgproto", "libsm-devel", "libxext-devel", "libxt-devel"]
pkgdesc = "X PixMap library"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/libXpm-{pkgver}.tar.gz"
sha256 = "959466c7dfcfcaa8a65055bfc311f74d4c43d9257900f85ab042604d286df0c6"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libxpm-devel")
def _(self):
    return self.default_devel()
