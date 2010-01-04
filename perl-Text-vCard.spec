%define upstream_name    Text-vCard
%define upstream_version 2.04

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    A package that provides APIs to work with single or multiple vCards (RFC 2426) 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:    ftp://ftp.perl.org/pub/CPAN/modules/by-module/Text/Text-vCard-%{upstream_version}.tar.gz

BuildRequires:	perl(Text::vFile::asData)
BuildRequires:	perl(File::Slurp)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

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
