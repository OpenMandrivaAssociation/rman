Name: rman
Version: 3.2
Release: 10
Summary: PolyglotMan - manual page translator to HTML, ASCII, TkMan, DocBook
Group: Development/X11
URL: http://polyglotman.sourceforge.net/
Source: %{name}-%{version}.tar.gz
License: GPL

BuildRequires: pkgconfig(x11) >= 1.0.0
BuildRequires: pkgconfig(xmu) >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1

%define debug_package %{nil}

%description
PolyglotMan takes man pages from most of the popular flavors of UNIX and
transforms them into any of a number of text source formats.

%prep
%setup -q

%build
%make

%install
rm -rf %buildroot
install -d %buildroot/%_bindir
install -d %buildroot/%_mandir/man1
make BINDIR=%buildroot/%_bindir MANDIR=%buildroot/%_mandir/man1 install


%files
%defattr(-,root,root)
%_bindir/rman
%_mandir/*/*




%changelog
* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 3.2-8mdv2011.0
+ Revision: 669426
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 3.2-7mdv2011.0
+ Revision: 607367
- rebuild

* Mon Mar 15 2010 Oden Eriksson <oeriksson@mandriva.com> 3.2-6mdv2010.1
+ Revision: 520209
- rebuilt for 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 3.2-5mdv2010.0
+ Revision: 426940
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 3.2-4mdv2009.0
+ Revision: 225321
- rebuild

* Wed Mar 05 2008 Oden Eriksson <oeriksson@mandriva.com> 3.2-3mdv2008.1
+ Revision: 179439
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Jun 08 2007 Adam Williamson <awilliamson@mandriva.org> 3.2-2mdv2008.0
+ Revision: 37169
- rebuild for new era


* Mon May 22 2006 Helio Chissini de Castro <helio@mandriva.com>
+ 2006-05-22 22:51:43 (27877)
- Fixed install and tarball naming

* Mon May 22 2006 Helio Chissini de Castro <helio@mandriva.com>
+ 2006-05-22 22:42:44 (27876)
- Added missing rman package

