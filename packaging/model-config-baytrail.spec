%define debug_package %{nil}

Name:		model-config-baytrail
Summary:	A Model configuration
Version:	0.0.1
Release:	0
Group:		System/Configuration
License:	Apache-2.0
BuildArch:	noarch
Source0:	%{name}-%{version}.tar.gz
Source1:	model-config.manifest
BuildRequires:	/bin/sed

%description
Model configuration data package

%prep
%setup -q -n %{name}-%{version}
cp %{SOURCE1} .

%build
sed -e 's/@@PROFILE@@/%{profile}/g' \
	    model-config.xml.in > model-config.xml

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_sysconfdir}/config
cp -f model-config.xml %{buildroot}%{_sysconfdir}/config/model-config.xml

%files
%{_sysconfdir}/config/model-config.xml
%manifest model-config.manifest
