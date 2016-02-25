Summary:	KDE Partition Manager
Name:		partitionmanager
Version:	2.0.2
Release:	1
License:	GPLv3
Group:		System/Kernel and hardware
Url:		http://sourceforge.net/projects/partitionman/
Source0:	http://download.kde.org/stable/partitionmanager/%{version}/src/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(blkid)
BuildRequires:	pkgconfig(libatasmart)
BuildRequires:	cmake(ECM)
BuildRequires:	pkgconfig(Qt5Core) >= 5.3.0
BuildRequires:	pkgconfig(Qt5Gui) >= 5.3.0
BuildRequires:	pkgconfig(Qt5Widgets) >= 5.3.0
BuildRequires:	cmake(KPMcore)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5Crash)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5JobWidgets)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5Service)
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
%cmake_qt5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang %{name} --with-html

%files -f %{name}.lang
%doc README TODO CHANGES
%{_bindir}/%{name}
%{_libdir}/lib%{name}fatlabel.so
%{_libdir}/lib%{name}private.so
%{_libdir}/qt5/plugins/libpmdummybackendplugin.so
%{_libdir}/qt5/plugins/libpmlibpartedbackendplugin.so
%{_datadir}/appdata/org.kde.PartitionManager.appdata.xml
%{_datadir}/applications/org.kde.PartitionManager.desktop
%{_datadir}/config.kcfg/config.kcfg
%{_iconsdir}/hicolor/scalable/apps/partitionmanager.svg
%{_datadir}/kservices5/pmdummybackendplugin.desktop
%{_datadir}/kservices5/pmlibpartedbackendplugin.desktop
%{_datadir}/kservicetypes5/pmcorebackendplugin.desktop
%{_datadir}/%{name}/%{name}*.rc
