Summary:	KDE Partition Manager
Name:		partitionmanager
Version:	1.2.1
Release:	1
License:	GPLv2+
Group:		System/Kernel and hardware
Url:		http://sourceforge.net/projects/partitionman/
Source0:	http://download.kde.org/stable/partitionmanager/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(blkid)
BuildRequires:	pkgconfig(libatasmart)
BuildRequires:	cmake >= 3.0
BuildRequires:	cmake(ECM)
BuildRequires:	pkgconfig(Qt5Core) >= 5.3.0
BuildRequires:	pkgconfig(Qt5Widgets) >= 5.3.0
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5Crash)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5JobWidgets)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5WindowSystem)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(KF5WidgetsAddons)
Requires:	e2fsprogs
Requires:	xfsprogs
Requires:	jfsutils
Requires:	reiserfsprogs
Requires:	ntfs-3g
Requires:	dosfstools

%description 
A KDE utility that allows you to manage disks,
partitions, and file systems.

%prep
%setup -q
%apply_patches

%build
%cmake_qt5
%make

%install
%{makeinstall_std} -C build

%find_lang %{name} --with-html

%files -f %{name}.lang



