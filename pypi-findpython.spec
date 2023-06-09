#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
#
Name     : pypi-findpython
Version  : 0.3.0
Release  : 3
URL      : https://files.pythonhosted.org/packages/7b/35/8edee643b70783adda91c29c3ba7a48816d03944c63d4e41ef65ec086af6/findpython-0.3.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/7b/35/8edee643b70783adda91c29c3ba7a48816d03944c63d4e41ef65ec086af6/findpython-0.3.0.tar.gz
Summary  : A utility to find python versions on your system
Group    : Development/Tools
License  : MIT
Requires: pypi-findpython-bin = %{version}-%{release}
Requires: pypi-findpython-license = %{version}-%{release}
Requires: pypi-findpython-python = %{version}-%{release}
Requires: pypi-findpython-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(pdm_backend)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# FindPython
_A utility to find python versions on your system._
[![Tests](https://github.com/frostming/findpython/actions/workflows/ci.yml/badge.svg)](https://github.com/frostming/findpython/actions/workflows/ci.yml)
[![PyPI](https://img.shields.io/pypi/v/findpython?logo=python&logoColor=%23cccccc&style=flat-square)](https://pypi.org/project/findpython)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/findpython?logo=python&logoColor=%23cccccc&style=flat-square)](https://pypi.org/project/findpython)
[![pdm-managed](https://img.shields.io/badge/pdm-managed-blueviolet?style=flat-square)](https://github.com/frostming/findpython)

%package bin
Summary: bin components for the pypi-findpython package.
Group: Binaries
Requires: pypi-findpython-license = %{version}-%{release}

%description bin
bin components for the pypi-findpython package.


%package license
Summary: license components for the pypi-findpython package.
Group: Default

%description license
license components for the pypi-findpython package.


%package python
Summary: python components for the pypi-findpython package.
Group: Default
Requires: pypi-findpython-python3 = %{version}-%{release}

%description python
python components for the pypi-findpython package.


%package python3
Summary: python3 components for the pypi-findpython package.
Group: Default
Requires: python3-core
Provides: pypi(findpython)
Requires: pypi(packaging)

%description python3
python3 components for the pypi-findpython package.


%prep
%setup -q -n findpython-0.3.0
cd %{_builddir}/findpython-0.3.0
pushd ..
cp -a findpython-0.3.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1689175651
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-findpython
cp %{_builddir}/findpython-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-findpython/383cfc48616ad432724500a5626c172123f123b2 || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/findpython

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-findpython/383cfc48616ad432724500a5626c172123f123b2

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
