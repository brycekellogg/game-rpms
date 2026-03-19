Name:           doom
Version:        5.0.0
Release:        1%{?dist}
Summary:        Doom + Doom II using UZDoom
License:        GPL-3.0-only/Proprietary
BuildRequires:  libvpx-devel iwyu cmake ninja-build ImageMagick
Source0:        https://github.com/UZDoom/UZDoom/archive/refs/tags/%{version}-pre.tar.gz#/uzdoom-%{version}-pre.tar.gz
Source1:        https://github.com/Owlet7/wadfusion/archive/refs/heads/master.zip#/wadfusion-master.zip
Source2:        https://doomwiki.org/w/images/8/85/Doom.jpg
Source3:        setup_doom_plus_doom_ii_2715-adcdb6e-5_64bit_81590.exe

%description


%prep
rsync -a %{sourceserver}/%{name}/$(basename %{SOURCE3}) %{SOURCE3}
tar -xzf %{SOURCE0} -C %{builddir}
unzip    %{SOURCE1} -d %{builddir}
mkdir -p %{builddir}/gog-installer/
mkdir -p %{builddir}/UZDoom-%{version}-pre/build/
innoextract -m -p 0 -d %{builddir}/gog-installer/ -e %{SOURCE3}
cp %{builddir}/gog-installer/*.wad  %{builddir}/wadfusion-master/source_wads/
magick %{SOURCE2} -resize 512x -crop 512x512+0+0 %{builddir}/doom.png
cat <<- EOF > %{builddir}/doom.desktop
	[Desktop Entry]
	Type=Application
	Name=Doom + Doom II
	Exec=uzdoom -iwad doom_fusion.ipk3
	Icon=doom
EOF


%conf
cd %{builddir}/UZDoom-%{version}-pre/build/
cmake                                              \
    -DCMAKE_BUILD_TYPE=Release                     \
    -DCMAKE_EXPORT_COMPILE_COMMANDS=ON             \
    -G Ninja                                       \
    ..


%build
ninja -C %{builddir}/UZDoom-%{version}-pre/build/
cd %{builddir}/wadfusion-master/ && yes | python wadfusion.py


%install
install -D -t %{buildroot}/%{_bindir}/                              %{builddir}/UZDoom-%{version}-pre/build/uzdoom
install -D -t %{buildroot}/%{_datadir}/doom/                        %{builddir}/UZDoom-%{version}-pre/build/*.pk3
install -D -t %{buildroot}/%{_datadir}/doom/fm_banks/               %{builddir}/UZDoom-%{version}-pre/build/fm_banks/*
install -D -t %{buildroot}/%{_datadir}/doom/soundfonts/             %{builddir}/UZDoom-%{version}-pre/build/soundfonts/*
install -D -t %{buildroot}/%{_datadir}/doom/                        %{builddir}/wadfusion-master/doom_fusion.ipk3
install -D -t %{buildroot}/%{_datadir}/icons/hicolor/512x512/apps/  %{builddir}/doom.png
install -D -t %{buildroot}/%{_datadir}/applications/                %{builddir}/doom.desktop


%files
%{_bindir}/uzdoom
%{_datadir}/doom/*.pk3
%{_datadir}/doom/*.ipk3
%{_datadir}/doom/fm_banks/*
%{_datadir}/doom/soundfonts/*
%{_datadir}/icons/hicolor/512x512/apps/doom.png
%{_datadir}/applications/doom.desktop


%changelog
* Sat Feb 28 2026 Bryce Kellogg <bryce@kellog.org>
- Initial packaging
