%{!?ruby_sitelib: %global ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")}
%{!?ruby_sitearch: %global ruby_sitearch %(ruby -rrbconfig -e "puts Config::CONFIG['sitearchdir']")}

Name:           <%= name %>
Version:        <%= version %>
Release:        2%{?dist}
Summary:        Ruby bindings for cairo

Group:          System Environment/Libraries

License:        GPLv2+
URL:            http://cairographics.org/rcairo
Source0:        http://cairographics.org/releases/rcairo-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
  
BuildRequires:  ruby ruby-devel cairo-devel
#Requires:       ruby(abi) = 1.8 %{_bindir}/env
Requires:       ruby(abi) %{_bindir}/env
# If this package is mainly a ruby library, it should provide
# whatever people have to require in their ruby scripts to use the library
# For example, if people use this lib with "require 'foo'", it should provide
# ruby(foo)
Provides:       ruby(cairo) = %{version}-%{release}

%description
Ruby bindings for cairo. Cairo is a 2D graphics library with support for 
multiple output devices. Currently supported output targets include the 
X Window System, win32, and image buffers.

%package devel
Summary:        Ruby-cairo development environment
Group:          Development/Languages
Requires:       %{name} = %{version}-%{release}
Requires:       cairo-devel ruby-devel
Provides:       ruby(cairo-devel) = %{version}-%{release}

%description devel
Header files and libraries for building a extension library for the
ruby-cairo


%prep
%setup -q -n rcairo-%{version}
ruby extconf.rb
%{__chmod} 644 samples/agg/aa_test.rb
%{__chmod} 644 samples/scalable.rb
%{__chmod} 644 samples/text2.rb
%{__chmod} 644 samples/png.rb
%{__chmod} 644 samples/text-on-path.rb
%{__chmod} 644 samples/blur.rb

rm -f samples/.cvsignore

%build
export CFLAGS="$RPM_OPT_FLAGS"
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="%{__install} -c -p"

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING GPL NEWS README samples
# For noarch packages: ruby_sitelib
%{ruby_sitelib}/cairo.rb
%{ruby_sitelib}/cairo/
#%{ruby_sitelib}/cairo/context/circle.rb
#%{ruby_sitelib}/cairo/context/path.rb
#%{ruby_sitelib}/cairo/context/quad.rb
#%{ruby_sitelib}/cairo/context/rectangle.rb
# For arch-specific packages: ruby_sitearch
%{ruby_sitearch}/cairo.so

%files devel
%defattr(-,root,root,-)
%{ruby_sitearch}/rb_cairo.h


%changelog
* Wed May 26 2010 Mo Morsi <mmorsi@redhat.com> 1.8.1-2
- remove static ruby abi version dep

* Wed Dec 16 2009 Allisson Azevedo <allisson@gmail.com> 1.8.1-1
- Update to 1.8.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jan 23 2009 Allisson Azevedo <allisson@gmail.com> 1.8.0-2
- Rebuild

* Sun Oct  5 2008 Allisson Azevedo <allisson@gmail.com> 1.8.0-1
- Update to 1.8.0

* Tue Sep  9 2008 Allisson Azevedo <allisson@gmail.com> 1.7.0-1
- Update to 1.7.0

* Sun May 18 2008 Allisson Azevedo <allisson@gmail.com> 1.6.1-1
- Update to 1.6.1

* Mon Feb 25 2008 Allisson Azevedo <allisson@gmail.com> 1.5.1-1
- Update to 1.5.1
- Update License for GPLv2+

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.5.0-2
- Autorebuild for GCC 4.3

* Mon Jun 11 2007 Allisson Azevedo <allisson@gmail.com> 1.5.0-1
- Update to 1.5.0

* Sun Mar 28 2007 Allisson Azevedo <allisson@gmail.com> 1.4.1-2
- Changed license for Ruby License/GPL
- Add ruby-devel for devel requires
- Changed main group for System Environment/Libraries
- Changed install for keep timestamps

* Sun Mar 26 2007 Allisson Azevedo <allisson@gmail.com> 1.4.1-1
- Initial RPM release
