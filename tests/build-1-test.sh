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

it_runs_without_arguments() {
    rerun nexus:build
}
