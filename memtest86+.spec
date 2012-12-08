# Debug package is empty and rpmlint rejects build
%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Summary:	A stand alone memory test for i386 architecture systems
Name:		memtest86+
Version:	4.20
Release:	2
License:	GPL
Source0:	http://www.memtest.org/download/%{version}/%{name}-%{version}.tar.gz
URL:		http://www.memtest.org
Group:		System/Kernel and hardware
BuildRequires:	dev86
Requires:	initscripts, drakxtools-backend

ExclusiveArch:	%{ix86} x86_64
%rename	memtest86

%description
Memtest86 is thorough, stand alone memory test for i386 architecture
systems.  BIOS based memory tests are only a quick check and often
missfailures that are detected by Memtest86.    

%prep
%setup -q 

%build
%make

%install
install -m644 memtest.bin -D %{buildroot}/boot/memtest.bin

%post
if [ -x /usr/sbin/bootloader-config ]; then
    /usr/sbin/bootloader-config --action add-entry --label memtest --image /boot/memtest.bin
fi

%preun
if [ -x /usr/sbin/bootloader-config ]; then
    /usr/sbin/bootloader-config --action remove-entry --label memtest
fi

%files
%doc FAQ
/boot/memtest.bin




%changelog
* Thu Dec 22 2011 Andrey Bondrov <abondrov@mandriva.org> 4.20-1
+ Revision: 744467
- New version 4.20

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 4.10-3
+ Revision: 666415
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 4.10-2mdv2011.0
+ Revision: 606636
- rebuild

* Sun May 23 2010 Thomas Backlund <tmb@mandriva.org> 4.10-1mdv2010.1
+ Revision: 545736
- update to 4.10
- drop note about needing gcc3.3 as it's not true anymore since v4.00

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 4.00-2mdv2010.1
+ Revision: 523303
- rebuilt for 2010.1

* Wed Sep 23 2009 Erwan Velu <erwan@mandriva.org> 4.00-1mdv2010.0
+ Revision: 447644
- 4.00

* Mon Aug 10 2009 Thomas Backlund <tmb@mandriva.org> 2.11-1mdv2010.0
+ Revision: 414265
- fix patch0 to apply cleanly

  + Thierry Vignaud <tv@mandriva.org>
    - new release

  + Erwan Velu <erwan@mandriva.org>
    - 2.10 now requires gcc3.3

* Thu Aug 28 2008 Erwan Velu <erwan@mandriva.org> 2.01-4mdv2009.0
+ Revision: 277029
- Removing versioning on memtest. Solve #16593

* Mon Aug 11 2008 Erwan Velu <erwan@mandriva.org> 2.01-3mdv2009.0
+ Revision: 270891
- Workaround for some gcc troubles in -0s

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 2.01-2mdv2009.0
+ Revision: 223233
- rebuild

* Fri Feb 22 2008 Erwan Velu <erwan@mandriva.org> 2.01-1mdv2008.1
+ Revision: 173833
- 2.01
  X86_64 patch is now upstream

* Fri Feb 08 2008 Erwan Velu <erwan@mandriva.org> 2.00-3mdv2008.1
+ Revision: 164162
- Rebuild
- Rebuild
- Fixing 64bit build
- 2.00

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 1.70-3mdv2008.1
+ Revision: 153069
- rebuild
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot


* Mon Jan 15 2007 Erwan Velu <erwan@mandriva.org> 1.70-1mdv2007.0
+ Revision: 109081
- 1.70
- Import memtest86+

* Tue Jul 25 2006 Erwan Velu <erwan@mandriva.org> 1.65-3mdv2007.0
- rebuild as src.rpm has been lost :(

* Sun Jun 25 2006 Giuseppe Ghibò <ghibo@mandriva.com> 1.65-2mdv2007.0
- Rebuilt.

* Sun Oct 02 2005 Erwan Velu <erwan@seanodes.com> 1.65-1mdk
- 1.65

* Tue Jun 28 2005 Erwan Velu <erwan@seanodes.com> 1.60.1mdk
- 1.60

* Fri Jun 10 2005 Per Ã˜yvind Karlsen <pkarlsen@mandriva.com> 1.55.1-1mdk
- 1.55.1
- %%mkrel

* Thu Apr 07 2005 Giuseppe Ghibò <ghibo@mandrakesoft.com> 1.55-2mdk
- Rebuilt for getting in sync both binaries and .src.rpm.

* Tue Mar 29 2005 Erwan Velu <erwan@seanodes.com> 1.55-1mdk
- 1.55

* Mon Mar 21 2005 Giuseppe GhibÃ² <ghibo@mandrakesoft.com< 1.51-4mdk
- Rebuilt.

* Thu Mar 10 2005 Giuseppe GhibÃ² <ghibo@mandrakesoft.com> 1.51-3mdk
- Rebuilt.

* Wed Feb 23 2005 Erwan Velu <velu@seanodes.com> 1.51-2mdk
- Rebuild

* Wed Feb 16 2005 Erwan Velu <velu@seanodes.com> 1.51-1mdk
- 1.51

* Thu Jan 27 2005 Giuseppe GHibÃ² <ghibo@mandrakesoft.com> 1.50-1mdk
- Release: 1.50.

* Mon Nov 29 2004 Erwan Velu <velu@seanodes.com> 1.40-1mdk
- 1.40

* Fri Nov 12 2004 Erwan Velu <velu@seanodes.com> 1.30-1mdk
- 1.30

* Sat Oct 23 2004 Giuseppe GhibÃ² <ghibo@mandrakesoft.com> 1.27-1mdl
- Release: 1.27.

* Sun Sep 05 2004 Giuseppe GhibÃ² <ghibo@mandrakesoft.com> 1.26-1mdk
- Release: 1.26.

* Sat Jul 10 2004 Erwan Velu <erwan@mandrakesoft.com> 1.20-1mdk
- 1.20

* Fri Jul 09 2004 Pixel <pixel@mandrakesoft.com> 1.15-4mdk
- fix requires

* Wed Jul 07 2004 Pixel <pixel@mandrakesoft.com> 1.15-3mdk
- use bootloader-config instead of /usr/share/loader stuff

* Sat Jun 19 2004 Per Ã˜yvind Karlsen <peroyvind@linux-mandrake.com> 1.15-2mdk
- opps, fix filename for loader (pixel)

* Thu Jun 17 2004 Per Ã˜yvind Karlsen <peroyvind@linux-mandrake.com> 1.15-1mdk
- 1.15
- should build on amd64 too
- cosmetics

* Mon Mar 01 2004 Giuseppe GhibÃ² <ghibo@mandrakesoft.com> 1.11-2mdk
- Fixed URLs.

* Sat Feb 07 2004 Giuseppe GhibÃ² <ghibo@mandrakesoft.com> 1.11-1mdk
- initial release.
- Obsolete memtest86 (unmaintained)

