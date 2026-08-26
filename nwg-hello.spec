%undefine _debugsource_packages
Name:		nwg-hello 
Version:	0.4.5
Release:	1
Summary:	GTK3-based greeter for greetd written in python 
URL:		https://github.com/nwg-piotr/nwg-hello
License:	MIT
Source0:	https://github.com/nwg-piotr/nwg-hello/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: pkgconfig(python3)
BuildRequires: python-setuptools
BuildRequires: python-wheel
BuildRequires: python-installer
BuildRequires: python-build
Requires:  python
Requires:  greetd
Requires:  python-gobject3
Requires:  python-gi
Requires:  gtk+3.0
Requires:  typelib(GtkLayerShell)
Requires:  gnome-themes-extra
Recommends:   mugshot			%dnl #FIXME not yet packaged
Recommends:  (hyprland or niri or sway)

%description
This program is a part of the nwg-shell project.
Nwg-hello is a GTK3-based greeter for the greetd daemon, written in python. 
It is meant to work under a Wayland compositor, like sway or Hyprland.
The greeter has been developed for the nwg-iso project, but it may be configured for standalone use.

%prep
%autosetup -p1

%build
%py_build

%install
%py_install

install -Dm 644 %{name}-default.json %{buildroot}%{_sysconfdir}/%{name}/%{name}-default.json
install -Dm 644 %{name}-default.css %{buildroot}%{_sysconfdir}/%{name}/%{name}-default.css
install -Dm 644 hyprland.conf %{buildroot}%{_sysconfdir}/%{name}/hyprland.conf
install -Dm 644 sway-config %{buildroot}%{_sysconfdir}/%{name}/sway-config
install -Dm 644 README %{buildroot}%{_sysconfdir}/%{name}/README
install -Dm 644 img/* -t %{buildroot}%{_datadir}/%{name}/
install -Dm 644 nwg.jpg %{buildroot}%{_datadir}/%{name}/nwg.jpg
install -Dm 644 cache.json 	%{buildroot}%{_localstatedir}/cache/%{name}/cache.json

#install -Dm 644 %{SOURCE1} %{buildroot}%{_libdir}/tmpfiles.d/%{name}.conf

%files
%{_bindir}/nwg-hello
%{python_sitelib}/nwg_hello-%{version}-py*.*.egg-info
%{python_sitelib}/nwg_hello/

%{_sysconfdir}/%{name}/*
%{_datadir}/%{name}/*
#%{_libdir}/tmpfiles.d/%{name}.conf
%{_localstatedir}/cache/%{name}/cache.json
%dir %{_localstatedir}/cache/%{name}
%dir %{_sysconfdir}/%{name}
%dir %{_datadir}/%{name}
