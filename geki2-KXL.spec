Summary:	Geki2, a video-oriented game
Summary(pl.UTF-8):   Geki2 - gra wideo
Name:		geki2-KXL
Version:	2.0.3
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://kxl.hn.org/download/%{name}-%{version}.tar.gz
# Source0-md5:	9bb542ea15a4e6b5f51164c19cc0a674
Patch0:		%{name}-scorepath.patch
URL:		http://kxl.hn.org/games.php
BuildRequires:	KXL-devel >= 1.1.1
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
Requires:	KXL >= 1.1.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
2D length scroll shooting game.

%description -l pl.UTF-8
Pionowo przewijana strzelanka 2D, klon raptora.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(2755,root,games) %{_bindir}/geki2
%dir %{_datadir}/geki2
%{_datadir}/geki2/bmp
%{_datadir}/geki2/wav
%dir %{_datadir}/geki2/data
%{_datadir}/geki2/data/*.dat
%attr(664,root,games) %config(noreplace) %verify(not md5 mtime size) /var/games/geki2.score
