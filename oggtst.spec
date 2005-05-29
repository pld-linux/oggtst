Summary:	Small utility to calculate Ogg-Vorbis playing time
Name:		oggtst
Version:	1.0
Release:	0.1
License:	GPL v2
Group:		Applications
Source0:	http://gnometoaster.rulez.org/archive/%{name}.tgz
# Source0-md5:	6bfc076664416251d7624ab3538d1cb9
URL:		http://gnometoaster.rulez.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libao-devel
BuildRequires:	libogg-devel
BuildRequires:	libvorbis-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Small utility to calculate Ogg-Vorbis playing time.

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