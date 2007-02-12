Summary:	Notes plugin for the Xfce panel
Summary(pl.UTF-8):	Notatki dla panelu Xfce
Name:		xfce4-notes-plugin
Version:	1.4.1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://goodies.xfce.org/releases/xfce4-notes-plugin/%{name}-%{version}.tar.bz2
# Source0-md5:	6f20d84bf3aadd6c974f226c04f33050
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-notes-plugin
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	xfce4-dev-tools >= 4.4.0
BuildRequires:	xfce4-panel-devel >= 4.4.0
Requires(post,postun):	gtk+2
Requires(post,postun):	hicolor-icon-theme
Requires:	xfce4-panel >= 4.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xfce4-notes is a plugin for the Xfce panel which provides a simple
system for managing sticky notes on your desktop.

%description -l pl.UTF-8
xfce4-notes jest wtyczką dla panelu Xfce pozwalającą na umieszczanie
notatek na pulpicie.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/xfce4-popup-notes
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/xfce4-notes-plugin
%{_datadir}/xfce4/panel-plugins/xfce4-notes-plugin.desktop
%{_iconsdir}/hicolor/*/apps/*.*
