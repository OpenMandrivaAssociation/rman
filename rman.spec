%define debug_package %{nil}

Summary:	PolyglotMan - manual page translator to HTML, ASCII, TkMan, DocBook
Name:		rman
Version:	3.2
Release:	22
Group:		Development/X11
License:	GPLv2
Url:		http://polyglotman.sourceforge.net/
Source0:	%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(x11) >= 1.0.0
BuildRequires:	pkgconfig(xmu) >= 1.0.0
BuildRequires:	pkgconfig(xorg-macros)

%description
PolyglotMan takes man pages from most of the popular flavors of UNIX and
transforms them into any of a number of text source formats.

%prep
%setup -q

%build
%make

%install
install -d %{buildroot}/%{_bindir}
install -d %{buildroot}/%{_mandir}/man1
make BINDIR=%{buildroot}/%{_bindir} MANDIR=%{buildroot}/%{_mandir}/man1 install

%files
%{_bindir}/rman
%{_mandir}/man1/rman.1*

