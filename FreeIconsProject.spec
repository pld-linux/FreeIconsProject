Name:		FreeIconsProject
Summary:	Very nice 3D icons
Summary(pl):	Bardzo ³adne ikonki 3D
Version:	0.2
Release:	1
Group:		X11/Other
Group(pl):	X11/Ró¿ne
License:	GPL
URL:		http://gfx.contex.pl
Source0:	http://gfx.contex.pl/ikons/%{name}_%{version}.tar.bz2
BuildRoot: 	%{tmpdir}/%{name}_%{version}-build-root-%(id -u -n)
BuildArch:	noarch

%define 	_x11pixdir	%{_prefix}/X11R6/share/pixmaps

%description
Very nice 3D icons

%description -l pl
Bardzo ³adne ikonki 3D zrobione przez Polaka


%prep
%setup -n %{name}_%{version} -q

%build
gzip -9nf LICENCE AUTHORS TODO VERSION

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_x11pixdir}/{apps,devices,filesystem,symbols}
install -d $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
install apps/* $RPM_BUILD_ROOT%{_x11pixdir}/apps
install devices/* $RPM_BUILD_ROOT%{_x11pixdir}/devices
install filesystem/* $RPM_BUILD_ROOT%{_x11pixdir}/filesystem
install symbols/* $RPM_BUILD_ROOT%{_x11pixdir}/symbols

%files
%defattr(644,root,root,755)
%doc *.gz
%{_x11pixdir}/apps
%{_x11pixdir}/devices
%{_x11pixdir}/filesystem
%{_x11pixdir}/symbols

%clean
rm -rf $RPM_BUILD_ROOT
