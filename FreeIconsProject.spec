Name:		FreeIconsProject
Summary:	Very nice 3D icons
Summary(pl):	Bardzo ³adne ikonki 3D
Version:	0.5
Release:	1
License:	GPL
Group:		X11/Amusements
# can be get from http://www.kde-look.org/content/download.php?content=1822
Source0:	http://www.kde-look.org/content/files/1822-FreeIcons_%{version}.tar.gz
# Source0-md5:	22eaaba11ff2a90e41c45eaffee867c9
URL:		http://carrion.elysium.pl/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Very nice 3D icons.

%description -l pl
Bardzo ³adne ikonki 3D zrobione przez Polaka.

%prep
%setup -n FreeIcons_%{version} -q

%build
%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_pixmapsdir}/48x48/{apps,devices,filesystems,mimetypes}
#install -d $RPM_BUILD_ROOT%{_pixmapsdir}/{apps,devices,filesystem,symbols}

install 48x48/apps/* $RPM_BUILD_ROOT%{_pixmapsdir}/48x48/apps
install 48x48/devices/* $RPM_BUILD_ROOT%{_pixmapsdir}/48x48/devices
install 48x48/filesystems/* $RPM_BUILD_ROOT%{_pixmapsdir}/48x48/filesystems
install 48x48/mimetypes/* $RPM_BUILD_ROOT%{_pixmapsdir}/48x48/mimetypes

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#%doc AUTHORS TODO VERSION
%{_pixmapsdir}/*/*
