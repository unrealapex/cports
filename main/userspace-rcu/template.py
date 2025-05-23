pkgname = "userspace-rcu"
pkgver = "0.15.1"
pkgrel = 0
build_style = "gnu_configure"
make_check_args = ["-j1"]
hostmakedepends = ["automake", "pkgconf", "slibtool"]
pkgdesc = "Userspace RCU library"
license = "LGPL-2.1-or-later"
url = "https://liburcu.org"
source = f"https://www.lttng.org/files/urcu/userspace-rcu-{pkgver}.tar.bz2"
sha256 = "98d66cc12f2c5881879b976f0c55d10d311401513be254e3bd28cf3811fb50c8"
tool_flags = {"CFLAGS": ["-DLITTLE_ENDIAN=4321", "-DBIG_ENDIAN=1234"]}
# XXX: tests pass when run outside the suite...
options = ["!check"]

if self.profile().endian == "big":
    tool_flags["CFLAGS"] += ["-DBYTE_ORDER=1234"]
else:
    tool_flags["CFLAGS"] += ["-DBYTE_ORDER=4321"]


@subpackage("userspace-rcu-devel")
def _(self):
    return self.default_devel(extra=["usr/share/doc"])
