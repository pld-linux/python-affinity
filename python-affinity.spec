#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		module	affinity
Summary:	Control processor affinity on linux
Name:		python-%{module}
Version:	0.1.0
Release:	1
License:	Python Software Foundation License
Group:		Libraries/Python
Source0:	https://pypi.python.org/packages/source/a/affinity/%{module}-%{version}.tar.gz
# Source0-md5:	cc610cdb05ca675b4089ce2f05796f57
URL:		http://cheeseshop.python.org/pypi/affinity
BuildRequires:	python-devel
BuildRequires:	python-distribute
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
'affinity' provides a simple api for setting the processor affinity
by wrapping the specific underlying function calls of each platform.

%prep
%setup -q -n %{module}-%{version}

%build
%py_build

%{?with_tests:%{__python} setup.py test}

%install
rm -rf $RPM_BUILD_ROOT
%py_install

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{py_sitedir}/affinity
%{py_sitedir}/affinity/*.py[co]
%attr(755,root,root) %{py_sitedir}/affinity/*.so
%{py_sitedir}/affinity-*.egg-info
