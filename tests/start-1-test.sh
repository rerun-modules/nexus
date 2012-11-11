#!/usr/bin/env roundup
#
# This file contains the test plan for the start command.
# Execute the plan by invoking: 
#    
#     rerun stubbs:test -m nexus -p start
#

# The Plan
# --------

describe "start"

it_runs_without_arguments() {
    rerun nexus:start
}
