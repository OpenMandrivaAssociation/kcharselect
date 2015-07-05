Name:		kcharselect
Summary:	Select special characters from any font
Version:	15.04.3
Release:	1
Group:		Graphical desktop/KDE
License:	LGPLv2
URL:		http://utils.kde.org/projects/kcharselect
Source:		ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)

%description
KCharSelect is a tool to select special characters from all installed
fonts and copy them into the clipboard.

%files
%{_kde_appsdir}/kcharselect
%{_kde_bindir}/kcharselect
%{_kde_applicationsdir}/KCharSelect.desktop
%{_kde_docdir}/HTML/*/kcharselect

#----------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
