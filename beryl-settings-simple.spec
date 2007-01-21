Summary:	simple gui configuration tool for beryl
Name:		beryl-settings-simple
Version:	0.1.99.2
Release:	1
Epoch:		1
License:	GPL v2+
Group:		X11/Window Managers/Tools
Source0:	http://releases.beryl-project.org/0.1.99.2/%{name}-%{version}.tar.bz2
# Source0-md5:	5d94ca4f8e85fad68029a11fb7cc9cff
URL:		http://beryl-project.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake >= 1:1.9
BuildRequires:	beryl-core-devel >= 1:0.1.99.2
BuildRequires:	beryl-settings >= 1:0.1.99.2
BuildRequires:	gtk+2-devel >= 2:2.8.0
BuildRequires:	intltool >= 0.35.0
BuildRequires:	pkgconfig
BuildRequires:	python-Pyrex
Requires:	beryl-core >= 1:0.1.99.2
Requires:	beryl-settings >= 1:0.1.99.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains a simple gui configuration tool to configure
Beryl's plugins and the composite window manager.
 
%prep
%setup -q
echo '#beryl version header' > VERSION
echo VERSION=0.1.99.2 >> VERSION

%build
autoreconf -v --install
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
    DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/beryl-settings-simple
%{_datadir}/beryl-settings-simple/
