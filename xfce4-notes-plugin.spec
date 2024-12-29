Summary:	Notes plugin for the Xfce panel
Summary(pl.UTF-8):	Notatki dla panelu Xfce
Name:		xfce4-notes-plugin
Version:	1.11.1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	https://archive.xfce.org/src/panel-plugins/xfce4-notes-plugin/1.11/%{name}-%{version}.tar.bz2
# Source0-md5:	b20d784fae90192e0597e857a620c392
URL:		https://goodies.xfce.org/projects/panel-plugins/xfce4-notes-plugin
BuildRequires:	Thunar-devel >= 1.2.0
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake
BuildRequires:	glib2-devel >= 1:2.50.0
BuildRequires:	gtk+3-devel >= 3.22.0
BuildRequires:	gtksourceview4-devel >= 4.0.0
BuildRequires:	libtool
BuildRequires:	libunique-devel
BuildRequires:	libxfce4ui-devel >= 4.16.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.601
BuildRequires:	vala-xfce4-panel >= 4.16.0
BuildRequires:	vala-xfconf >= 4.16.0
BuildRequires:	xfce4-dev-tools >= 4.16.0
BuildRequires:	xfce4-panel-devel >= 4.16.0
BuildRequires:	xfconf-devel >= 4.16.0
Requires:	gtk-update-icon-cache
Requires:	hicolor-icon-theme
Requires:	xfce4-panel >= 4.16.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xfce4-notes is a plugin for the Xfce panel which provides a simple
system for managing sticky notes on your desktop.

%description -l pl.UTF-8
xfce4-notes jest wtyczką dla panelu Xfce pozwalającą na umieszczanie
notatek na pulpicie.

%prep
%setup -q

#%{__rm} lib/ext-gdk.* lib/popup.* lib/theme-gtkrc.* src/xfce4-popup-notes.*

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-maintainer-mode \
	--disable-silent-rules \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/xfce4/panel/plugins/*.la

%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{hy_AM,hye,ie,ur_PK}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS
%{_sysconfdir}/xdg/autostart/xfce4-notes-autostart.desktop
%attr(755,root,root) %{_bindir}/xfce4-notes
%attr(755,root,root) %{_bindir}/xfce4-popup-notes
%attr(755,root,root) %{_bindir}/xfce4-notes-settings
%attr(755,root,root) %{_libdir}/xfce4/panel/plugins/libnotes.so*
%dir %{_datadir}/xfce4/notes
%dir %{_datadir}/xfce4/notes/gtk-3.0
%{_datadir}/xfce4/notes/gtk-3.0/gtk.css
%{_datadir}/xfce4/panel/plugins/xfce4-notes-plugin.desktop
%{_iconsdir}/hicolor/*/apps/*.*
%{_desktopdir}/xfce4-notes.desktop
