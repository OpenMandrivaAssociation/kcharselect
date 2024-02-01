Name:		plasma6-kcharselect
Summary:	Select special characters from any font
Version:	24.01.95
Release:	1
Group:		Graphical desktop/KDE
License:	LGPLv2
URL:		http://utils.kde.org/projects/kcharselect
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/kcharselect-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6WidgetsAddons)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(KF6Bookmarks)
BuildRequires:	cmake(KF6Crash)

%description
KCharSelect is a tool to select special characters from all installed
fonts and copy them into the clipboard.

%files -f kcharselect.lang
%{_bindir}/kcharselect
%{_datadir}/applications/org.kde.kcharselect.desktop
%{_datadir}/metainfo/org.kde.kcharselect.appdata.xml

#----------------------------------------------------------------------

%prep
%autosetup -p1 -n kcharselect-%{?git:master}%{!?git:%{version}}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang kcharselect --with-html
