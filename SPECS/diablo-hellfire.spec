Name:           diablo-hellfire
Version:        1.5.5
Release:        1%{?dist}
Summary:        Diablo I + Hellfire using DevilutionX
License:        SUL-1.0/Proprietary
Requires:       SDL2

Source0:        https://github.com/diasurgical/DevilutionX/releases/download/%{version}/devilutionx-linux-%{_arch}.tar.xz
Source1:        https://github.com/diasurgical/DevilutionX/releases/download/%{version}/devilutionx-src.tar.xz
Source2:        "setup_diablo_1.09_hellfire_v4_(78466).exe"

%description
DevilutionX is a port of Diablo and Hellfire that strives to make it simple to
run the game while providing engine improvements, bugfixes, and some optional
quality of life features. This RPM packages DevilutionX with the game files
from Diablo I + Hellfire.


%prep
mkdir -p %{builddir}/devilutionx-%{version}/
mkdir -p %{builddir}/diablo-gog/
tar -xJf %{SOURCE0} -C %{builddir}/devilutionx-%{version}/
tar -xJf %{SOURCE1} -C %{builddir}/
cd %{builddir}/diablo-gog
innoextract -m -p 0 \
            -I DIABDAT.MPQ \
            -I hellfire/hellfire.mpq \
            -I hellfire/hfmonk.mpq \
            -I hellfire/hfmusic.mpq \
            -I hellfire/hfvoice.mpq \
            -e %{SOURCE2}
sed -i "s|Exec=devilutionx|Exec=devilutionx --data-dir %{_datadir}/diablo|g"  %{builddir}/devilutionx-src-%{version}/Packaging/nix/*.desktop
sed -i "s|Name=DevilutionX|Name=Diablo|g"                                     %{builddir}/devilutionx-src-%{version}/Packaging/nix/*.desktop


%install
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_libdir}
mkdir -p %{buildroot}/%{_datadir}/diablo/
mkdir -p %{buildroot}/%{_datadir}/applications/
mkdir -p %{buildroot}/%{_datadir}/icons/hicolor/512x512/apps/
cp %{builddir}/devilutionx-%{version}/devilutionx          %{buildroot}/%{_bindir}
cp %{builddir}/devilutionx-%{version}/discord_game_sdk.so  %{buildroot}/%{_libdir}
cp %{builddir}/devilutionx-%{version}/devilutionx.mpq      %{buildroot}/%{_datadir}/diablo/
cp %{builddir}/diablo-gog/DIABDAT.MPQ            %{buildroot}/%{_datadir}/diablo/
cp %{builddir}/diablo-gog/hellfire/hellfire.mpq  %{buildroot}/%{_datadir}/diablo/
cp %{builddir}/diablo-gog/hellfire/hfmonk.mpq    %{buildroot}/%{_datadir}/diablo/
cp %{builddir}/diablo-gog/hellfire/hfmusic.mpq   %{buildroot}/%{_datadir}/diablo/
cp %{builddir}/diablo-gog/hellfire/hfvoice.mpq   %{buildroot}/%{_datadir}/diablo/
cp %{builddir}/devilutionx-src-%{version}/Packaging/nix/devilutionx.desktop           %{buildroot}/%{_datadir}/applications/diablo.desktop
cp %{builddir}/devilutionx-src-%{version}/Packaging/nix/devilutionx-hellfire.desktop  %{buildroot}/%{_datadir}/applications/hellfire.desktop
cp %{builddir}/devilutionx-src-%{version}/Packaging/resources/icon.png      %{buildroot}/%{_datadir}/icons/hicolor/512x512/apps/devilutionx.png
cp %{builddir}/devilutionx-src-%{version}/Packaging/resources/hellfire.png  %{buildroot}/%{_datadir}/icons/hicolor/512x512/apps/devilutionx-hellfire.png
chrpath -d %{buildroot}/%{_bindir}/devilutionx


%files
%{_bindir}/devilutionx
%{_libdir}/discord_game_sdk.so
%{_datadir}/diablo/devilutionx.mpq
%{_datadir}/diablo/DIABDAT.MPQ
%{_datadir}/diablo/hellfire.mpq
%{_datadir}/diablo/hfmonk.mpq
%{_datadir}/diablo/hfmusic.mpq
%{_datadir}/diablo/hfvoice.mpq
%{_datadir}/applications/diablo.desktop
%{_datadir}/applications/hellfire.desktop
%{_datadir}/icons/hicolor/512x512/apps/devilutionx.png
%{_datadir}/icons/hicolor/512x512/apps/devilutionx-hellfire.png


%changelog
* Sat Feb 28 2026 Bryce Kellogg <bryce@kellog.org>
- Initial packaging
