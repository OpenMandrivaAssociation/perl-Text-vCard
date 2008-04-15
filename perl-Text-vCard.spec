%define realname   Text-vCard

Name:		perl-%{realname}
Version:    2.03
Release:    %mkrel 1
License:	GPL or Artistic
Group:		Development/Perl
Summary:    A package that provides APIs to work with single or multiple vCards (RFC 2426) 
Source0:    ftp://ftp.perl.org/pub/CPAN/modules/by-module/Text/Text-vCard-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{realname}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	perl-devel
BuildRequires:	perl(Text::vFile::asData)
BuildRequires:	perl(File::Slurp)
BuildArch: noarch

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
%{perl_vendorlib}/Text/*
%{_mandir}/man3/*
