Summary:	Geki2, a video-oriented game
Summary(pl):	Geki2 - gra wideo
Name:		geki2-KXL
Version:	2.0.2
Release:	2
License:	GPL
Group:		X11/Applications/Games
Source0:	http://www2.mwnet.or.jp/~fc3srx7/download/%{name}-%{version}.tar.gz
URL:		http://www2.mwnet.or.jp/~fc3srx7/
BuildRequires:	KXL-devel >= 1.1.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
2D length scroll shooting game.

%description -l pl
Strzelanka 2D, klon raptora.

%prep
%setup -q

%build
./configure --prefix=%{_prefix}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/geki2
%dir %{_datadir}/geki2
%{_datadir}/geki2/bmp
%{_datadir}/geki2/wav
%dir %{_datadir}/geki2/data
%{_datadir}/geki2/data/*.dat
#%attr(664,root,games) %config(noreplace) %verify(not size mtime md5) /var/games/geki2.score
#%{_prefix}/share/geki2/data/.score
