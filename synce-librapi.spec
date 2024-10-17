%define name     synce-librapi
%define shortname rapi
%define release  %mkrel 5
%define version  0.10.0

%define major 2

%define libname %mklibname %shortname %major

Summary: SynCE: Remote Application Programming Interface (RAPI) library
Name: %{name}
Version: %{version}
Release: %{release}
License: MIT
Group: System/Libraries
Source: %{name}%{major}-%{version}.tar.bz2
URL: https://synce.sourceforge.net/
Buildroot: %{_tmppath}/%name-root
BuildRequires: libsynce-devel = %{version}
BuildRequires: python-devel
BuildRequires: python-pyrex
Conflicts: synce < 0.9.3

%description
Librapi is part of the SynCE project:

  http://synce.sourceforge.net/

The RAPI library is an open source implementation that works like RAPI.DLL,
available on Microsoft operating systems. The library makes it possible to make
remote calls to a computer running Pocket PC. Documentation for the RAPI calls
is available at this address:

http://msdn.microsoft.com/library/default.asp?url=/library/en-us/wcesdkr/htm/_wcesdk_CeRapiInit.asp

%package -n %libname-python
Group: System/Libraries
Summary: SynCE: Remote Application Programming Interface (RAPI) library
Provides: %{shortname}-python = %{version}-%{release}
Provides: lib%{shortname}-python = %{version}-%{release}
Requires: %{libname} = %{version}-%{release}
Requires: python

%description -n %libname-python
Librapi is part of the SynCE project:

  http://synce.sourceforge.net/

The RAPI library is an open source implementation that works like RAPI.DLL,
available on Microsoft operating systems. The library makes it possible to make
remote calls to a computer running Pocket PC. Documentation for the RAPI calls
is available at this address:

http://msdn.microsoft.com/library/default.asp?url=/library/en-us/wcesdkr/htm/_wcesdk_CeRapiInit.asp

%package -n %libname
Group: System/Libraries
Summary: SynCE: Remote Application Programming Interface (RAPI) library
Provides: lib%{shortname} = %{version}-%{release}
Conflicts: %{_lib}synce0 < 0.9.3

%description -n %libname
Librapi is part of the SynCE project:

  http://synce.sourceforge.net/

The RAPI library is an open source implementation that works like RAPI.DLL,
available on Microsoft operating systems. The library makes it possible to make
remote calls to a computer running Pocket PC. Documentation for the RAPI calls
is available at this address:

http://msdn.microsoft.com/library/default.asp?url=/library/en-us/wcesdkr/htm/_wcesdk_CeRapiInit.asp

%package -n %libname-devel
Group: System/Libraries
Summary: SynCE: Remote Application Programming Interface (RAPI) library
Provides: lib%{shortname}-devel = %{version}-%{release}
Requires: %{libname} = %{version}-%{release}
Conflicts: %{_lib}synce0-devel < 0.9.3

%description -n %libname-devel
Librapi is part of the SynCE project:

  http://synce.sourceforge.net/

The RAPI library is an open source implementation that works like RAPI.DLL,
available on Microsoft operating systems. The library makes it possible to make
remote calls to a computer running Pocket PC. Documentation for the RAPI calls
is available at this address:

http://msdn.microsoft.com/library/default.asp?url=/library/en-us/wcesdkr/htm/_wcesdk_CeRapiInit.asp

%prep
%setup -q -n lib%{shortname}%{major}-%{version}

%build
%configure2_5x --with-libsynce=%{_prefix}
%make

%install
rm -rf %buildroot
%makeinstall_std

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files
%defattr(-,root,root)
%doc README TODO
%{_bindir}/*
%{_mandir}/man1/*

%files -n %{libname}
%defattr(-,root,root)
%_libdir/librapi.so.*

%files -n %{libname}-devel
%defattr(-,root,root)
%_libdir/librapi.so
%_libdir/librapi.a
%_libdir/librapi.la
%{_includedir}/rapi.h
%_libdir/pkgconfig/*.pc

%files -n %{libname}-python
%python_sitearch/pyrapi2.*
