# $Id$
# Authority: dag
# Upstream: Ben Escoto <bescoto$stanford,edu>
# Upstream: <rdiff-backup-users$nongnu,org>

%define python_version %(%{__python} -c 'import sys; print sys.version[:3]')
%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

%{?el6:%define _popen_patch 1}

%{?el5:%define _without_egg_info 1}
%{?el4:%define _without_egg_info 1}
%{?el3:%define _without_egg_info 1}
%{?el2:%define _without_egg_info 1}

Summary: Convenient and transparent local/remote incremental mirror/backup
Name: rdiff-backup
Version: 1.2.8
Release: 4%{?dist}
License: GPLv2+
Group: Applications/Archiving
URL: http://www.nongnu.org/rdiff-backup/

Source: http://savannah.nongnu.org/download/rdiff-backup/rdiff-backup-%{version}.tar.gz
Patch0: rdiff-backup-popen2.patch

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: python-devel >= 2.2
BuildRequires: librsync-devel >= 0.9.7
#BuildRequires: python-libacl, python-xattr

# we don't want to provide private python extension libs
%{?filter_setup:
%filter_provides_in %{python_sitearch}/rdiff_backup/.*\.so$
%filter_setup
}

%description
rdiff-backup is a script, written in Python, that backs up one directory
to another and is intended to be run periodically (nightly from cron for
instance). The target directory ends up a copy of the source directory,
but extra reverse diffs are stored in the target directory, so you can
still recover files lost some time ago.

The idea is to combine the best features of a mirror and an incremental
backup. rdiff-backup can also operate in a bandwidth efficient manner
over a pipe, like rsync. Thus you can use rdiff-backup and ssh to
securely back a hard drive up to a remote location, and only the
differences from the previous backup will be transmitted.

%prep
%setup
%{?_popen_patch:%patch0 -p1}

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install --root "%{buildroot}"

### Create .pyo files
%{__python} -Oc 'from compileall import *; compile_dir("%{buildroot}%{python_sitearch}/rdiff_backup")'

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGELOG COPYING examples.html FAQ.html README
%doc %{_mandir}/man1/rdiff-backup.1*
%doc %{_mandir}/man1/rdiff-backup-statistics.1*
%{_bindir}/rdiff-backup
%{_bindir}/rdiff-backup-statistics
%dir %{python_sitearch}/rdiff_backup/
%{python_sitearch}/rdiff_backup/*.py
%{python_sitearch}/rdiff_backup/*.pyc
%ghost %{python_sitearch}/rdiff_backup/*.pyo
%{python_sitearch}/rdiff_backup/*.so
%{!?_without_egg_info:%{python_sitearch}/*.egg-info}

%changelog
* Sat Oct 01 2011 Yury V. Zaytsev <yury@shurup.com> - 1.2.8-4
- Fixed the popen patch (Julian Yap).

* Wed Sep 21 2011 David Hrbáč <david@hrbac.cz> - 1.2.8-3
- popen patch for el6

* Tue Sep 13 2011 David Hrbáč <david@hrbac.cz> - 1.2.8-2
- added egg-info support for el6

* Wed Apr 29 2009 Christoph Maser <cmr@financial.com> - 1.2.8-1
- Updated to release 1.2.8.

* Thu Jan 01 2009 Dag Wieers <dag@wieers.com> - 1.2.4-1
- Updated to release 1.2.4.

* Tue Dec 30 2008 Dag Wieers <dag@wieers.com> - 1.2.3-1
- Updated to release 1.2.3.

* Sat Oct 25 2008 Dag Wieers <dag@wieers.com> - 1.2.2-1
- Updated to release 1.2.2.

* Thu Aug 28 2008 Dag Wieers <dag@wieers.com> - 1.2.1-1
- Updated to release 1.2.1.

* Fri Jun 20 2008 Dag Wieers <dag@wieers.com> - 1.1.16-1
- Updated to release 1.1.16.

* Tue Feb 12 2008 Dag Wieers <dag@wieers.com> - 1.1.15-1
- Updated to release 1.1.15 (development).

* Fri Aug 03 2007 Dag Wieers <dag@wieers.com> - 1.1.12-1
- Updated to release 1.1.12 (development).

* Mon Jun 11 2007 Dag Wieers <dag@wieers.com> - 1.1.10-1
- Updated to release 1.1.10 (development).

* Mon Dec 18 2006 Dag Wieers <dag@wieers.com> - 1.1.7-1
- Updated to release 1.1.7 (development).

* Tue Jun 06 2006 Dag Wieers <dag@wieers.com> - 1.1.5-1
- Updated to release 1.1.5 (development).

* Thu Jan 26 2006 Dag Wieers <dag@wieers.com> - 1.0.4-1
- Updated to release 1.0.4.

* Sat Nov 26 2005 Dag Wieers <dag@wieers.com> - 1.0.3-1
- Updated to release 1.0.3.

* Sun Sep 11 2005 Dag Wieers <dag@wieers.com> - 1.0.1-1
- Updated to release 1.0.1.

* Sun Sep 11 2005 Dag Wieers <dag@wieers.com> - 1.0.0-2
- Rebuild against librsync-0.9.7.

* Mon Aug 15 2005 Dag Wieers <dag@wieers.com> - 1.0.0-1
- Updated to release 1.0.0.

* Sat Apr 09 2005 Dag Wieers <dag@wieers.com> - 0.12.8-1
- Updated to release 0.12.8.

* Mon Aug 02 2004 Dag Wieers <dag@wieers.com> - 0.12.7-1
- Cosmetic changes.

* Sun Nov 4 2001 Ben Escoto <bescoto@stanford.edu>
- Initial RPM.
