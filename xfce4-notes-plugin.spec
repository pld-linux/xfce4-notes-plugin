Summary:	Notes plugin for the Xfce panel
Summary(pl.UTF-8):	Notatki dla panelu Xfce
Name:		xfce4-notes-plugin
Version:	1.7.7
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://archive.xfce.org/src/panel-plugins/xfce4-notes-plugin/1.7/%{name}-%{version}.tar.bz2
# Source0-md5:	42b924b23f2fec6a1099e9b7a87db4a3
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-notes-plugin
BuildRequires:	Thunar-devel >= 1.1.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	xfce4-dev-tools >= 4.7.0
BuildRequires:	xfce4-panel-devel >= 4.7.0
BuildRequires:	xfconf-devel >= 4.7.0
Requires(post,postun):	gtk+2
Requires(post,postun):	hicolor-icon-theme
Requires:	xfce4-panel >= 4.6.0
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
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -r $RPM_BUILD_ROOT%{_datadir}/locale/ur_PK

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
%{_sysconfdir}/xdg/autostart/xfce4-notes-autostart.desktop
%attr(755,root,root) %{_bindir}/xfce4-notes
%attr(755,root,root) %{_bindir}/xfce4-popup-notes
%attr(755,root,root) %{_bindir}/xfce4-notes-settings
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/xfce4-notes-plugin
%{_datadir}/xfce4/panel-plugins/xfce4-notes-plugin.desktop
%{_iconsdir}/hicolor/*/apps/*.*
%{_desktopdir}/xfce4-notes.desktop
