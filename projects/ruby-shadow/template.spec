%{!?ruby_sitearch: %define ruby_sitearch %(ruby -rrbconfig -e "puts Config::CONFIG['sitearchdir']")}
# This fails in mock since ruby doesn't exist in the default build env.
#%{!?ruby_abi: %define ruby_abi %(ruby -rrbconfig -e "puts Config::CONFIG['ruby_version']")}

Name:           <%= name %>
Version:        <%= version %>
Release:        14%{?dist}
Summary:        Ruby bindings for shadow password access
Group:          System Environment/Libraries
License:        Public Domain
URL:            http://ttsky.net/
Source0:        http://ttsky.net/src/ruby-shadow-%{version}.tar.gz
Patch0:         ruby-shadow-1.4.1-extconf-fixes.patch
# FIXME these two patches should only be applied when building against Ruby 1.9
Patch1:         ruby-shadow-1.4.1-update-depend-to-ruby19.patch
Patch2:         ruby-shadow-1.4.1-update-shadowc-to-ruby19.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  ruby ruby-devel
BuildRequires:  ruby(abi)
Requires:       ruby(abi)
Provides:       ruby(shadow) = %{version}-%{release}

%description
Ruby bindings for shadow password access

%prep
%setup -q -n shadow-%{version}
%patch0
%patch1
%patch2
%{_bindir}/iconv -f EUCJP -t utf8 -o README.ja README.euc

%build
ruby extconf.rb --with-cflags="$RPM_OPT_FLAGS"
make

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc HISTORY README README.ja
%{ruby_sitearch}/shadow.so

%changelog
* Wed May 25 2010 Mo Morsi <mmorsi@redhat.com> - 1.4.1-14
- bumped release for polisher

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Feb 10 2008 Kostas Georgiou <k.georgiou@imperial.ac.uk> - 1.4.1-11
- Rebuild for GCC 4.3

* Wed Aug 29 2007 Kostas Georgiou <k.georgiou@imperial.ac.uk> - 1.4.1-10
- Increase version to fix wrong tag

* Wed Aug 29 2007 Kostas Georgiou <k.georgiou@imperial.ac.uk> - 1.4.1-9
- Clean up of the "sh: ruby: command not found" added by the automated rebuild
  in the spec file

* Wed Aug 29 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 1.4.1-8
- Rebuild for selinux ppc32 issue.

* Wed Jul 18 2007 David Lutterkort <dlutter@redhat.com> - 1.4.1-7
- Remove dependency on ruby{,io}.h from depend - makes builds on RHEL4 fail, 
  and doesn't provide anything for proper rpm builds

* Fri May 25 2007 Kostas Georgiou <k.georgiou@imperial.ac.uk> 1.4.1-6
Removed _smp_mflags from install since it was causing problems

* Fri May 18 2007 Kostas Georgiou <k.georgiou@imperial.ac.uk> 1.4.1-5
Removed the ruby abi macro since it doesn't work in mock

* Tue May 15 2007 Kostas Georgiou <k.georgiou@imperial.ac.uk> 1.4.1-4
Cleaner ruby abi macro

* Tue May 15 2007 Kostas Georgiou <k.georgiou@imperial.ac.uk> 1.4.1-3
Fixed struct defines (0 != NULL in C) 
Calculate ruby abi at runtime instead of a hard coded version

* Tue May 15 2007 Kostas Georgiou <k.georgiou@imperial.ac.uk> 1.4.1-2
Converted README.euc to utf8 README.ja
Patched extconf.rb to use provided CFLAGS

* Mon May 14 2007 Kostas Georgiou <k.georgiou@imperial.ac.uk> 1.4.1-1
Initial rpm release
