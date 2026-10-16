# Debug package is empty and rpmlint rejects build
%define _enable_debug_packages %{nil}
%define debug_package %{nil}

#define pre beta2

Summary:	A stand alone memory test for x86 and AArch64 systems
Name:		memtest86+
Version:	9.00
Release:	1
License:	GPLv2
Group:		System/Kernel and hardware
Url:		https://www.memtest.org
Source0:	https://github.com/memtest86plus/memtest86plus/archive/refs/tags/v%{version}%{?pre:-%{pre}}.tar.gz
Source1:	%{name}.rpmlintrc
Source2:	20_memtest86+
BuildRequires:	make
BuildRequires:	gcc binutils
ExclusiveArch:	%{ix86} %{x86_64} aarch64
%rename pcmemtest

%description
MemTest86+ is a thorough, stand alone memory test for x86 and AArch64
systems. BIOS based memory tests are only a quick check and often
miss failures that are detected by MemTest86+.

%prep
%autosetup -p1 -n memtest86plus-%{version}%{?pre:-%{pre}}

%build
%setup_compile_flags 
# 9.00 builds one image, mt86plus, from build/<arch>. It is a Linux
# boot image on x86 and a UEFI image on every arch (ld.bfd; lld does
# not accept the linker scripts).
%ifarch %{ix86}
cd build/i586
%endif
%ifarch %{x86_64}
cd build/x86_64
%endif
%ifarch aarch64
cd build/aarch64
%endif
%make_build CC=%{__cc} LD=/usr/bin/ld.bfd

%install
%ifarch %{ix86}
cd build/i586
%endif
%ifarch %{x86_64}
cd build/x86_64
%endif
%ifarch aarch64
cd build/aarch64
%endif
mkdir -p %{buildroot}/boot
# grub.d looks for memtest.bin; UEFI looks for memtest.efi. Same image.
install -m644 mt86plus %{buildroot}/boot/memtest.bin
install -m644 mt86plus %{buildroot}/boot/memtest.efi

install -p -m755 %{SOURCE2} -D %{buildroot}%{_sysconfdir}/grub.d/20_memtest86+

%files
/boot/memtest.efi
/boot/memtest.bin
%{_sysconfdir}/grub.d/20_memtest86+
