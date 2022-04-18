Name:		fermilab-conf_firewall
Version:	1.0
Release:	2.1%{?dist}
Summary:	A firewall zone with Fermilab's public IP ranges

Group:		Fermilab
License:	GPL
URL:		https://github.com/fermilab-context-rpms/fermilab-conf_firewall
Source0:	FNAL.xml

BuildArch:	noarch

# Top level package should require software specific packages
Requires:	(%{name}-firewalld == %{version}-%{release} if firewalld)

%description
Deploy a firewall zone with Fermilab's public IP ranges.

%package firewalld
Summary:        A firewalld zone with FNAL public IPs
%if 0%{?rhel} >= 8 || 0%{?fedora} >= 27
Recommends:	firewalld
%endif

%description firewalld
Deploy a firewalld zone with Fermilab's public IP ranges.


%prep


%build


%install
%{__install} -D %{SOURCE0} %{buildroot}/usr/lib/firewalld/zones/FNAL.xml


%post firewalld -p /bin/bash
systemctl is-active firewalld >/dev/null 2>&1
if [[ $? -eq 0 ]]; then
  systemctl reload firewalld >/dev/null 2>&1 || :
fi

%files
%defattr(0644,root,root,0755)

%files firewalld
%defattr(0644,root,root,0755)
/usr/lib/firewalld/zones/FNAL.xml

%changelog
* Mon Apr 18 2022 Pat Riehecky <riehecky@fnal.gov> 1.0-2.1
- use systemd to reload the config rather than firewall-cmd

* Wed Apr 13 2022 Pat Riehecky <riehecky@fnal.gov> 1.0-2
- Boolean conditional on firewalld
- Reload firewalld if it is running to get the new zone

* Wed Mar 9 2022 Pat Riehecky <riehecky@fnal.gov> 1.0-1
- Initial build
