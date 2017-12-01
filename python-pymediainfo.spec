%if 0%{?fedora}
%bcond_without python3
%else
%bcond_with python3
%endif

Name:           python-pymediainfo
Version:        2.2.0
Release:        1%{?dist}
Summary:        Python wrapper around the MediaInfo library

License:        MIT
URL:            https://github.com/sbraz/pymediainfo
Source0:        %{url}/archive/v%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  python2-pytest
BuildRequires:  python2-pytest-runner
%if %{with python3}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-runner
%endif # with python3

%description
%{sum}.

%package     -n python2-pymediainfo
Summary:        Python2 wrapper around the MediaInfo library

%description -n python2-pymediainfo
This small package is a Python2 wrapper around the MediaInfo library.

%if %{with python3}
%package     -n python3-pymediainfo
Summary:        Python3 wrapper around the MediaInfo library

%description -n python3-pymediainfo
This small package is a Python3 wrapper around the MediaInfo library.
%endif # with python3


%prep
%autosetup -c
mv pymediainfo-%{version} python2

%if %{with python3}
cp -a python2 python3
%endif # with python3


%build
pushd python2
    %py2_build
popd

%if %{with python3}
pushd python3
    %py3_build
popd
%endif # with python3


%install
rm -rf $RPM_BUILD_ROOT
%if %{with python3}
pushd python3
    %py3_install
popd
%endif # with python3

pushd python2
    %py2_install
popd

%check
pushd python2
    PYTEST_ADDOPTS='-k "not test_parse_unicode_file"' %{__python2} setup.py test
popd

%if %{with python3}
pushd python3
    PYTEST_ADDOPTS='-k "not test_parse_unicode_file"' %{__python3} setup.py test
popd
%endif


%files -n python2-pymediainfo
%license python2/LICENSE
%doc python2/AUTHORS python2/README.rst
%{python2_sitelib}/*

%if %{with python3}
%files -n python3-pymediainfo
%license python3/LICENSE
%doc python3/AUTHORS python3/README.rst
%{python3_sitelib}/*
%endif # with python3


%changelog
* Thu Nov 16 2017 Vasiliy N. Glazov <vascom2@gmail.com> 2.2.0-1
- Initial package
