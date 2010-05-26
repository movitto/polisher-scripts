%global gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%global gemname gemcutter
%global geminstdir %{gemdir}/gems/%{gemname}-%{version}

Summary:        The gemcutter client gem
Name:           rubygem-%{gemname}
Version:        <%= spec.version %>
Release:        4%{?dist}
Group:          Development/Languages
License:        MIT
URL:            http://gemcutter.org
Source0:        http://gems.rubyforge.org/gems/%{gemname}-%{version}.gem
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:       ruby(abi)
Requires:       rubygems
Requires:       rubygem(json)
BuildRequires:  rubygems
BuildRequires:  dos2unix
# For test
#BuildRequires:  rubygem(shoulda)

BuildArch:      noarch
Provides:       rubygem(%{gemname}) = %{version}

%description
The gemcutter client gem that interacts with the site http://gemcutter.org

%prep
%setup -q -T -c
mkdir -p ./%{gemdir}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gemdir}
gem install --local --install-dir ./%{gemdir} \
            --force --rdoc %{SOURCE0}

# bug 570254
grep -rl json_pure . | xargs sed -i -e 's|json_pure|json|'

mkdir -p %{buildroot}/%{gemdir}
cp -a ./%{gemdir}/* %{buildroot}/%{gemdir}/.

dos2unix %{buildroot}/%{geminstdir}/MIT-LICENSE

%check
pushd ./%{geminstdir}
rake test || :
popd

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%doc %{gemdir}/doc/%{gemname}-%{version}
%dir %{geminstdir}/
%doc %{geminstdir}/MIT-LICENSE
%{geminstdir}/Rakefile
%{geminstdir}/lib
%{geminstdir}/test
%attr(0644,root,root) %{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec

%changelog
* Wed May 25 2010 Mo Morsi <mmorsi@redhat.com> - 0.3.0-4
- bumped release for polisher

* Thu Mar  4 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.3.0-3
- Require rubygem(json), replace json_pure with json
  (bug 570254)

* Sat Jan  9 2010 Jeroen van Meeuwen <j.van.meeuwen@ogd.nl> - 0.3.0-2
- Fix end-of-line encoding in MIT-LICENSE file
- First package

