
diablo-hellfire:
	spectool -d "_topdir ${CURDIR}" -d "_sourcedir ${CURDIR}/SOURCES/$@"  -gR SPECS/$@.spec
	rpmbuild -D "_topdir ${CURDIR}" -D "_sourcedir ${CURDIR}/SOURCES/$@" --bb SPECS/$@.spec

uzdoom:
	spectool -d "_topdir ${CURDIR}" -d "_sourcedir ${CURDIR}/SOURCES/$@"  -gR SPECS/$@.spec
	rpmbuild -D "_topdir ${CURDIR}" -D "_sourcedir ${CURDIR}/SOURCES/$@" --bb SPECS/$@.spec

indiana-jones-atlantis:
	spectool -d "_topdir ${CURDIR}" -d "_sourcedir ${CURDIR}/SOURCES/$@"  -gR SPECS/$@.spec
	rpmbuild -D "_topdir ${CURDIR}" -D "_sourcedir ${CURDIR}/SOURCES/$@" --bb SPECS/$@.spec

