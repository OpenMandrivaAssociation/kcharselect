Name:		kcharselect
Summary:	Select special characters from any font
Version:	4.8.97
Release:	1
Group:		Graphical desktop/KDE
License:	LGPLv2
URL:		http://utils.kde.org/projects/kcharselect
Source:		ftp://ftp.kde.org/pub/kde/unstable/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs4-devel

%description
KCharSelect is a tool to select special characters from all installed
fonts and copy them into the clipboard.

%files
%{_kde_appsdir}/kconf_update
%{_kde_appsdir}/kcharselect
%{_kde_bindir}/kcharselect
%{_kde_applicationsdir}/KCharSelect.desktop
%{_kde_docdir}/HTML/*/kcharselect

#----------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

