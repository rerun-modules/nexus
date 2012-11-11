Summary: Sonatype Nexus Maven Repository Server

# The package name, version and release are supplied by rpm:build using rpmbuild(8)'s "--define" option:
Name: %{name}
Version: %{version}
Release: %{release} 

# Assumes the appropriate community release has been downloaded to SOURCES from maven mirror
Source0: %{name}-%{version}.zip
 
License: LGPL
Group: Applications/System

BuildArch: x86_64

# Specify minimum Java version required:
Requires: java

# Disables debug packages and stripping of binaries:
%global _enable_debug_package 0
%global debug_package %{nil}
%global __os_install_post %{nil}
 
# stop the build failing just becauses there are a few sample binaries in the distribution:
%define _binaries_in_noarch_packages_terminate_build   0


%description
Sonatype Nexus Maven Repository Server
 
%prep

%setup
# Overlay the source package contents with the customized files and directories:
#cp -R $RPM_SOURCE_DIR/%{name}-%{version}/* $RPM_BUILD_DIR/%{name}-%{version}


%build
 
%install
# setup the target directory hierarchy:
rm -rf %{buildroot}
install -d -m 755 %{buildroot}/usr/share/nexus
install -d -m 755 %{buildroot}/usr/share/nexus/sonatype-work
install -d -m 755 %{buildroot}/usr/share/nexus/nexus-%{version}
install -d -m 755 %{buildroot}/usr/share/nexus/nexus-%{version}/bin/jsw
#mv * %{buildroot}/usr/share/nexus
mv bin/jsw/{conf,lib,license,linux-x86-64} %{buildroot}/usr/share/nexus/nexus-%{version}/bin/jsw
mv bin/nexus %{buildroot}/usr/share/nexus/nexus-%{version}/bin/nexus
mv {LICENSE.txt,NOTICE.txt,conf,lib,logs,nexus,tmp} %{buildroot}/usr/share/nexus/nexus-%{version}

#------------buildroot------------------------|
#(cd /tmp/nexus/BUILDROOT/nexus-2.0.6-1.noarch/usr/share/nexus/bin/jsw && ls -d {conf,lib,license,linux-x86-64})

mkdir -p %{buildroot}/etc/init.d
cat >%{buildroot}/etc/init.d/nexus <<"EOF"
#!/bin/bash

# chkconfig: 345 20 80
# description: Starts and stops the nexus server

export RUN_AS_USER=nexus

exec /usr/share/nexus/nexus-%{version}/bin/nexus $*
EOF

%clean

%files
# add the files to the RPM with appropriate permissions: 
%defattr(-,nexus,nexus)

/usr/share/nexus

%attr(755,root,root) /etc/init.d/nexus
 
%changelog

%pre
# make sure the nexus user and group exist:
if id nexus > /dev/null 2>&1
then
  :
else
  groupadd -f nexus
  useradd -rd /usr/share/nexus -gnexus nexus
  passwd -l nexus
fi


%post
# setup nexus as a system service:
chkconfig --add nexus
chkconfig --level 345 nexus on

%preun
service nexus stop
