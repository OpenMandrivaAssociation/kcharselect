#define git 20240217
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
Name:		kcharselect
Summary:	Select special characters from any font
Version:	25.08.1
Release:	%{?git:0.%{git}.}1
Group:		Graphical desktop/KDE
License:	LGPLv2
URL:		https://utils.kde.org/projects/kcharselect
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
%if 0%{?git:1}
Source0:	https://invent.kde.org/utilities/kcharselect/-/archive/%{gitbranch}/kcharselect-%{gitbranchd}.tar.bz2#/kcharselect-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/kcharselect-%{version}.tar.xz
%endif
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6WidgetsAddons)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(KF6Bookmarks)
BuildRequires:	cmake(KF6Crash)

%rename plasma6-kcharselect

BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%description
KCharSelect is a tool to select special characters from all installed
fonts and copy them into the clipboard.

%files -f %{name}.lang
%{_bindir}/kcharselect
%{_datadir}/applications/org.kde.kcharselect.desktop
%{_datadir}/metainfo/org.kde.kcharselect.appdata.xml
