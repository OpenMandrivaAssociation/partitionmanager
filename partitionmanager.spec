Summary:	KDE Partition Manager
Name:		partitionmanager
Version: 	1.0.60
Release: 	0.1236311.2
License: 	GPLv2+
Group: 		System/Kernel and hardware
Url: 		http://sourceforge.net/projects/partitionman/
Source0: 	http://downloads.sourceforge.net/partitionman/%{name}-%{version}.tar.xz
Patch0:		partitionmanager-1.0.60-parted3.patch

BuildRequires: 	kdelibs4-devel
BuildRequires:	parted-devel
BuildRequires:	libblkid-devel
BuildRequires:	libatasmart-devel
BuildRequires:	doxygen

%description 
Easily manage disks, partitions and file systems on your KDE Desktop:
Create, resize, move, copy, back up, restore or delete partitions.

%prep
%setup -qn %{name}
%patch0 -p0

%build
%cmake_kde4
%make

%install
%{makeinstall_std} -C build

%files
%_kde_bindir/*
%_kde_libdir/*.so
%_kde_libdir/kde4/*.so
%_kde_iconsdir/hicolor/*/*/*
%_kde_datadir/applications/kde4/*.desktop
%_kde_appsdir/%{name}
%_kde_services/*.desktop
%_kde_servicetypes/*.desktop

