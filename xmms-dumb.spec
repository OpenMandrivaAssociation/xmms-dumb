%define name xmms-dumb
%define oname dumb-xmms
%define version 0.1
%define release %mkrel 8

Summary: MOD player plugin for XMMS based on DUMB
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://prdownloads.sourceforge.net/dumb/%{oname}-%{version}.tar.bz2
Patch0: dumb-xmms-fpic.patch
License: GPLv2+
Group: Sound
Url: http://dumb.sf.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: dumb-devel
BuildRequires: xmms-devel
Requires: xmms

%description
This is a plugin for XMMS that can play IT/XM/S3M/MOD files.

%prep
%setup -q -n %oname
%apply_patches

%build
%make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %buildroot%_libdir/xmms/Input
cp *.so %buildroot%_libdir/xmms/Input/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README
%_libdir/xmms/Input/*.so


