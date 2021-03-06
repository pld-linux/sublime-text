Summary:	Sublime Text is a sophisticated text editor for code, html and prose
Name:		sublime-text
Version:	2.0.2
Release:	0.3
License:	Copyright Sublime HQ Pty Ltd
Group:		Applications/Editors
Source0:	http://c758482.r82.cf2.rackcdn.com/Sublime%20Text%20%{version}.tar.bz2
# NoSource0-md5:	34a60dac42f4ebc41218398fcfa92fe2
NoSource:	0
Source1:	http://c758482.r82.cf2.rackcdn.com/Sublime%20Text%20%{version}%20x64.tar.bz2
# NoSource1-md5:	699cd26d7fe0bada29eb1b2cd7b50e4b
NoSource:	1
Source2:	sublime_text.desktop
URL:		http://www.sublimetext.com/
Requires:	desktop-file-utils
Requires:	gtk-update-icon-cache
Requires:	hicolor-icon-theme
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_prefix}/lib/%{name}
%define		_enable_debug_packages	0

%description
Sublime Text is a sophisticated text editor for code, html and prose.
You'll love the slick user interface and extraordinary features.

%prep
%ifarch %{ix86}
%setup -qcT -a0
%endif
%ifarch %{x8664}
%setup -qcT -a1
%endif

mv "Sublime Text 2"/Icon .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_appdir},%{_bindir}}
cp -a "Sublime Text 2"/* $RPM_BUILD_ROOT%{_appdir}
ln -s %{_appdir}/sublime_text $RPM_BUILD_ROOT%{_bindir}/sublime

%py_ocomp $RPM_BUILD_ROOT%{_appdir}
%py_comp $RPM_BUILD_ROOT%{_appdir}

install -d $RPM_BUILD_ROOT%{_desktopdir}
cp -p %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}
for dir in Icon/*; do
	size=${dir#Icon/}
	install -d $RPM_BUILD_ROOT%{_iconsdir}/hicolor/$size/apps
	cp -p $dir/sublime_text.png $RPM_BUILD_ROOT%{_iconsdir}/hicolor/$size/apps
	install -d $RPM_BUILD_ROOT%{_appdir}/Icon/$size
	ln -s %{_iconsdir}/hicolor/$size/apps/sublime_text.png $RPM_BUILD_ROOT%{_appdir}/Icon/$size
done

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database
%update_icon_cache hicolor

%postun
%update_desktop_database
%update_icon_cache hicolor

%files
%defattr(644,root,root,755)
%dir %{_appdir}
%attr(755,root,root) %{_bindir}/sublime
%attr(755,root,root) %{_appdir}/sublime_text
%{_appdir}/PackageSetup.py
%{_appdir}/PackageSetup.py[co]
%{_appdir}/sublime_plugin.py
%{_appdir}/sublime_plugin.py[co]
%{_appdir}/Pristine?Packages
%{_appdir}/Icon
%dir %{_appdir}/lib
%{_appdir}/lib/python26.zip
%{_desktopdir}/sublime_text.desktop
%{_iconsdir}/hicolor/*/apps/sublime_text.png
