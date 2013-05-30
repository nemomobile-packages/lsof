Summary: A utility which lists open files on a Linux/UNIX system
Name: lsof
Version: 4.86
Release: 1
License: zlib
Group: Development/Debuggers

# lsof contains licensed code that we cannot ship.  Therefore we use
# upstream2downstream.sh script to remove the code before shipping it.
#
# The script you can found in SCM or download from:
# http://pkgs.fedoraproject.org/gitweb/?p=lsof.git;a=blob_plain;f=upstream2downstream.sh
#
Source0: %{name}-%{version}.tar.bz2
Source1: upstream2downstream.sh
URL: ftp://lsof.itap.purdue.edu/pub/tools/unix/lsof

%description
Lsof stands for LiSt Open Files, and it does just that: it lists
information about files that are open by the processes running on a
UNIX system.

%prep
%setup -q -n %{name}-%{version}/%{name}

%build
LSOF_VSTR=2.6.16 LINUX_BASE=/proc ./Configure -n linux

make DEBUG="$RPM_OPT_FLAGS" %{?_smp_mflags}

%install
rm -rf ${RPM_BUILD_ROOT}
mkdir -p ${RPM_BUILD_ROOT}%{_sbindir}
install -p -m 0755 lsof ${RPM_BUILD_ROOT}%{_prefix}/sbin
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man8
install -p -m 0644 lsof.8 ${RPM_BUILD_ROOT}%{_mandir}/man8/

%docs_package

%files
%defattr(-,root,root,-)
%{_sbindir}/lsof

