Name:		FreeIconsProject
Summary:	Very nice 3D icons
Summary(pl):	Bardzo ³adne ikonki 3D
Version:	0.2
Release:	1
License:	GPL
Group:		X11/Amusements
URL:		http://gfx.contex.pl
Source0:	http://gfx.contex.pl/ikons/%{name}_%{version}.tar.bz2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Very nice 3D icons.

%description -l pl
Bardzo ³adne ikonki 3D zrobione przez Polaka.

%prep
%setup -n %{name}_%{version} -q

%build
%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_pixmapsdir}/{apps,devices,filesystem,symbols}

install apps/* $RPM_BUILD_ROOT%{_pixmapsdir}/apps
install devices/* $RPM_BUILD_ROOT%{_pixmapsdir}/devices
install filesystem/* $RPM_BUILD_ROOT%{_pixmapsdir}/filesystem
install symbols/* $RPM_BUILD_ROOT%{_pixmapsdir}/symbols

gzip -9nf AUTHORS TODO VERSION

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{_pixmapsdir}/*
