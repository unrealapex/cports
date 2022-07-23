pkgname = "dinit-userservd"
pkgver = "0.1.0_git20220723"
_commit = "dc8c5da96b6dd07e2ad904bda9635476b02dfb70"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["linux-pam-devel"]
pkgdesc = "Dinit user instance manager"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://github.com/chimera-linux/dinit-userservd"
source = f"https://github.com/chimera-linux/{pkgname}/archive/{_commit}.tar.gz"
sha256 = "69208eb923b9419b7be6c1d0a2218003d518de0e0ee693ca2e82d5f281e4e7e3"
