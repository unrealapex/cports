pkgname = "python-lsp-server"
pkgver = "1.12.2"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools_scm",
]
depends = [
    "python-docstring-to-markdown",
    "python-jedi",
    "python-lsp-jsonrpc",
    "python-pluggy",
    "python-ujson",
]
checkdepends = [
    "python-flaky",
    "python-pytest-xdist",
    *depends,
]
pkgdesc = "Python LSP server"
license = "MIT"
url = "https://github.com/python-lsp/python-lsp-server"
source = f"$(PYPI_SITE)/p/python-lsp-server/python_lsp_server-{pkgver}.tar.gz"
sha256 = "fea039a36b3132774d0f803671184cf7dde0c688e7b924f23a6359a66094126d"


def init_check(self):
    self.make_check_args += [
        f"--numprocesses={self.make_jobs}",
        "--dist=worksteal",
        # skipping all these deps
        "--ignore=test/plugins",
        "-k",
        "not test_set_flake8_using_workspace_did_change_configuration"
        + " and not test_workspace_loads_pycodestyle_config"
        + " and not test_notebook_document__did_change"
        + " and not test_notebook_document__did_open",
    ]


def post_install(self):
    self.install_license("LICENSE")
