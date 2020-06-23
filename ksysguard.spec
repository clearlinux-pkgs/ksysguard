#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xEC94D18F7F05997E (jr@jriddell.org)
#
Name     : ksysguard
Version  : 5.19.2
Release  : 44
URL      : https://download.kde.org/stable/plasma/5.19.2/ksysguard-5.19.2.tar.xz
Source0  : https://download.kde.org/stable/plasma/5.19.2/ksysguard-5.19.2.tar.xz
Source1  : https://download.kde.org/stable/plasma/5.19.2/ksysguard-5.19.2.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GFDL-1.2 GPL-2.0
Requires: ksysguard-bin = %{version}-%{release}
Requires: ksysguard-data = %{version}-%{release}
Requires: ksysguard-lib = %{version}-%{release}
Requires: ksysguard-license = %{version}-%{release}
Requires: ksysguard-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : glibc-dev
BuildRequires : kdoctools-dev
BuildRequires : ki18n-dev
BuildRequires : libksysguard-dev

%description
What is KSysGuard?
------------------
KSysGuard is a program to monitor various elements of your system, or any
other remote system with the KSysGuard daemon (ksysgardd) installed.
Currently the daemon has been ported to Linux, FreeBSD, Irix, NetBSD,
OpenBSD, Solaris and Tru64 with varying degrees of completion.

%package bin
Summary: bin components for the ksysguard package.
Group: Binaries
Requires: ksysguard-data = %{version}-%{release}
Requires: ksysguard-license = %{version}-%{release}

%description bin
bin components for the ksysguard package.


%package data
Summary: data components for the ksysguard package.
Group: Data

%description data
data components for the ksysguard package.


%package dev
Summary: dev components for the ksysguard package.
Group: Development
Requires: ksysguard-lib = %{version}-%{release}
Requires: ksysguard-bin = %{version}-%{release}
Requires: ksysguard-data = %{version}-%{release}
Provides: ksysguard-devel = %{version}-%{release}
Requires: ksysguard = %{version}-%{release}

%description dev
dev components for the ksysguard package.


%package doc
Summary: doc components for the ksysguard package.
Group: Documentation

%description doc
doc components for the ksysguard package.


%package lib
Summary: lib components for the ksysguard package.
Group: Libraries
Requires: ksysguard-data = %{version}-%{release}
Requires: ksysguard-license = %{version}-%{release}

%description lib
lib components for the ksysguard package.


%package license
Summary: license components for the ksysguard package.
Group: Default

%description license
license components for the ksysguard package.


%package locales
Summary: locales components for the ksysguard package.
Group: Default

%description locales
locales components for the ksysguard package.


%prep
%setup -q -n ksysguard-5.19.2
cd %{_builddir}/ksysguard-5.19.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1592940434
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1592940434
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ksysguard
cp %{_builddir}/ksysguard-5.19.2/COPYING %{buildroot}/usr/share/package-licenses/ksysguard/7c203dee3a03037da436df03c4b25b659c073976
cp %{_builddir}/ksysguard-5.19.2/COPYING.DOC %{buildroot}/usr/share/package-licenses/ksysguard/bd75d59f9d7d9731bfabdc48ecd19e704d218e38
pushd clr-build
%make_install
popd
%find_lang ksysguard
%find_lang ksysguard_plugins_global
%find_lang ksysguard_plugins_process

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/kstatsviewer
/usr/bin/ksysguard
/usr/bin/ksysguardd
/usr/bin/ksystemstats

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.ksysguard.desktop
/usr/share/dbus-1/services/org.kde.ksystemstats.service
/usr/share/icons/hicolor/16x16/apps/computer.png
/usr/share/icons/hicolor/16x16/apps/daemon.png
/usr/share/icons/hicolor/16x16/apps/kdeapp.png
/usr/share/icons/hicolor/16x16/apps/kernel.png
/usr/share/icons/hicolor/16x16/apps/ksysguardd.png
/usr/share/icons/hicolor/16x16/apps/running.png
/usr/share/icons/hicolor/16x16/apps/shell.png
/usr/share/icons/hicolor/16x16/apps/unknownapp.png
/usr/share/icons/hicolor/16x16/apps/waiting.png
/usr/share/knotifications5/ksysguard.notifyrc
/usr/share/knsrcfiles/ksysguard.knsrc
/usr/share/ksysguard/ProcessTable.sgrd
/usr/share/ksysguard/SystemLoad2.sgrd
/usr/share/kxmlgui5/ksysguard/ksysguardui.rc
/usr/share/metainfo/org.kde.ksysguard.appdata.xml

%files dev
%defattr(-,root,root,-)
/usr/lib64/libksgrdbackend.so

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/ksysguard/index.cache.bz2
/usr/share/doc/HTML/ca/ksysguard/index.docbook
/usr/share/doc/HTML/de/ksysguard/index.cache.bz2
/usr/share/doc/HTML/de/ksysguard/index.docbook
/usr/share/doc/HTML/en/ksysguard/index.cache.bz2
/usr/share/doc/HTML/en/ksysguard/index.docbook
/usr/share/doc/HTML/et/ksysguard/index.cache.bz2
/usr/share/doc/HTML/et/ksysguard/index.docbook
/usr/share/doc/HTML/id/ksysguard/index.cache.bz2
/usr/share/doc/HTML/id/ksysguard/index.docbook
/usr/share/doc/HTML/it/ksysguard/index.cache.bz2
/usr/share/doc/HTML/it/ksysguard/index.docbook
/usr/share/doc/HTML/nl/ksysguard/index.cache.bz2
/usr/share/doc/HTML/nl/ksysguard/index.docbook
/usr/share/doc/HTML/pt/ksysguard/index.cache.bz2
/usr/share/doc/HTML/pt/ksysguard/index.docbook
/usr/share/doc/HTML/pt_BR/ksysguard/index.cache.bz2
/usr/share/doc/HTML/pt_BR/ksysguard/index.docbook
/usr/share/doc/HTML/ru/ksysguard/index.cache.bz2
/usr/share/doc/HTML/ru/ksysguard/index.docbook
/usr/share/doc/HTML/sv/ksysguard/index.cache.bz2
/usr/share/doc/HTML/sv/ksysguard/index.docbook
/usr/share/doc/HTML/uk/ksysguard/index.cache.bz2
/usr/share/doc/HTML/uk/ksysguard/index.docbook

%files lib
%defattr(-,root,root,-)
/usr/lib64/libkdeinit5_ksysguard.so
/usr/lib64/qt5/plugins/ksysguard/ksysguard_ksgrd.so
/usr/lib64/qt5/plugins/ksysguard/ksysguard_plugin_nvidiaglobal.so
/usr/lib64/qt5/plugins/ksysguard/process/ksysguard_plugin_nvidia.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ksysguard/7c203dee3a03037da436df03c4b25b659c073976
/usr/share/package-licenses/ksysguard/bd75d59f9d7d9731bfabdc48ecd19e704d218e38

%files locales -f ksysguard.lang -f ksysguard_plugins_global.lang -f ksysguard_plugins_process.lang
%defattr(-,root,root,-)

