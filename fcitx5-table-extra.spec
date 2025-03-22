Name:		fcitx5-table-extra
Version:	5.1.7
Release:	1
Source0:	https://github.com/fcitx/fcitx5-table-extra/archive/%{version}/%{name}-%{version}.tar.gz
Summary:	Chinese input tables for fcitx
URL:		https://github.com/fcitx/fcitx5-table-extra
License:	GPL-3.0+
Group:		Graphical desktop/KDE
BuildRequires:	cmake
BuildRequires:	cmake(LibIMETable)
BuildRequires:	cmake(ECM)
BuildRequires:	gettext
BuildRequires:	boost-devel
BuildSystem:	cmake
BuildArch:	noarch

%description
Chinese input tables for fcitx

%files
%{_datadir}/fcitx5/inputmethod
%{_datadir}/fcitx5/table
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/metainfo/org.fcitx.Fcitx5.Addon.TableExtra.metainfo.xml
