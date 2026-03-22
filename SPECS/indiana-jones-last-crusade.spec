Name:           indiana-jones-last-crusade
Version:        2.20145
Release:        1%{?dist}
Summary:        Indiana Jones and the Last Crusade
License:        Proprietary
Requires:       scummvm
BuildRequires:  rsync unzip
BuildArch:      noarch
Source0:        http://%{sourceserver}/games/sources/indiana-jones-last-crusade/indiana_jones_and_the_last_crusade_en_gog_2_20145.sh
Source1:        http://%{sourceserver}/games/sources/indiana-jones-last-crusade/indiana_jones_last_crucade_reference_card.zip
Source2:        http://%{sourceserver}/games/sources/indiana-jones-last-crusade/indiana_jones_last_crusade_grail_diary.zip


%description


%prep
chmod u+x %{SOURCE0}
%{SOURCE0} -- --i-agree-to-all-licenses --noreadme --nooptions --noprompt --destination %{builddir}
cp %{builddir}/support/icon.png %{builddir}/%{name}.png
unzip %{SOURCE1} -d %{builddir}
unzip %{SOURCE2} -d %{builddir}
cat <<- EOF > %{builddir}/%{name}.desktop
	[Desktop Entry]
	Type=Application
	Name=%{summary}
	Exec=scummvm -f -p %{_datadir}/%{name}/ scumm:indy3
	Icon=%{name}
EOF


%install
install -D -t %{buildroot}/%{_datadir}/%{name}                      %{builddir}/data/*.LFL
install -D -t %{buildroot}/%{_datadir}/applications/                %{builddir}/%{name}.desktop
install -D -t %{buildroot}/%{_datadir}/icons/hicolor/256x256/apps/  %{builddir}/%{name}.png
install -D -t %{buildroot}/%{_docdir}/%{name}                       %{builddir}/**/*.pdf


%files
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/256x256/apps/%{name}.png
%{_docdir}/%{name}


%changelog
* Thu Mar 19 2026 Bryce Kellogg <bryce@kellog.org>
- Initial packaging
