pkgname = "parallel"
pkgver = "20250622"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake"]
depends = ["perl"]
pkgdesc = "Shell tool for executing jobs in parallel"
license = "GPL-3.0-or-later"
url = "https://www.gnu.org/software/parallel"
source = f"https://ftp.gnu.org/gnu/parallel/parallel-{pkgver}.tar.bz2"
sha256 = "69f578cf11f1b124ba3c2b673a16641debe63aeb3d2ac4cec5ad65f8a53d489b"
