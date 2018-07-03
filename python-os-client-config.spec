#
# Conditional build:
%bcond_with	doc	# build doc (deps missing)
%bcond_with	tests	# do perform "make test" (deps missing)
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	OpenStack Client Configuation Library
Name:		python-os-client-config
Version:	1.28.0
Release:	2
License:	Apache
Group:		Libraries/Python
Source0:	https://files.pythonhosted.org/packages/source/o/os-client-config/os-client-config-%{version}.tar.gz
# Source0-md5:	cf0bffcf349932c306fd1d81459b1a9e
URL:		https://pypi.python.org/pypi/os-client-config
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-pbr
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-pbr
BuildRequires:	python3-setuptools
%endif
Requires:	python-PyYAML >= 3.1.0
Requires:	python-appdirs >= 1.3.0
Requires:	python-keystoneauth1 >= 2.1.0
Requires:	python-requestsexceptions >= 1.1.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
os-client-config is a library for collecting client configuration for
using an OpenStack cloud in a consistent and comprehensive manner. It
will find cloud config for as few as 1 cloud and as many as you want
to put in a config file. It will read environment variables and config
files, and it also contains some vendor specific default values so
that you don't have to know extra info to use OpenStack

- If you have a config file, you will get the clouds listed in it
- If you have environment variables, you will get a cloud named
  envvars
- If you have neither, you will get a cloud named defaults with base
  defaults

%package -n python3-os-client-config
Summary:	OpenStack Client Configuation Library
Group:		Libraries/Python
Requires:	python3-PyYAML >= 3.1.0
Requires:	python3-appdirs >= 1.3.0
Requires:	python3-keystoneauth1 >= 2.1.0
Requires:	python3-requestsexceptions >= 1.1.1

%description -n python3-os-client-config
os-client-config is a library for collecting client configuration for
using an OpenStack cloud in a consistent and comprehensive manner. It
will find cloud config for as few as 1 cloud and as many as you want
to put in a config file. It will read environment variables and config
files, and it also contains some vendor specific default values so
that you don't have to know extra info to use OpenStack

- If you have a config file, you will get the clouds listed in it
- If you have environment variables, you will get a cloud named
  envvars
- If you have neither, you will get a cloud named defaults with base
  defaults

%package apidocs
Summary:	API documentation for Python os-client-config module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona os-client-config
Group:		Documentation

%description apidocs
API documentation for Pythona os-client-config module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona os-client-config.

%prep
%setup -q -n os-client-config-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%if %{with doc}
cd doc
%{__make} -j1 html
rm -rf _build/html/_sources
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README.rst
%{py_sitescriptdir}/os_client_config
%{py_sitescriptdir}/os_client_config-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-os-client-config
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README.rst
%{py3_sitescriptdir}/os_client_config
%{py3_sitescriptdir}/os_client_config-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc doc/_build/html/*
%endif
