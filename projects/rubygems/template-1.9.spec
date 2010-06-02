%define gem_dir %(ruby -rrbconfig -e 'puts File::expand_path(File::join(Config::CONFIG["sitedir"],"..","gems"))')
%define rb_ver %(ruby -rrbconfig -e 'puts Config::CONFIG["ruby_version"]')
%define gem_home %{gem_dir}/%{rb_ver}
%define ruby_sitelib %(ruby -rrbconfig -e 'puts Config::CONFIG["sitelibdir"]')

%define repoid <%= repoid %>

Summary: The Ruby standard for packaging ruby libraries
Name: <%= name %>
Version: <%= version %>
Release: 2%{?dist}
Group: Development/Libraries
# No GPL version is specified.
License: Ruby or GPL+
URL: http://rubyforge.org/projects/rubygems/
Source0: http://rubyforge.org/frs/download.php/%{repoid}/rubygems-%{version}.tgz
Patch0: rubygems-1.3.5-noarch-gemdir.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-root-%(%{__id_u} -n)
Requires: ruby(abi) ruby-rdoc
BuildRequires:  ruby ruby-rdoc
BuildArch: noarch
Provides: ruby(rubygems) = %{version}

%description
RubyGems is the Ruby standard for publishing and managing third party
libraries.

# rubygems ships w/ ruby 1.9, do nothing

%prep

%build

%install

%clean

%files
%defattr(-, root, root, -)

%changelog
* Wed May 25 2010 Mo Morsi <mmorsi@redhat.com> - 1.3.5-2
- bumped release for polisher

* Mon Sep 21 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.3.5-1
- Update to 1.3.5

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Nov 09 2008 Jeroen van Meeuwen <kanarip@kanarip.com> - 1.3.1-1
- New upstream version

* Tue Sep 16 2008 David Lutterkort <dlutter@redhat.com> - 1.2.0-2
- Bump release because I forgot to check in newer patch

* Tue Sep 16 2008 David Lutterkort <dlutter@redhat.com> - 1.2.0-1
- Updated for new setup.rb
- Simplified by removing conditionals that were needed for EL-4;
  there's just no way we can support that with newer rubygems

* Wed Sep  3 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.9.4-2
- fix license tag

* Fri Jul 27 2007 David Lutterkort <dlutter@redhat.com> - 0.9.4-1
- Conditionalize so it builds on RHEL4

* Tue Feb 27 2007 David Lutterkort <dlutter@redhat.com> - 0.9.2-1
- New version
- Add patch0 to fix multilib sensitivity of Gem::dir (bz 227400)

* Thu Jan 18 2007 David Lutterkort <dlutter@redhat.com> - 0.9.1-1
- New version; include LICENSE.txt and GPL.txt
- avoid '..' in gem_dir to work around a bug in gem installer
- add ruby-rdoc to requirements

* Tue Jan  2 2007 David Lutterkort <dlutter@redhat.com> - 0.9.0-2
- Fix gem_dir to be arch independent
- Mention dual licensing in License field

* Fri Dec 22 2006 David Lutterkort <dlutter@redhat.com> - 0.9.0-1
- Updated to 0.9.0
- Changed to agree with Fedora Extras guidelines

* Mon Jan  9 2006 David Lutterkort <dlutter@redhat.com> - 0.8.11-1
- Updated for 0.8.11

* Sun Oct 10 2004 Omar Kilani <omar@tinysofa.org> 0.8.1-1ts
- First version of the package
