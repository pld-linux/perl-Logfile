%include	/usr/lib/rpm/macros.perl
%define		pdir	Logfile
Summary:	Logfile - Perl extension for generating reports from logfiles
Summary(pl):	Logfile - rozszerzenie Perla do tworzenia raportów z logów
Name:		perl-Logfile
Version:	0.300
Release:	1
License:	unknown
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Logfile extension will help you to generate various reports from
different server logfiles.

%description -l pl
Rozszerzenie Logfile pomaga przy generowaniu rozmaitych raportów z
plików logów ró¿nych serwerów.

%prep
%setup -q -n %{pdir}-%{version}

%build
perl Makefile.PL
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
%{perl_sitelib}/Logfile
%{perl_sitelib}/Net/*.pm
%{_mandir}/man3/*
