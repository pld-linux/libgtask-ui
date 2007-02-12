Summary:	Implementation of the progress bar simplification system
Summary(pl.UTF-8):   Implementacja systemu upraszczania paska postępu
Name:		libgtask-ui
Version:	0.1
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/gtask/%{name}-%{version}.tar.gz
# Source0-md5:	fb3a6af97d9a6e1b98b5d2eacf5bbe14
URL:		http://gtask.sourceforge.net/
BuildRequires:	GConf2-devel >= 2.4.0
BuildRequires:	eel-devel >= 2.4.0
BuildRequires:	gnome-vfs2-devel >= 2.4.0
BuildRequires:	gtk+2-devel >= 2:2.3.0
BuildRequires:	libgnomeui-devel >= 2.4.0
BuildRequires:	libgtask-devel >= 0.1
BuildRequires:	libxml2-devel >= 2.5.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gTask is an implementation of the progress bar simplification system.
The intent of the project is to create an easy to use framework for
application developers to communication the progress to certain long
running events.

%description -l pl.UTF-8
gTask jest implementacją systemu upraszczania paska postępu.
Założeniem projektu jest stworzenie łatwej w użyciu biblioteki
służącej do komunikacji procesów z długo wykonywanymi zadaniami.

%package devel
Summary:	Header files for libgtask-ui library
Summary(pl.UTF-8):   Pliki nagłówkowe biblioteki libgtask-ui
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	GConf2-devel >= 2.4.0
Requires:	gtk+2-devel >= 2.3.0
Requires:	libgnomeui-devel >= 2.4.0
Requires:	libgtask-devel >= 0.1

%description devel
Header files for libgtask-ui library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libgtask-ui.

%package static
Summary:	Static libgtask-ui library
Summary(pl.UTF-8):   Statyczna biblioteka libgtask-ui
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libgtask-ui library.

%description static -l pl.UTF-8
Statyczna biblioteka libgtask-ui.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%{_datadir}/gtask-ui-0.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/gtask-ui-0.1
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
