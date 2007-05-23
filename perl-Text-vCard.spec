%define realname   Text-vCard

Name:		perl-%{realname}
Version:    2.00
Release:    %mkrel 1
License:	GPL or Artistic
Group:		Development/Perl
Summary:    A package to edit and create a single vCard (RFC 2426)
Source0:    ftp://ftp.perl.org/pub/CPAN/modules/by-module/Text/Text-vCard-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{realname}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	perl-devel
BuildRequires:	perl(Text::vFile::asData)

BuildArch: noarch

%description
A vCard is an electronic business card.

This package is for a single vCard (person / record / set of address 
information). It provides an API to editing and creating vCards, or 
supplied a specific piece of the Text::vFile::asData results it generates 
a vCard with that content.

You should really use Text::vCard::Addressbook as this handles creating vCards 
from an existing file for you.

%prep
%setup -q -n Text-vCard-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*
