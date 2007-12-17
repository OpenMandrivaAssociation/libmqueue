%define	name	libmqueue
%define	version	4.41
%define	release	%mkrel 2
%define	major	4
%define libname	%mklibname mqueue %{major}

Summary:	POSIX message queues
Name:		%{name}
Version:	%{version}
Release:	%{release}
URL:		http://www.geocities.com/wronski12/posix_ipc/index.html
License:	GPL
Source0:	%{name}-%{version}.tar.bz2
Group:		System/Libraries

%description
POSIX message queues are part of IPC used to exchange messages
between processes

%package -n	%{libname}
Summary:	POSIX message queues
Group:          System/Libraries
Provides:	%{name} = %{version}-%{release}

%description -n	%{libname}
POSIX message queues are part of IPC used to exchange messages
between processes

%package -n	%{libname}-devel
Summary:	Development libraries and header files for libmqueue
Group:		Development/C
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}

%description -n	%{libname}-devel
POSIX message queues are part of IPC used to exchange messages
between processes

These are the development libraries and header files for libmqueue

%prep
%setup -q

%build
%configure
%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}
%{makeinstall_std}

# Remove /usr/include/mqueue.h, it's already in glibc-devel
rm -rf %{buildroot}%{_includedir}/mqueue.h

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%post -n %{libname}-devel -p /sbin/ldconfig
%postun -n %{libname}-devel -p /sbin/ldconfig

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libmqueue.so.*

%files -n %{libname}-devel
%defattr(-,root,root)
#{_includedir}/mqueue.h
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/*.so
%{_mandir}/man?/*
