%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)
#define git 20240218
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")

Summary:	KDE Partition Manager
Name:		partitionmanager
Version:	25.12.1
Release:	%{?git:0.%{git}.}1
License:	GPLv3
Group:		System/Kernel and hardware
Url:		https://sourceforge.net/projects/partitionman/
%if 0%{?git:1}
Source0:	https://invent.kde.org/system/partitionmanager/-/archive/%{gitbranch}/partitionmanager-%{gitbranchd}.tar.bz2#/partitionmanager-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/partitionmanager-%{version}.tar.xz
%endif
# incorrectly treats a non-empty error message
# as indication that the support tools cannot be found
#Patch1:		partitionmanager-2.2.0-fix_empty_error_message.patch
BuildRequires:	pkgconfig(blkid)
BuildRequires:	pkgconfig(libatasmart)
BuildRequires:	cmake(ECM)
BuildRequires:	pkgconfig(Qt6Core) >= 5.3.0
BuildRequires:	pkgconfig(Qt6Gui) >= 5.3.0
BuildRequires:	pkgconfig(Qt6Widgets) >= 5.3.0
BuildRequires:	cmake(KPMcore) >= 24.01.0
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6IconThemes)
BuildRequires:	cmake(KF6JobWidgets)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6Service)
BuildRequires:	cmake(KF6WindowSystem)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(KF6WidgetsAddons)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:  pkgconfig(polkit-qt6-1)

# (tpg) this requires all the filesystem tools needed to manipulate filesystems
Requires:	kpmcore >= 6.0

%rename plasma6-partitionmanager

BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%description
A KDE utility that allows you to manage disks,
partitions, and file systems.

%files -f %{name}.lang
%doc README.md
%{_bindir}/partitionmanager
%{_datadir}/applications/org.*.desktop
%{_datadir}/metainfo/org.*.xml
%{_datadir}/config.kcfg/partitionmanager.kcfg
%{_iconsdir}/hicolor/scalable/apps/partitionmanager.svg
%{_datadir}/solid/actions/open_in_partitionmanager.desktop
