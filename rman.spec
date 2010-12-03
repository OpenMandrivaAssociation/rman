Name: rman
Version: 3.2
Release: %mkrel 7
Summary: PolyglotMan - manual page translator to HTML, ASCII, TkMan, DocBook
Group: Development/X11
URL: http://polyglotman.sourceforge.net/
Source: %{name}-%{version}.tar.gz
License: GPL
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: libx11-devel >= 1.0.0
BuildRequires: libxmu-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1

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


%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%_bindir/rman
%_mandir/*/*


