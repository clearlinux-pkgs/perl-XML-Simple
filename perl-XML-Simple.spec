#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v21
# autospec commit: 94c6be0
#
Name     : perl-XML-Simple
Version  : 2.25
Release  : 47
URL      : https://cpan.metacpan.org/authors/id/G/GR/GRANTM/XML-Simple-2.25.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/G/GR/GRANTM/XML-Simple-2.25.tar.gz
Summary  : 'An API for simple XML files'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-XML-Simple-license = %{version}-%{release}
Requires: perl-XML-Simple-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
This archive contains the distribution XML-Simple,
version 2.25:
An API for simple XML files

%package dev
Summary: dev components for the perl-XML-Simple package.
Group: Development
Provides: perl-XML-Simple-devel = %{version}-%{release}
Requires: perl-XML-Simple = %{version}-%{release}

%description dev
dev components for the perl-XML-Simple package.


%package license
Summary: license components for the perl-XML-Simple package.
Group: Default

%description license
license components for the perl-XML-Simple package.


%package perl
Summary: perl components for the perl-XML-Simple package.
Group: Default
Requires: perl-XML-Simple = %{version}-%{release}

%description perl
perl components for the perl-XML-Simple package.


%prep
%setup -q -n XML-Simple-2.25
cd %{_builddir}/XML-Simple-2.25

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-XML-Simple
cp %{_builddir}/XML-Simple-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-XML-Simple/fb6772d29e4082e7a9cc780a9e05de9d97d63940 || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/XML::Simple.3
/usr/share/man/man3/XML::Simple::FAQ.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-XML-Simple/fb6772d29e4082e7a9cc780a9e05de9d97d63940

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
