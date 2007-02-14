# $Id$
# Authority: dries
# Upstream: Tels <nospam-abuse$bloodgate,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Graph-Easy

Summary: Create graphs
Name: perl-Graph-Easy
Version: 0.52
Release: 1
License: GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Graph-Easy/

Source: http://search.cpan.org/CPAN/authors/id/T/TE/TELS/graph/Graph-Easy-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 5.8.1, perl-Heap, perl(Scalar::Util) >= 1.13

%description
This module let's you create graphs (nodes/vertices connected by edges/arcs,
not pie charts!) and then lay them out on a flat surface.

Once laid out, the graph can be converted into various output formats like
ASCII art, HTML or SVG. You can also output the graph in graphviz format
and let dot do the layout for you.

Graphs can be generated by Perl code, or parsed from a simple text format
that is human readable and maintainable.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES README TODO
%doc %{_mandir}/man3/Graph::Easy*
%doc %{_mandir}/man1/graph-easy*
%{_bindir}/graph-easy
%{perl_vendorlib}/Graph/Easy.pm
%{perl_vendorlib}/Graph/Easy/

%changelog
* Wed Feb 14 2007 Dries Verachtert <dries@ulyssis.org> - 0.52-1
- Fixed the license (thanks to Tels)
- Updated to release 0.52.

* Wed Jan 03 2007 Dries Verachtert <dries@ulyssis.org> - 0.50-1
- Updated to release 0.50.

* Tue Nov 14 2006 Dries Verachtert <dries@ulyssis.org> - 0.49-1
- Updated to release 0.49.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 0.48-1
- Updated to release 0.48.

* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 0.44-1
- Updated to release 0.44.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.43-1
- Updated to release 0.43.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.38-1.2
- Rebuild for Fedora Core 5.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 0.38-1
- Updated to release 0.38.

* Sun Dec 25 2005 Dries Verachtert <dries@ulyssis.org> - 0.36-1
- Updated to release 0.36.

* Fri Dec  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.34-1
- Initial package.
