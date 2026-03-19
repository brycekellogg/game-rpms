Name:           shivah
Version:        3.0b.81406
Release:        1%{?dist}
Summary:        The Shivah
License:        Proprietary
Requires:       scummvm
BuildRequires:  ImageMagick
BuildArch:      noarch
Source0:        the_shivah_3_0b_81406.sh
Source1:        https://cdn2.steamgriddb.com/thumb/081d6134616fb110aa8fccfacc9d86e3.jpg


%description


%prep
rsync -a %{sourceserver}/%{name}/$(basename %{SOURCE0}) %{SOURCE0}
%{SOURCE0} -- --i-agree-to-all-licenses --noreadme --nooptions --noprompt --destination %{builddir}
magick %{SOURCE1} -resize 512x %{builddir}/%{name}.png
cat <<- EOF > %{builddir}/%{name}.desktop
	[Desktop Entry]
	Type=Application
	Name=%{summary}
	Exec=scummvm -f -p %{_datadir}/%{name}/ ags:shivahkosher
	Icon=%{name}
EOF


%install
install -D -t %{buildroot}/%{_datadir}/%{name}                      %{builddir}/game/Shivah.ags
install -D -t %{buildroot}/%{_datadir}/%{name}                      %{builddir}/game/speech.vox
install -D -t %{buildroot}/%{_datadir}/%{name}                      %{builddir}/game/audio.vox
install -D -t %{buildroot}/%{_datadir}/applications/                %{builddir}/%{name}.desktop
install -D -t %{buildroot}/%{_datadir}/icons/hicolor/512x512/apps/  %{builddir}/%{name}.png


%files
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/512x512/apps/%{name}.png


%changelog
* Wed Mar 18 2026 Bryce Kellogg <bryce@kellog.org>
- Initial packaging
