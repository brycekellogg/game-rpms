Name:           zork
Version:        legacy
Release:        1%{?dist}
Summary:        Zork
License:        Proprietary
Requires:       frotz-gui
BuildRequires:  ImageMagick
BuildArch:      noarch
Source0:        http://%{sourceserver}/games/sources/zork/zork1.dat
Source1:        http://%{sourceserver}/games/sources/zork/zork2.dat
Source2:        http://%{sourceserver}/games/sources/zork/zork3.dat
Source3:        http://www.infocom-if.org/games/zork1/zork1front_th.jpg
Source4:        http://www.infocom-if.org/games/zork2/zork2front_th.jpg
Source5:        http://www.infocom-if.org/games/zork3/zork3front_th.jpg


%description


%prep
magick %{SOURCE3} -resize 512x %{builddir}/%{name}1.png
magick %{SOURCE4} -resize 512x %{builddir}/%{name}2.png
magick %{SOURCE5} -resize 512x %{builddir}/%{name}3.png
cat <<- EOF > %{builddir}/%{name}1.desktop
	[Desktop Entry]
	Type=Application
	Name=%{summary} I
	Exec=sfrotz -F -l 10 -r 10 %{_datadir}/%{name}/zork1.dat
	Icon=%{name}1
EOF
cat <<- EOF > %{builddir}/%{name}2.desktop
	[Desktop Entry]
	Type=Application
	Name=%{summary} II
	Exec=sfrotz -F -l 10 -r 10 %{_datadir}/%{name}/zork2.dat
	Icon=%{name}2
EOF
cat <<- EOF > %{builddir}/%{name}3.desktop
	[Desktop Entry]
	Type=Application
	Name=%{summary} III
	Exec=sfrotz -F -l 10 -r 10 %{_datadir}/%{name}/zork3.dat
	Icon=%{name}3
EOF


%install
install -D -t %{buildroot}/%{_datadir}/%{name}/                     %{SOURCE0}
install -D -t %{buildroot}/%{_datadir}/%{name}/                     %{SOURCE1}
install -D -t %{buildroot}/%{_datadir}/%{name}/                     %{SOURCE2}
install -D -t %{buildroot}/%{_datadir}/icons/hicolor/512x512/apps/  %{builddir}/%{name}1.png
install -D -t %{buildroot}/%{_datadir}/icons/hicolor/512x512/apps/  %{builddir}/%{name}2.png
install -D -t %{buildroot}/%{_datadir}/icons/hicolor/512x512/apps/  %{builddir}/%{name}3.png
install -D -t %{buildroot}/%{_datadir}/applications/                %{builddir}/%{name}1.desktop
install -D -t %{buildroot}/%{_datadir}/applications/                %{builddir}/%{name}2.desktop
install -D -t %{buildroot}/%{_datadir}/applications/                %{builddir}/%{name}3.desktop


%files
%{_datadir}/%{name}
%{_datadir}/applications/%{name}1.desktop
%{_datadir}/applications/%{name}2.desktop
%{_datadir}/applications/%{name}3.desktop
%{_datadir}/icons/hicolor/512x512/apps/%{name}1.png
%{_datadir}/icons/hicolor/512x512/apps/%{name}2.png
%{_datadir}/icons/hicolor/512x512/apps/%{name}3.png


%changelog
* Tue Sep 22 2026 Bryce Kellogg <bryce@kellog.org>
- Initial packaging
