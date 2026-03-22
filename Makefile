SPECTOOL_MACROS = -d "_topdir ${CURDIR}" \
				  -d "sourceserver ${SOURCE_SERVER}"
RPMBUILD_MACROS = -D "_topdir ${CURDIR}"

all: indiana-jones-atlantis.rpm     \
	 diablo-hellfire.rpm            \
	 doom.rpm                       \
	 indiana-jones-last-crusade.rpm


%.rpm: SPECS/%.spec
	spectool ${SPECTOOL_MACROS}  -gR SPECS/$(basename $@).spec
	rpmbuild ${RPMBUILD_MACROS} --bb SPECS/$(basename $@).spec

