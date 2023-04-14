Name:		kcharselect
Summary:	Select special characters from any font
Version:	23.03.90
Release:	1
Group:		Graphical desktop/KDE
License:	LGPLv2
URL:		http://utils.kde.org/projects/kcharselect
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(KF5Bookmarks)
BuildRequires:	cmake(KF5Crash)

%description
KCharSelect is a tool to select special characters from all installed
fonts and copy them into the clipboard.

%files -f %{name}.lang
%{_bindir}/kcharselect
%{_datadir}/applications/org.kde.kcharselect.desktop
%{_datadir}/metainfo/org.kde.kcharselect.appdata.xml

#----------------------------------------------------------------------

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang %{name} --with-html
