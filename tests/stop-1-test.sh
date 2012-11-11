#!/usr/bin/env roundup
#
# This file contains the test plan for the stop command.
# Execute the plan by invoking: 
#    
#     rerun stubbs:test -m nexus -p stop
#

# The Plan
# --------

describe "stop"

it_runs_without_arguments() {
    rerun nexus:stop
}
