%define	version	1.5
%define release	7

Summary:	Drgeo documentation
Name:		drgeo-doc
Version:	%{version}
Release:	%{release}
License:	GFDL
Group:		Books/Other
URL:		https://www.ofset.org/drgeo/
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



%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 1.5-6mdv2011.0
+ Revision: 617901
- the mass rebuild of 2010.0 packages

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 1.5-5mdv2010.0
+ Revision: 428342
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.5-4mdv2009.0
+ Revision: 244545
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 1.5-2mdv2008.1
+ Revision: 140722
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Aug 23 2007 Thierry Vignaud <tv@mandriva.org> 1.5-2mdv2008.0
+ Revision: 70205
- use %%mkrel


* Sun Dec 26 2004 Abel Cheung <deaddog@mandrake.org> 1.5-1mdk
- New version
- Generate file list dynamically

* Wed Nov 26 2003 Abel Cheung <deaddog@deaddog.org> 1.4-1mdk
- First Mandrake package

