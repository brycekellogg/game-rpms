Name:           indiana-jones-atlantis
Version:        2.20145
Release:        1%{?dist}
Summary:        Indiana Jones and the Fate of Atlantis
License:        Proprietary
Requires:       scummvm
BuildRequires:  ImageMagick
BuildArch:      noarch
Source0:        indiana_jones_and_the_fate_of_atlantis_en_gog_2_20145.sh
Source1:        https://cdn2.steamgriddb.com/grid/cec1b4ad140aabc94957c40cb00934ec.png


%description


%prep
rsync -a %{sourceserver}/%{name}/$(basename %{SOURCE0}) %{SOURCE0}
%{SOURCE0} -- --i-agree-to-all-licenses --noreadme --nooptions --noprompt --destination %{builddir}
magick %{SOURCE1} -resize 512x %{builddir}/%{name}.png
cat <<- EOF > %{builddir}/%{name}.desktop
	[Desktop Entry]
	Type=Application
	Name=%{summary}
	Exec=scummvm -f -p %{_datadir}/%{name}/ scumm:atlantis
	Icon=%{name}
EOF


%install
install -D -t %{buildroot}/%{_datadir}/%{name}                      %{builddir}/data/MONSTER.SOU
install -D -t %{buildroot}/%{_datadir}/%{name}                      %{builddir}/data/ATLANTIS.000
install -D -t %{buildroot}/%{_datadir}/%{name}                      %{builddir}/data/ATLANTIS.001
install -D -t %{buildroot}/%{_datadir}/applications/                %{builddir}/%{name}.desktop
install -D -t %{buildroot}/%{_datadir}/icons/hicolor/512x512/apps/  %{builddir}/%{name}.png
install -D -t %{buildroot}/%{_docdir}/%{name}                       %{builddir}/docs/english/*


%files
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/512x512/apps/%{name}.png
%{_docdir}/%{name}


%changelog
* Wed Mar 18 2026 Bryce Kellogg <bryce@kellog.org>
- Initial packaging
