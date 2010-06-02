# Generated from rake-0.7.3.gem by gem2rpm -*- rpm-spec -*-
%define ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define gemname <%= spec.name %>
%define geminstdir %{gemdir}/gems/%{gemname}-%{version}

%global rubyabi 1.9

Summary: Ruby based make-like utility
Name: rubygem-%{gemname}

Version: <%= spec.version %>
Release: 3%{?dist}
Group: Development/Languages
License: MIT
URL: http://rake.rubyforge.org
Source0: http://gems.rubyforge.org/gems/%{gemname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root-%(%{__id_u} -n)
Requires: ruby(rubygems)
Requires: ruby(abi) = %{rubyabi}
BuildRequires: ruby(rubygems)
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires(check): ruby(flexmock)
BuildArch: noarch
Provides: rubygem(%{gemname}) = %{version}

%description
Rake is a Make-like program implemented in Ruby. Tasks and dependencies are
specified in standard Ruby syntax.

# rake ships w/ ruby 1.9, do nothing

%prep

%build

%install

%clean

%check

%files
%defattr(-, root, root, -)

%changelog
* Wed May 25 2010 Mo Morsi <mmorsi@redhat.com> - 0.8.7-3
- bumped release for polisher

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jun 18 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.8.7-1
- 0.8.7
- Enable %%check

* Tue Mar 17 2009 Jeroen van Meeuwen <j.van.meeuwen@ogd.nl> - 0.8.4-1
- New upstream version

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Oct 27 2008 David Lutterkort <lutter@redhat.com> - 0.8.3-1
- Cleanup multiply listed files
- Set permissions in doc/, lib/ and test/ to 644

* Thu May 15 2008 Alan Pevec <apevec@redhat.com> 0.8.1-2
- fix shebang in scripts

* Thu May 15 2008 Alan Pevec <apevec@redhat.com> 0.8.1-1
- new upstream version

* Thu Aug 23 2007 David Lutterkort <dlutter@redhat.com> - 0.7.3-2
- Fix license tag
- Remove bogus shebangs in lib/ and test/

* Mon Jun 18 2007 David Lutterkort <dlutter@redhat.com> - 0.7.3-1
- Initial package
