Summary:	Simple GUI configuration tool for beryl
Summary(pl.UTF-8):   Proste graficzne narzędzie konfiguracyjne dla beryla
Name:		beryl-settings-simple
Version:	0.1.9999.1
Release:	1
Epoch:		1
License:	GPL v2+
Group:		X11/Window Managers/Tools
Source0:	http://releases.beryl-project.org/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	f34cfc2d55a7bd2c317f890262dde673
URL:		http://beryl-project.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake >= 1:1.9
BuildRequires:	beryl-core-devel >= 1:0.1.9999.1
BuildRequires:	beryl-settings-bindings-devel >= 1:0.1.9999.1
BuildRequires:	gtk+2-devel >= 2:2.8.0
BuildRequires:	intltool >= 0.35.0
BuildRequires:	pkgconfig
BuildRequires:	python-pygtk-devel >= 2.0
Requires:	beryl-core >= 1:0.1.9999.1
Requires:	beryl-settings-bindings >= 1:0.1.9999.1
Requires:	python-pygtk-gtk >= 2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains a simple GUI configuration tool to configure
beryl's plugins and the composite window manager.

%description -l pl.UTF-8
Ten pakiet zawiera proste graficzne narzędzie do konfiguracji wtyczek
i zarządcy okien beryla.

%prep
%setup -q
echo '#beryl version header' > VERSION
echo VERSION=0.1.9999.1 >> VERSION

%build
%{__glib_gettextize}
%{__intltoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/beryl-settings-simple
%{_datadir}/beryl-settings-simple
%{_desktopdir}/beryl-settings-simple.desktop
