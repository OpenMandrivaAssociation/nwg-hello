%undefine _debugsource_packages
Name:		nwg-hello 
Version:	0.3.1
Release:	1
Summary:	GTK3-based greeter for greetd written in python 
URL:		https://github.com/nwg-piotr/nwg-hello
License:	MIT
Group:		NWG
Source0:	https://github.com/nwg-piotr/nwg-hello/archive/v%{version}/%{name}-%{version}.tar.gz
BuildSystem:	python

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
Requires:  (hyprland or sway)
BuildSystem: python

%description
This program is a part of the nwg-shell project.
Nwg-hello is a GTK3-based greeter for the greetd daemon, written in python. 
It is meant to work under a Wayland compositor, like sway or Hyprland.
The greeter has been developed for the nwg-iso project, but it may be configured for standalone use.

%files
