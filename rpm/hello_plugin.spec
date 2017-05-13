Name:           hello_plugin.sh
Version:        1.0
Release:        1%{?dist}
Summary:        Says hello maaaaaan
Group:          The Awesome Group
License:        gnu
URL:            https://github.com/grantypantyyy
Source0:        hello_plugin.sh-1.0.tar.gz
BuildRequires:  bash
Requires:       nagios, check_nrpe_plugin
%description
Prints "Hello!!!" in your terminal.
%prep
%setup -q
%build
%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/lib64/nagios/plugins
install -m 0755 %{name} %{buildroot}/usr/lib64/nagios/plugins/%{name}
%clean
rm -rf %{buildroot}
%files
/usr/lib64/nagios/plugins/hello_plugin.sh
%post
sudo chown nagios:nagios /usr/lib64/nagios/plugins/hello_plugin.sh
sudo chmod +x /usr/lib64/nagios/plugins/hello_plugin.sh
sudo sed -i "215i command[hello_plugin]=\/usr\/lib64\/nagios\/plugins\/hello_plugin.sh -w 66 -c 902" /etc/nagios/nrpe.cfg
%changelog
