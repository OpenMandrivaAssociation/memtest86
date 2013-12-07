# Debug package is empty and rpmlint rejects build
%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Summary:	A stand alone memory test for i386 architecture systems
Name:		memtest86+
Version:	4.20
Release:	7
License:	GPLv2
Group:		System/Kernel and hardware
Url:		http://www.memtest.org
Source0:	http://www.memtest.org/download/%{version}/%{name}-%{version}.tar.gz
Source1:	%{name}.rpmlintrc
BuildRequires:	dev86
Requires:	initscripts
Requires:	drakxtools-backend
Requires(post,preun):	drakxtools-backend

ExclusiveArch:	%{ix86} x86_64
%rename		memtest86

%description
Memtest86 is thorough, stand alone memory test for i386 architecture
systems. BIOS based memory tests are only a quick check and often
missfailures that are detected by Memtest86.

%prep
%setup -q 

%build
%make

%install
install -m644 memtest.bin -D %{buildroot}/boot/memtest.bin

%post
if [ -x /usr/sbin/bootloader-config ]; then
	if [ "x$DURING_INSTALL" = "x" ]; then
    /usr/sbin/bootloader-config --action add-entry --label memtest --image /boot/memtest.bin
    fi
fi

%preun
if [ -x /usr/sbin/bootloader-config ]; then
    /usr/sbin/bootloader-config --action remove-entry --label memtest
fi

%files
%doc FAQ
/boot/memtest.bin

