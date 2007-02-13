Summary:	Small utility to calculate Ogg-Vorbis playing time
Summary(pl.UTF-8):	Niewielkie narzędzie obliczajace długość grania pliku Ogg
Name:		oggtst
Version:	1.0
Release:	0.1
License:	GPL v2
Group:		Applications
Source0:	http://gnometoaster.rulez.org/archive/%{name}.tgz
# Source0-md5:	8d35377ce3e72f4a01440d7f121d4f68
URL:		http://gnometoaster.rulez.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libao-devel
BuildRequires:	libogg-devel
BuildRequires:	libvorbis-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Small utility to calculate Ogg-Vorbis playing time.

%description -l pl.UTF-8
Niewielkie narzędzie obliczajace długość grania pliku Ogg.

%prep
%setup -q -n %{name}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/*
