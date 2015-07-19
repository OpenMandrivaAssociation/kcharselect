Name:		kcharselect
Summary:	Select special characters from any font
Version:	15.04.3
Release:	2
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
%doc %{_docdir}/HTML/*/kcharselect
%{_bindir}/kcharselect
%{_datadir}/applications/org.kde.KCharSelect.desktop
%{_datadir}/kxmlgui5/kcharselect/kcharselectui.rc

#----------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
