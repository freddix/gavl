Summary:	GMerlin Audio Video Library
Name:		gavl
Version:	1.4.0
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://downloads.sourceforge.net/gmerlin/%{name}-%{version}.tar.gz
# Source0-md5:	2752013a817fbc43ddf13552215ec2c0
URL:		http://gmerlin.sourceforge.net/gavl_frame.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libpng-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GMerlin Audio Video Library.

%package devel
Summary:	Header files for gavl library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This is the package containing the header files for gavl library.

%prep
%setup -q

sed -i -e 's|-O3 -funroll-all-loops -fomit-frame-pointer -ffast-math|%{rpmcflags}|' configure.ac

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-shared		\
	--with-cpuflags=none	\
	--without-doxygen
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_prefix}/share/doc/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS README TODO
%ghost %attr(755,root,root) %{_libdir}/libgavl.so.?
%attr(755,root,root) %{_libdir}/libgavl.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgavl.so
%{_libdir}/libgavl.la
%{_includedir}/gavl
%{_pkgconfigdir}/gavl.pc

