#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-XML-Simple
Version  : 2.22
Release  : 10
URL      : http://search.cpan.org/CPAN/authors/id/G/GR/GRANTM/XML-Simple-2.22.tar.gz
Source0  : http://search.cpan.org/CPAN/authors/id/G/GR/GRANTM/XML-Simple-2.22.tar.gz
Summary  : 'An API for simple XML files'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-XML-Simple-doc

%description
This archive contains the distribution XML-Simple,
version 2.22:
An API for simple XML files

%package doc
Summary: doc components for the perl-XML-Simple package.
Group: Documentation

%description doc
doc components for the perl-XML-Simple package.


%prep
%setup -q -n XML-Simple-2.22

%build
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make V=1  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot}
else
./Build install --installdirs=site --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.22.0/XML/Simple.pm
/usr/lib/perl5/site_perl/5.22.0/XML/Simple/FAQ.pod

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man3/*
