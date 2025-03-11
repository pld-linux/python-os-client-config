#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_with	tests	# unit tests (deps missing)
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	OpenStack Client Configuration Library
Summary(pl.UTF-8):	Biblioteka konfiguracji klienta OpenStack
Name:		python-os-client-config
# keep 1.x here for python2 support
Version:	1.33.0
Release:	3
License:	Apache v2.0
Group:		Libraries/Python
Source0:	https://files.pythonhosted.org/packages/source/o/os-client-config/os-client-config-%{version}.tar.gz
# Source0-md5:	94cc492acd8ccdeb721d2ee4229d05cd
URL:		https://pypi.org/project/os-client-config/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-pbr >= 2.0.0
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-extras >= 1.0.0
BuildRequires:	python-fixtures >= 3.0.0
BuildRequires:	python-glanceclient >= 2.8.0
BuildRequires:	python-jsonschema >= 2.6.0
BuildRequires:	python-jsonschema < 3.0.0
BuildRequires:	python-mock >= 2.0.0
BuildRequires:	python-openstacksdk >= 0.13.0
BuildRequires:	python-oslotest >= 3.2.0
BuildRequires:	python-stestr >= 1.0.0
BuildRequires:	python-subunit >= 1.0.0
BuildRequires:	python-testscenarios >= 0.4
BuildRequires:	python-testtools >= 2.2.0
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-pbr >= 2.0.0
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-extras >= 1.0.0
BuildRequires:	python3-fixtures >= 3.0.0
BuildRequires:	python3-glanceclient >= 2.8.0
BuildRequires:	python3-jsonschema >= 2.6.0
BuildRequires:	python3-jsonschema < 3.0.0
BuildRequires:	python3-openstacksdk >= 0.13.0
BuildRequires:	python3-oslotest >= 3.2.0
BuildRequires:	python3-stestr >= 1.0.0
BuildRequires:	python3-subunit >= 1.0.0
BuildRequires:	python3-testscenarios >= 0.4
BuildRequires:	python3-testtools >= 2.2.0
%endif
%endif
%if %{with doc}
BuildRequires:	python-docutils >= 0.11
BuildRequires:	python-openstackdocstheme >= 1.18.1
BuildRequires:	python-openstacksdk >= 0.13.0
BuildRequires:	python-reno >= 2.5.0
BuildRequires:	sphinx-pdg-2 >= 1.7.0
%endif
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
os-client-config is a library for collecting client configuration for
using an OpenStack cloud in a consistent and comprehensive manner. It
will find cloud config for as few as 1 cloud and as many as you want
to put in a config file. It will read environment variables and config
files, and it also contains some vendor specific default values so
that you don't have to know extra info to use OpenStack.

%description -l pl.UTF-8
os-client-config to biblioteka do zbierania konfiguracji klienckiej do
używania chmury OpenStack w sposób spójny i wyczerpujący. Odnajdzie
konifgurację chmury - od jednej do tylu, ile umieści się w pliku
konfiguracyjnym. Odczyta zmienne środowiskowe i pliki konfiguracyjne;
zawiera też wartości domyślne, więc nie trzeba znać dodatkowych
informacji, aby używać OpenStack.

%package -n python3-os-client-config
Summary:	OpenStack Client Configuation Library
Summary(pl.UTF-8):	Biblioteka konfiguracji klienta OpenStack
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.6

%description -n python3-os-client-config
os-client-config is a library for collecting client configuration for
using an OpenStack cloud in a consistent and comprehensive manner. It
will find cloud config for as few as 1 cloud and as many as you want
to put in a config file. It will read environment variables and config
files, and it also contains some vendor specific default values so
that you don't have to know extra info to use OpenStack.

%description -n python3-os-client-config -l pl.UTF-8
os-client-config to biblioteka do zbierania konfiguracji klienckiej do
używania chmury OpenStack w sposób spójny i wyczerpujący. Odnajdzie
konifgurację chmury - od jednej do tylu, ile umieści się w pliku
konfiguracyjnym. Odczyta zmienne środowiskowe i pliki konfiguracyjne;
zawiera też wartości domyślne, więc nie trzeba znać dodatkowych
informacji, aby używać OpenStack.

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
sphinx-build-2 -b html doc/source doc/build/html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/os_client_config/tests
%endif

%if %{with python3}
%py3_install

%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/os_client_config/tests
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
%doc doc/build/html/{_static,contributor,install,reference,user,*.html,*.js}
%endif
