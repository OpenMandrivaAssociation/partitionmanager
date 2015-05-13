Summary:	KDE Partition Manager
Name:		partitionmanager
Version: 	1.1.1
Release: 	1
License: 	GPLv2+
Group: 		System/Kernel and hardware
Url: 		http://sourceforge.net/projects/partitionman/
Source0:	http://download.kde.org/stable/partitionmanager/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires: 	kdelibs4-devel
BuildRequires:	parted-devel
BuildRequires:	libblkid-devel
BuildRequires:	libatasmart-devel
BuildRequires:	doxygen

%description 
Easily manage disks, partitions and file systems on your KDE Desktop:
Create, resize, move, copy, back up, restore or delete partitions.

%prep
%setup -q
%apply_patches

%build
%cmake_kde4
%make

%install
%{makeinstall_std} -C build

%find_lang %{name} --with-html

%files -f %{name}.lang
%_kde_bindir/*
%_kde_libdir/*.so
%_kde_libdir/kde4/*.so
%_kde_iconsdir/hicolor/*/*/*
%_kde_datadir/applications/kde4/*.desktop
%_datadir/appdata/%{name}.appdata.xml
%_kde_appsdir/%{name}
%_kde_services/*.desktop
%_kde_servicetypes/*.desktop


