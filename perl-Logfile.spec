%include	/usr/lib/rpm/macros.perl
%define		pdir	Logfile
Summary:	Logfile - Perl extension for generating reports from logfiles
Summary(pl):	Logfile - rozszerzenie Perla do tworzenia raport�w z log�w
Name:		perl-Logfile
Version:	0.300
Release:	2
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Logfile extension will help you to generate various reports from
different server logfiles.

%description -l pl
Rozszerzenie Logfile pomaga przy generowaniu rozmaitych raport�w z
plik�w log�w r�nych serwer�w.

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