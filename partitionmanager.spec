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



%changelog
* Mon May 21 2012 Matthew Dawkins <mattydaw@mandriva.org> 1.0.60-0.1236311.2
+ Revision: 799848
- rebuild for parted
- cleaned up spec

* Wed Jun 15 2011 Funda Wang <fwang@mandriva.org> 1.0.60-0.1236311.1
+ Revision: 685216
- new snapshot
- build with latest parted3
- rebuild for new parted

* Wed Sep 01 2010 Funda Wang <fwang@mandriva.org> 1.0.3-1mdv2011.0
+ Revision: 575100
- update to new version 1.0.3

* Sat Apr 24 2010 Funda Wang <fwang@mandriva.org> 1.0.2-1mdv2010.1
+ Revision: 538464
- update to new version 1.0.2

* Sat Feb 27 2010 Funda Wang <fwang@mandriva.org> 1.0.1-2mdv2010.1
+ Revision: 512203
- rebuild for new parted

* Mon Jan 11 2010 Funda Wang <fwang@mandriva.org> 1.0.1-1mdv2010.1
+ Revision: 489783
- fix file list
- new version 1.0.1

* Sun Dec 27 2009 Funda Wang <fwang@mandriva.org> 1.0.0-2mdv2010.1
+ Revision: 482622
- rebuild for new parted

* Tue Aug 18 2009 Funda Wang <fwang@mandriva.org> 1.0.0-1mdv2010.0
+ Revision: 417737
- 1.0.0 final

* Tue Aug 04 2009 Funda Wang <fwang@mandriva.org> 1.0.0-0.RC1.1mdv2010.0
+ Revision: 408642
- new version 1.0 rc1

* Mon Jul 27 2009 Emmanuel Andry <eandry@mandriva.org> 1.0.0-0.BETA3.3mdv2010.0
+ Revision: 400624
- rebuild for new parted

* Tue Jun 09 2009 Frederic Crozat <fcrozat@mandriva.com> 1.0.0-0.BETA3.2mdv2010.0
+ Revision: 384385
- Switch to libblkid-devel

* Fri Jun 05 2009 Funda Wang <fwang@mandriva.org> 1.0.0-0.BETA3.1mdv2010.0
+ Revision: 382962
- New version 1.0.0 beta 3

* Fri May 01 2009 Funda Wang <fwang@mandriva.org> 1.0.0-0.BETA2.1mdv2010.0
+ Revision: 369466
- New version beta 2

* Sun Jan 18 2009 Funda Wang <fwang@mandriva.org> 1.0.0-0.BETA1a.1mdv2009.1
+ Revision: 330834
- import partitionmanager


