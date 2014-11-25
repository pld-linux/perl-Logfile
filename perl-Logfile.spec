%define		pdir	Logfile
%include	/usr/lib/rpm/macros.perl
Summary:	Logfile - Perl extension for generating reports from logfiles
Summary(pl.UTF-8):	Logfile - rozszerzenie Perla do tworzenia raportów z logów
Name:		perl-Logfile
Version:	0.302
Release:	2
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{version}.tar.gz
# Source0-md5:	a733c079c912b98c1f17a81d32b4ee29
URL:		http://search.cpan.org/dist/Logfile/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Logfile extension will help you to generate various reports from
different server logfiles.

%description -l pl.UTF-8
Rozszerzenie Logfile pomaga przy generowaniu rozmaitych raportów z
plików logów różnych serwerów.

%prep
%setup -q -n %{pdir}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{perl_vendorlib}/Logfile
%{perl_vendorlib}/Net/*.pm
%{_mandir}/man3/*
