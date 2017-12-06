%global srcname pymediainfo

%if 0%{?rhel} && 0%{?rhel} <= 7
%bcond_with python3
%else
%bcond_without python3
%endif

Name:           python-%{srcname}
Version:        2.2.0
Release:        1%{?dist}
Summary:        Python wrapper around the MediaInfo library

License:        MIT
URL:            https://github.com/sbraz/%{srcname}
Source0:        %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  libmediainfo

%description
%{sum}.

%package     -n python2-%{srcname}
Summary:        Python2 wrapper around the MediaInfo library
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  python2-pytest
BuildRequires:  python2-pytest-runner
Requires:       libmediainfo
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname}
This small package is a Python2 wrapper around the MediaInfo library.

%if %{with python3}
%package     -n python3-%{srcname}
Summary:        Python3 wrapper around the MediaInfo library
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-runner
Requires:       libmediainfo
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
This small package is a Python3 wrapper around the MediaInfo library.
%endif # with python3


%prep
%autosetup -n %{srcname}-%{version}


%build
%py2_build

%if %{with python3}
%py3_build
%endif # with python3


%install
%if %{with python3}
%py3_install
%endif # with python3

%py2_install

%check
export LC_ALL=C.UTF-8
PYTEST_ADDOPTS='-k "not test_parse_url"' %{__python2} setup.py test

%if %{with python3}
PYTEST_ADDOPTS='-k "not test_parse_url"' %{__python3} setup.py test
%endif


%files -n python2-%{srcname}
%license LICENSE
%doc AUTHORS README.rst
%{python2_sitelib}/%{srcname}*

%if %{with python3}
%files -n python3-%{srcname}
%license LICENSE
%doc AUTHORS README.rst
%{python3_sitelib}/%{srcname}*
%endif # with python3


%changelog
* Thu Nov 16 2017 Vasiliy N. Glazov <vascom2@gmail.com> 2.2.0-1
- Initial package
