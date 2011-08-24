Name:           prey
Version:        0.5.3
Release:        1%{?dist}.R
Summary:        Prey is a lightweight application for tracking your stolen laptop/phone

License:        GPLv3
URL:            http://preyproject.com/
Source0:        http://preyproject.com/releases/%{version}/%{name}-%{version}-linux.zip
  
Requires:       curl
Requires:       xawtv
Requires:       ImageMagick
Requires:       perl-Net-SSLeay
Requires:       perl-IO-Socket-SSL

BuildArch:      noarch

%description
The script runs at a specified interval in your machine, and checks
for a specified URL on the web. If the URL does not exist it means the
PC has been stolen, and thus goes through the information
gathering routine and sends all that info through to a previously defined
email address. You can also not define a URL and in that case the program
will send the data every time it runs, although it is *not* recommended.  

%prep
%setup -q -n %{name}
chmod +x ../%{name}

%build


%install
#rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}
%{__cp} -r %{_builddir}/%{name} $RPM_BUILD_ROOT%{_datadir}/


%files
%defattr(755,root,root)
%{_datadir}/%{name}
%doc LICENSE README


%changelog
* Wed Aug 24 2011 Vasiliy N. Glazov <vascom2@gmail.com> 0.5.3-1.R
- initial build
