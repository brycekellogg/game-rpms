SPECTOOL_MACROS = -d "_topdir ${CURDIR}"
RPMBUILD_MACROS = -D "_topdir ${CURDIR}" \
				  -D "sourceserver ${SOURCE_SERVER}"

all: indiana-jones-atlantis.rpm     \
	 diablo-hellfire.rpm            \
	 doom.rpm                       \
	 indiana-jones-last-crusade.rpm


%.rpm: SPECS/%.spec
	spectool ${SPECTOOL_MACROS}  -gR SPECS/$(basename $@).spec
	rpmbuild ${RPMBUILD_MACROS} --bb SPECS/$(basename $@).spec

