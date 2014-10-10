%define upstream_name    Text-vCard
%define upstream_version 2.13

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	A package that provides APIs to work with single or multiple vCards (RFC 2426) 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org:21/pub/CPAN/modules/by-module/Text/Text-vCard-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Text::vFile::asData)
BuildRequires:	perl(File::Slurp)
BuildRequires:	perl(Digest::SHA)
BuildArch:	noarch

%description
A vCard is an electronic business card, containing information on a
person, a record, a set of address information, and more.

This package contains two related APIs:
 - Text::vCard, to create or edit a single vCard
 - Text::vCard::Addressbook, to work with multiple vCards

Text::vCard can also use data read through Text::vFile::asData to
generate a vCard with that content. It is recommended to use
Text::vCard::Addressbook, as it handles creating vCards from an existing
file for you.

%prep
%setup -q -n Text-vCard-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes
%{perl_vendorlib}/Text/*
%{_mandir}/man3/*

%changelog
* Thu Feb 03 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2.100.0-1mdv2011.0
+ Revision: 635555
- update to new version 2.10

* Mon Aug 23 2010 Jérôme Quelin <jquelin@mandriva.org> 2.90.0-1mdv2011.0
+ Revision: 572230
- update to 2.09

* Fri Jan 29 2010 Jérôme Quelin <jquelin@mandriva.org> 2.70.0-1mdv2011.0
+ Revision: 497916
- update to 2.07

* Mon Jan 25 2010 Jérôme Quelin <jquelin@mandriva.org> 2.60.0-1mdv2010.1
+ Revision: 495705
- update to 2.06

* Sat Jan 09 2010 Jérôme Quelin <jquelin@mandriva.org> 2.50.0-1mdv2010.1
+ Revision: 487935
- update to 2.05

* Mon Jan 04 2010 Jérôme Quelin <jquelin@mandriva.org> 2.40.0-1mdv2010.1
+ Revision: 486119
- update to 2.04

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 2.30.0-1mdv2010.0
+ Revision: 406191
- rebuild using %%perl_convert_version

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 2.03-2mdv2009.0
+ Revision: 268865
- rebuild early 2009.0 package (before pixel changes)

* Tue Apr 15 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.03-1mdv2009.0
+ Revision: 193949
- update to new version 2.03

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Sep 03 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.01-1mdv2008.0
+ Revision: 78722
- update to new version 2.01

* Wed Jun 27 2007 Michael Scherer <misc@mandriva.org> 2.00-2mdv2008.0
+ Revision: 45041
- yet another cosmetic fix from John Keller
- cosmetic fix proposed by John Keller

* Wed May 23 2007 Michael Scherer <misc@mandriva.org> 2.00-1mdv2008.0
+ Revision: 30203
- Import perl-Text-vCard



* Wed May 23 2007 Michael Scherer <misc@mandriva.org> 2.00-1mdv2008.0
- First Mandriva package

