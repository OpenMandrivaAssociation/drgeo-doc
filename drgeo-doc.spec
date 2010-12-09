%define	version	1.5
%define release	%mkrel 6

Summary:	Drgeo documentation
Name:		drgeo-doc
Version:	%{version}
Release:	%{release}
License:	GFDL
Group:		Books/Other
URL:		http://www.ofset.org/drgeo/
Source:		http://prdownloads.sourceforge.net/ofset/%{name}-%{version}.tar.bz2
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch

%description
This package contains manual for DrGeo, an interactive geometry
software.

%prep
%setup -q

%build
%configure2_5x

%install
rm -rf %{buildroot}
%makeinstall_std

# drgeo searches for ..../C/drgenius.html, not c/drgenius.html
mv %{buildroot}%{_datadir}/drgeo/help/{c,C}

pwd=`pwd`
pushd %{buildroot}%{_datadir}/drgeo/help
for i in ??*; do echo "%%lang($i) %%{_datadir}/drgeo/help/$i" >> $pwd/%{name}.lang; done
popd

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING README
%dir %{_datadir}/drgeo/help
%{_datadir}/drgeo/help/C

