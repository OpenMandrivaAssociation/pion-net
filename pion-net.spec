%define major 4.0
%define libname %mklibname pion-net %{major}
%define libcommon %mklibname pion-common %{major}
%define devname %mklibname %{name} -d

Summary:	C++ library for building lightweight HTTP interfaces
Name:		pion-net
Version:	4.0.9
Release:	1
License:	Boost
Group:		System/Libraries
Url:		http://www.pion.org/projects/pion-network-library
Source0:	http://www.pion.org/files/%{name}-%{version}.tar.bz2
Patch0:		pion-net-cflags.patch
Patch1:		pion-net-pkgconfig.patch
Patch2:		pion-net-gcc47-symbols-lookup.patch
Patch3:		pion-net-boost-linking.patch
Patch4:		pion-net-log4cpp-headers.patch
Patch5:		pion-net-boost-compatibility.patch
Patch6:		pion-net-boost-time-utc.patch
BuildRequires:	doxygen
BuildRequires:	boost-devel
BuildRequires:	bzip2-devel
BuildRequires:	icu-devel
BuildRequires:	pkgconfig(log4cpp)
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(zlib)

%description
Pion Network Library is a C++ framework for building lightweight HTTP
interfaces.

%files
%doc AUTHORS COPYING NEWS TODO
%dir %{_libdir}/pion
%dir %{_libdir}/pion/plugins
%{_libdir}/pion/plugins/*.so

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Shared library for pion-net
Group:		System/Libraries

%description -n %{libname}
This package contains shared library for pion-net.

%files -n %{libname}
%{_libdir}/libpion-net-%{major}.so

#----------------------------------------------------------------------------

%package -n %{libcommon}
Summary:	Shared library for pion-net
Group:		System/Libraries

%description -n %{libcommon}
This package contains shared library for pion-net.

%files -n %{libcommon}
%{_libdir}/libpion-common-%{major}.so

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development files for pion-net
Group:		Development/C++
Requires:	%{libname} = %{EVRD}
Requires:	%{libcommon} = %{EVRD}

%description -n %{devname}
This package contains the pkgconfig, header files, and libraries needed to
develop application that use pion-net.

%files -n %{devname}
%{_includedir}/pion/
%{_libdir}/pkgconfig/*.pc
%{_libdir}/libpion-common.so
%{_libdir}/libpion-net.so

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

%build
./autogen.sh
%configure2_5x \
	--disable-static \
	--with-pic \
	--with-plugins=%{_libdir}/pion/plugins \
	--with-zlib \
	--with-bzlib \
	--with-openssl \
	--with-log4cpp

%make LIBS=-lpthread

%install
%makeinstall_std

# delete example apps
rm -f %{buildroot}%{_bindir}/PionHelloServer
rm -f %{buildroot}%{_bindir}/PionWebServer

