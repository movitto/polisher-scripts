%define ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define gemname <%= spec.name %>
%define geminstdir %{gemdir}/gems/%{gemname}-%{version}

# Only run the tests on distros that have sqlite3
%define with_check 0

# FIXME name should be rubygem-%{gemname}
Name:           ruby-%{gemname}
Version:        <%= spec.version %>
Release:        3%{?dist}
Summary:        Implements the ActiveRecord pattern for ORM

Group:          Development/Languages

License:        MIT
URL:            http://rubyforge.org/projects/activerecord/
Source0:        http://rubygems.org/downloads/activerecord-%{version}.gem
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  ruby >= 1.8
%if %with_check
BuildRequires:  ruby(active_support) = 2.0.1
BuildRequires:  ruby(sqlite3)
%endif
Requires:       ruby(abi) = 1.8
Requires:       ruby(active_support) = 2.0.1
Provides:       ruby(active_record) = %{version}

%description
Implements the ActiveRecord pattern (Fowler, PoEAA) for ORM. It ties
database tables and classes together for business objects, like Customer or
Subscription, that can find, save, and destroy themselves without resorting
to manual SQL.


%prep

%build

%install
%{__rm} -rf %{buildroot}
mkdir -p %{buildroot}%{gemdir}
gem install --local --install-dir %{buildroot}%{gemdir} \
            --force --rdoc %{SOURCE0}

%check
%if %with_check
cd test
ruby -I "connections/native_sqlite3" base_test.rb
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%{geminstdir}
%doc %{gemdir}/doc/%{gemname}-%{version}
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec

%changelog
* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 10 2007 David Lutterkort <dlutter@redhat.com> - 2.0.1-1
- New version

* Thu Nov 29 2007 David Lutterkort <dlutter@redhat.com> - 1.15.6-1
- New version

* Fri Jan 19 2007 David Lutterkort <dlutter@redhat.com> - 1.15.1-1
- New version
- Remove patch fix_ar_tests_accounts.diff, fixed upstream (ticket 5268)

* Wed Nov 15 2006 David Lutterkort <dlutter@redhat.com> - 1.14.4-2
- Run test suite for Fedora; requires patch0 to run successfully

* Wed Nov  8 2006 David Lutterkort <dlutter@redhat.com> - 1.14.4-1
- New upstream version

* Tue Sep 26 2006 David Lutterkort <dlutter@redhat.com> - 1.14.2-2
- Fix permissions on README

* Fri Sep  8 2006 David Lutterkort <dlutter@redhat.com> - 1.14.2-1
- Initial specfile
