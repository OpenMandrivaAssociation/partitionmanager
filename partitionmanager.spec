%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	KDE Partition Manager
Name:		partitionmanager
Version:	21.04.2
Release:	1
License:	GPLv3
Group:		System/Kernel and hardware
Url:		http://sourceforge.net/projects/partitionman/
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
# incorrectly treats a non-empty error message
# as indication that the support tools cannot be found
#Patch1:		partitionmanager-2.2.0-fix_empty_error_message.patch
BuildRequires:	pkgconfig(blkid)
BuildRequires:	pkgconfig(libatasmart)
BuildRequires:	cmake(ECM)
BuildRequires:	pkgconfig(Qt5Core) >= 5.3.0
BuildRequires:	pkgconfig(Qt5Gui) >= 5.3.0
BuildRequires:	pkgconfig(Qt5Widgets) >= 5.3.0
BuildRequires:	cmake(KPMcore) >= 3.1.0
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
BuildRequires:	cmake(KF5DBusAddons)
# (tpg) this requires all the filesystem tools needed to manipulate filesystems
Requires:	kpmcore >= 4.2.0

%description
A KDE utility that allows you to manage disks,
partitions, and file systems.

%prep
%setup -q
%autopatch -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang %{name} --with-html

%files -f %{name}.lang
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/org.*.desktop
%{_datadir}/metainfo/org.*.xml
%{_datadir}/config.kcfg/partitionmanager.kcfg
%{_datadir}/kxmlgui5/partitionmanager/partitionmanagerui.rc
%{_iconsdir}/hicolor/scalable/apps/partitionmanager.svg
