
# Getting Started
```bash
sudo dnf install rpmdevtools chrpath
make ${GAME}.rpm
```

# Games

## Diablo I + Hellfire
- [GOG](https://www.gog.com/en/game/diablo)
- [SPEC](./SPECS/diablo-hellfire.spec)
```bash
make diablo-hellfire.rpm
sudo dnf install ./RPMS/**/diablo-hellfire-*.rpm
```

## Doom + Doom II
- [GOG](https://www.gog.com/en/game/doom_doom_ii)
- [SPEC](./SPECS/doom.spec)
```bash
make doom.rpm
sudo dnf install ./RPMS/**/doom-*.rpm
```

## Indiana Jones and the Fate of Atlantis
- [GOG](https://www.gog.com/en/game/indiana_jones_and_the_fate_of_atlantis)
- [SPEC](./SPECS/indiana-jones-atlantis.spec)
```bash
make indiana-jones-atlantis.rpm
sudo dnf install ./RPMS/**/indiana-jones-atlantis-*.rpm
```

## Indiana Jones and the Last Crusade
- [GOG](https://www.gog.com/en/game/indiana_jones_and_the_last_crusade)
- [SPEC](./SPECS/indiana-jones-last-crusade.spec)
```bash
make indiana-jones-last-crusade.rpm
sudo dnf install ./RPMS/**/indiana-jones-last-crusade-*.rpm
```

## The Shivah
- [GOG](https://www.gog.com/en/game/the_shivah)
- [SPEC](./SPECS/shivah.spec)
```bash
make shivah.rpm
sudo dnf install ./RPMS/**/shivah-*.rpm
```

## Myst
- [Steam](https://store.steampowered.com/app/63660/Myst_Masterpiece_Edition/)
- [SPEC](./SPECS/myst.spec)
```bash
make myst.rpm
sudo dnf install ./RPMS/**/myst-*.rpm
```

# Games to be packaged
- Sid Meier's Civilization III
- Sid Meier's Civilization IV
- Robin Hood: The Legend of Sherwood
- Stronghold
- Portal
- Starsector
- Transcendentance
- Final Fantasy VII

