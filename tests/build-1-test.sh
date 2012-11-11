#!/usr/bin/env roundup
#
# This file contains the test plan for the build command.
# Execute the plan by invoking: 
#    
#     rerun stubbs:test -m nexus -p build
#

# The Plan
# --------

describe "build"

it_fails_without_arguments() {
    rerun nexus:build || return 0
}

it_can_build_nexus() {
   processor=$(uname -p)
   tmpDir="$(mktemp -d)/nexus"
   cp -r ${RERUN_MODULES}/nexus/examples/build/nexus ${tmpDir}
   rerun  nexus: build --release 1 --version 2.0.6 --directory "${tmpDir}"
   rpm -qip "${tmpDir}/RPMS/${processor}/nexus-2.0.6-1.${processor}.rpm"
   rm -rf "${tmpDir}"
}
