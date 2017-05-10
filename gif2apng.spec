Summary:	Convert GIF animations into APNG format
Summary(pl.UTF-8):	Konwerter animacji GIF do formatu APNG
Name:		gif2apng
Version:	1.9
Release:	1
License:	Zlib (BSD-like)
Group:		Applications/Graphics
Source0:	http://downloads.sourceforge.net/gif2apng/%{name}-%{version}-src-only.zip
# Source0-md5:	52c0689e244425b6033cf8a39a8266b6
URL:		http://gif2apng.sourceforge.net/
BuildRequires:	advancecomp-7z-devel
BuildRequires:	libstdc++-devel
BuildRequires:	zlib-devel >= 1.2.8
BuildRequires:	zopfli-devel
Requires:	zlib >= 1.2.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program converts GIF animations into APNG format.

%description -l pl.UTF-8
Ten program przekształca animacje GIF do formatu APNG

%prep
%setup -q -c

%build
%{__cxx} %{rpmldflags} %{rpmcxxflags} %{rpmcppflags} -Wall -o gif2apng gif2apng.cpp \
	-I/usr/include/adv7z \
	-ladv7z -lzopfli -lz -lm

%install
rm -rf $RPM_BUILD_ROOT

install -D gif2apng $RPM_BUILD_ROOT%{_bindir}/gif2apng

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc readme.txt
%attr(755,root,root) %{_bindir}/gif2apng
