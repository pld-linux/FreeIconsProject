# TODO: icon themes should go to %{_iconsdir}/theme/size/... instead of %{_pixmapsdir}/size/...
Summary:	Very nice 3D icons
Summary(pl.UTF-8):	Bardzo ładne ikonki 3D
Name:		FreeIconsProject
Version:	0.5
Release:	5
License:	GPL
Group:		X11/Amusements
#Source0:	http://www.kde-look.org/content/files/1822-FreeIcons_%{version}.tar.gz
Source0:	http://carrion.elysium.pl/download/FreeIcons_%{version}.tar.gz
# Source0-md5:	22eaaba11ff2a90e41c45eaffee867c9
URL:		http://carrion.elysium.pl/
Requires:	%{_pixmapsdir}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Very nice 3D icons.

%description -l pl.UTF-8
Bardzo ładne ikonki 3D zrobione przez Polaka.

%prep
%setup -n FreeIcons_%{version} -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_pixmapsdir}/48x48/{apps,devices,filesystems,mimetypes}

install 48x48/apps/* $RPM_BUILD_ROOT%{_pixmapsdir}/48x48/apps
install 48x48/devices/* $RPM_BUILD_ROOT%{_pixmapsdir}/48x48/devices
install 48x48/filesystems/* $RPM_BUILD_ROOT%{_pixmapsdir}/48x48/filesystems
install 48x48/mimetypes/* $RPM_BUILD_ROOT%{_pixmapsdir}/48x48/mimetypes

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#%doc AUTHORS TODO VERSION
%{_pixmapsdir}/48x48
