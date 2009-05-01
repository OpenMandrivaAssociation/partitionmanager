%define betaver BETA2

Summary:	KDE Partition Manager
Name:		partitionmanager
Version: 	1.0.0
Release: 	%mkrel -c %betaver 1
Source0: 	http://downloads.sourceforge.net/partitionman/%name-%version-%betaver.tar.bz2
License: 	GPLv2+
Group: 		System/Kernel and hardware
Url: 		http://sourceforge.net/projects/partitionman/
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: 	kdelibs4-devel
BuildRequires:	parted-devel
BuildRequires:	e2fsprogs-devel
BuildRequires:	doxygen

%description 
Easily manage disks, partitions and file systems on your KDE Desktop:
Create, resize, move, copy, back up, restore or delete partitions.

%files -f %name.lang
%defattr(-,root,root)
%_kde_bindir/*
%_kde_libdir/*.so
%_kde_libdir/kde4/*.so
%_kde_iconsdir/hicolor/*/*/*
%_kde_services/*.desktop
%_kde_datadir/applications/kde4/*.desktop
%_kde_appsdir/%name

#--------------------------------------------------------------------

%prep
%setup -q -n %name-%version-%betaver

%build
%cmake_kde4
%make

%install
rm -rf %{buildroot}
%{makeinstall_std} -C build

%find_lang %name --with-html

%clean
rm -rf %{buildroot}
