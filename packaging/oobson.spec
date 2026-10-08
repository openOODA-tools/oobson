Name:           oobson
Version:        0.2.0
Release:        1%{?dist}
Summary:        Binary JSON encoder and decoder with bson-to-json streaming converters.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oobson
Source0:        oobson-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oobson is a sovereign, capability-bounded BSON SERIALIZER written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oobson
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oobson-uninstall

%files
/usr/bin/oobson
/usr/bin/oobson-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
