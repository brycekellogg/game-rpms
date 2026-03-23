Name:           myst
Version:        2.0.5
Release:        1%{?dist}
Summary:        Myst: Masterpiece Edition via Scummvm
License:        Proprietary
Requires:       scummvm
BuildRequires:  tar xz
BuildArch:      noarch
Source0:        http://%{sourceserver}/games/sources/%{name}/%{name}-%{version}.tar.xz
Source1:        http://%{sourceserver}/games/sources/%{name}/%{name}.png


%description


%prep
tar -xJf %{SOURCE0} -C %{builddir}
cat <<- EOF > %{builddir}/%{name}.desktop
	[Desktop Entry]
	Type=Application
	Name=%{summary}
	Exec=scummvm -f -p %{_datadir}/%{name}/ mohawk:myst
	Icon=%{name}
EOF


%install
mkdir -p %{buildroot}/%{_datadir}/%{name}
cp -r %{builddir}/myst/* %{buildroot}/%{_datadir}/%{name}/
install -D -t %{buildroot}/%{_datadir}/applications/                %{builddir}/%{name}.desktop
install -D -t %{buildroot}/%{_datadir}/icons/hicolor/512x512/apps/  %{SOURCE1}


%files
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/512x512/apps/%{name}.png


%changelog
* Mon Mar 23 2026 Bryce Kellogg <bryce@kellog.org>
- Initial packaging
