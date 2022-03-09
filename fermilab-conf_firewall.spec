Name:		fermilab-conf_firewall
Version:	1.0
Release:	1%{?dist}
Summary:	A firewall zone with Fermilab's public IP ranges

Group:		Fermilab
License:	GPL
URL:		https://github.com/fermilab-context-rpms/fermilab-conf_firewall
Source0:	FNAL.xml

BuildArch:	noarch

# Top level package should require software specific packages
Requires:	%{name}-firewalld == %{version}-%{release}

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


%files
%defattr(0644,root,root,0755)

%files firewalld
%defattr(0644,root,root,0755)
/usr/lib/firewalld/zones/FNAL.xml

%changelog
* Wed Mar 9 2022 Pat Riehecky <riehecky@fnal.gov> 1.0-1
- Initial build
