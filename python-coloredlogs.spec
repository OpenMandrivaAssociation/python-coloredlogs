%global	module	coloredlogs
%global mod %(m=%{module}; echo ${m:0:1})

%bcond_with		docs

Summary:	Colored terminal output for Python's logging module
Name:		python-%{module}
Version:	15.0.1
Release:	1
#Source0:	https://github.com/xolox/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Source0:	https://pypi.io/packages/source/%{mod}/%{module}/%{module}-%{version}.tar.gz
License:	MIT
URL:		https://%{module}.readthedocs.io
BuildRequires:	pkgconfig(python3)
#BuildRequires:	python3dist(capturer)
BuildRequires:	python3dist(humanfriendly)
BuildRequires:	python3dist(pip)
BuildRequires:	python3dist(setuptools)
#BuildRequires:	python3dist(verboselogs)
BuildRequires:	python3dist(wheel)
%{?with_docs:	BuildRequires:	python3dist(sphinx)}

BuildArch:	noarch

#%%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%description
The coloredlogs package enables colored terminal output for Python's logging
module. The ColoredFormatter class inherits from logging.Formatter and uses
ANSI escape sequences to render your logging messages in color. It uses only
standard colors so it should work on any UNIX terminal.

%files
%license LICENSE.txt
%doc CHANGELOG.rst README.rst
%{_bindir}/%{module}
%{py_puresitedir}/%{module}
%{py_puresitedir}/%{module}.pth
%{py_puresitedir}/%{module}-%{version}-py%{py_ver}.egg-info
%{?with_docs:%doc docs/build/html}

#--------------------------------------------------------------------

%prep
%autosetup -n %{module}-%{version}

%build
%py_build

%if %{with docs}
sphinx-build-%{python3_version} -nb html -d docs/build/doctrees docs docs/build/html
rm docs/build/html/.buildinfo
%endif

%install
%py_install

