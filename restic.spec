Summary: Restic binary
Name: restic
Version: 0.9.3
Release: 1%{?dist}
License: GPL
URL: %{url_prefix}/%{name} 
%ifarch %{arm}
%define nsarch arm
%endif
%ifarch aarch64
%define nsarch arm64
%endif
%ifarch x86_64
%define nsarch amd64
%endif
Source0: https://github.com/restic/restic/releases/download/v%{version}/restic_%{version}_linux_%{nsarch}.bz2
Source1: https://raw.githubusercontent.com/restic/restic/master/LICENSE

BuildRequires: bzip2

# Disable debuginfo creation
%define debug_package %{nil}


%description
Restic binary

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/bin
bunzip2 -c %{SOURCE0} > %{buildroot}/usr/bin/restic
chmod 0755 %{buildroot}/usr/bin/restic
mv %{SOURCE1} RESTIC-COPYING
echo %{restic_release} > RESTIC-RELEASE


%files
%defattr(-,root,root)
/usr/bin/restic
%doc RESTIC-COPYING
%doc RESTIC-RELEASE

%changelog
* Tue Nov 27 2018 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 0.9.3-1
- Update to upstream release 0.9.3

* Thu Jul 12 2018 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 0.9.1-1
- First release - restic 0.9.1
