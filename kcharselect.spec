Name:		kcharselect
Summary:	Select special characters from any font
Version:	15.04.3
Release:	1
Group:		Graphical desktop/KDE
License:	LGPLv2
URL:		http://utils.kde.org/projects/kcharselect
Source0:	http://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(KF5XmlGui)

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
