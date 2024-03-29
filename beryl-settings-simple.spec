Summary:	Simple GUI configuration tool for beryl
Summary(pl.UTF-8):	Proste graficzne narzędzie konfiguracyjne dla beryla
Name:		beryl-settings-simple
Version:	0.2.1
Release:	1
Epoch:		1
License:	GPL v2+
Group:		X11/Window Managers/Tools
Source0:	http://releases.beryl-project.org/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	2476d9618a07ec2d7acc117417f77a3b
Patch0:		%{name}-desktop.patch
URL:		http://beryl-project.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake >= 1:1.9
BuildRequires:	beryl-core-devel >= 1:%{version}
BuildRequires:	beryl-settings-bindings-devel >= 1:%{version}
BuildRequires:	gtk+2-devel >= 2:2.8.0
BuildRequires:	intltool >= 0.35.0
BuildRequires:	pkgconfig
BuildRequires:	python-pygtk-devel >= 2.0
Requires:	beryl-core >= 1:%{version}
Requires:	beryl-settings-bindings >= 1:%{version}
Requires:	librsvg >= 2.16
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
%patch0 -p1
echo '#beryl version header' > VERSION
echo VERSION=%{version} >> VERSION
mv -f po/{hu_HU,hu}.po
cat > po/LINGUAS <<EOF
ca
es
es_AR
hu
nl
zh_CN
zh_HK
zh_TW
EOF

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
