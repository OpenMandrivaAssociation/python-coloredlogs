Name:		python-coloredlogs
Version:	15.0.1
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/c/coloredlogs/coloredlogs-%{version}.tar.gz
Summary:	Colored terminal output for
URL:		https://pypi.org/project/coloredlogs/
License:	MIT
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildArch:	noarch

%description
Colored terminal output for Python's logging module

%files
%{_bindir}/coloredlogs
%{py_sitedir}/coloredlogs
%{py_sitedir}/coloredlogs.pth
%{py_sitedir}/coloredlogs-*.*-info
