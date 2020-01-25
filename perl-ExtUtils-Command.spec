#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	ExtUtils
%define	pnam	Command
Summary:	Shell::Command - Cross-platform functions emulating common shell commands
Summary(pl.UTF-8):	Shell::Command - wieloplatformowe funkcje emulujące popularne polecenia powłoki
Name:		perl-ExtUtils-Command
Version:	1.17
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/ExtUtils/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	8d2bd6a2311b6264d3dd96c11601c34a
URL:		http://search.cpan.org/dist/ExtUtils-Command/
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.31
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The module is used to replace common UNIX commands. In all cases the
functions work from @ARGV rather than taking arguments. This makes
them easier to deal with in Makefiles.

%description -l pl.UTF-8
Ten moduł ma na celu zastąpienie popularnych poleceń uniksowych. We
wszystkich przypadkach funkcje działają z @ARGV zamiast przyjmowania
argumentów - dzięki temu są łatwiejsze do obsługi w plikach Makefile.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/ExtUtils/Command.pm
%{_mandir}/man3/ExtUtils::Command.3pm*
