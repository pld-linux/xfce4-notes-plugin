Summary:	Notes plugin for the Xfce panel
Summary(pl):	Notatki dla Xfce
Name:		xfce4-notes-plugin
Version:	0.10.0
Release:	1
License:	GPL
Group:		X11/Applications	
Source0:	http://download.berlios.de/xfce-goodies/%{name}-%{version}.tar.gz
# Source0-md5:	3fe2a4ce0bf208138b8056dd1ca6ab74
URL:		http://xfce-goodies.berlios.de/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	xfce4-panel-devel >= 4.1.90
Requires:	xfce4-panel >= 4.1.90
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xfce4-notes is a plugin for the Xfce panel which provides a simple
system for managing sticky notes on your desktop.

%description -l pl
xfce4-notes jest wtyczk± dla panelu Xfce pozwalaj±c± na umieszczanie
notatek na pulpicie.

%prep
%setup -q

%build
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/libnotes.so
%{_datadir}/xfce4/notes/note.png
