# The following variables set:
#
# The Major.Minor version
%global rubymmver       <%= rubyxver %>
# The Major.Minor.Teeny version
%global rubymmtver      <%= version %>
# The patchlevel
%global _patchlevel     <%= patchlevel %>

##
## Safety net for missing /etc/rpm/macros.ruby
##
%{!?ruby_sitelib: %global ruby_sitelib %{_prefix}/local/share/ruby/}
%{!?ruby_sitearch: %global ruby_sitearch %{_prefix}/local/%{_lib}/ruby/}
%{!?ruby_vendorlib: %global ruby_vendorlib %{_datadir}/ruby/}
%{!?ruby_vendorarch: %global ruby_vendorarch %{_libdir}/ruby/}

%{!?ruby_sitelib_191: %global ruby_sitelib_191 %{_prefix}/local/share/ruby/1.9.1/}
%{!?ruby_sitearch_191: %global ruby_sitearch_191 %{_prefix}/local/%{_lib}/ruby/1.9.1/}
%{!?ruby_vendorlib_191: %global ruby_vendorlib_191 %{_datadir}/ruby/1.9.1/}
%{!?ruby_vendorarch_191: %global ruby_vendorarch_191 %{_libdir}/ruby/1.9.1/}

# Work on some of the defined variables to get the things we
# want (need)
%global dotpatchlevel   %{?_patchlevel:.%{_patchlevel}}
%global patchlevel      %{?_patchlevel:-p%{_patchlevel}}
%global arcver          %{rubymmtver}%{?patchlevel}

%global rubyfullver     <%= version %>
%global rubyabiver      <%= version %>

%global _compatsuffix   %{?rubymmtver:-%{rubymmtver}}

%global _normalized_cpu %(echo `echo %{_target_cpu} | sed 's/^ppc/powerpc/'`)

Name:               ruby%{?_compatsuffix}

Version:            %{_patchlevel}

Release:            11%{?dist}
License:            Ruby or GPLv2
URL:                http://www.ruby-lang.org/
BuildRoot:          %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:      autoconf
BuildRequires:      bison
BuildRequires:      byacc
BuildRequires:      db4-devel
BuildRequires:      emacs
BuildRequires:      gdbm-devel
BuildRequires:      glibc-devel
BuildRequires:      libX11-devel
BuildRequires:      ncurses-devel
BuildRequires:      openssl-devel
%if 0%{?fedora} >= 12
BuildRequires:      compat-readline5-devel
%else
BuildRequires:      readline-devel
%endif
BuildRequires:      unzip
BuildRequires:      tcl-devel
BuildRequires:      tk-devel

Source0:            ftp://ftp.ruby-lang.org/pub/%{name}/%{rubymmver}/ruby-%{arcver}.tar.bz2

# These patches actually make sense
Patch0:             ruby-1.9.1-p243-openssl-1.0.patch
Patch1:             ruby-1.9.1-p243-always-use-i386.patch
# These two patches belong together, but are rendered from the git repo
# as two separate patches. Maybe we'll truly fix this once it is in CVS.
Patch2:             ruby-1.9.1-p243-mmt-searchpath.patch
Patch3:             ruby-1.9.1-p243-mmt-searchpath-2.patch

# EPEL patches
Patch100:           ruby-1.9.1-p376-epel-test.patch

Summary:            An interpreter of object-oriented scripting language
Group:              Development/Languages
Requires:           %{name}-libs = %{version}-%{release}
Requires(post):     %{_sbindir}/alternatives
Requires(postun):   %{_sbindir}/alternatives

%description
Ruby is the interpreted scripting language for quick and easy
object-oriented programming.  It has many features to process text
files and to do system management tasks (as in Perl).  It is simple,
straight-forward, and extensible.

##
## ruby-devel
##
%package devel
Summary:    A Ruby development environment
Group:      Development/Languages
Requires:   %{name}-libs = %{version}-%{release}
Provides:   ruby(devel) = %{rubymmver}
Provides:   ruby(devel) = %{rubymmtver}

%description devel
Header files and libraries for building a extension library for the
Ruby or an application embedded Ruby.

##
## ruby-irb
##
%package irb
Summary:    The Interactive Ruby
Group:      Development/Languages
Requires:   %{name} = %{version}-%{release}
Provides:   ruby(irb) = %{rubymmver}
Provides:   ruby(irb) = %{rubymmtver}

%description irb
The irb is acronym for Interactive Ruby.  It evaluates ruby expression
from the terminal.

##
## ruby-libs
##
%package libs
Summary:    Libraries necessary to run Ruby
Group:      Development/Libraries
# Always offer both the rubymmver and rubymmtver Ruby ABI
Provides:   ruby(abi) = %{rubymmver}
Provides:   ruby(abi) = %{rubymmtver}
Provides:   ruby(api) = %{rubymmver}
Provides:   ruby(api) = %{rubymmtver}

%description libs
This package includes the libruby, necessary to run Ruby.

##
## ruby-mode
##
%package mode
Summary:    Emacs Lisp ruby-mode for the scripting language Ruby
Group:      Applications/Editors
Requires:   emacs-common

%description mode
Emacs Lisp ruby-mode for the object-oriented scripting language Ruby.

##
## ruby-rdoc
##
%package rdoc
Summary:    A tool to generate documentation from Ruby source files
Group:      Development/Languages
Requires:   %{name} = %{version}-%{release}
Requires:   ruby(irb) = %{rubymmtver}
Provides:   ruby(rdoc) = %{rubymmver}
Provides:   ruby(rdoc) = %{rubymmtver}

%description rdoc
The rdoc is a tool to generate the documentation from Ruby source files.
It supports some output formats, like HTML, Ruby interactive reference (ri),
XML and Windows Help file (chm).

##
## ruby-ri
##
%package ri
Summary:    Ruby interactive reference
Group:      Documentation
Requires:   %{name} = %{version}-%{release}
Requires:   ruby(rdoc) = %{rubymmtver}
Provides:   ruby(ri) = %{rubymmver}
Provides:   ruby(ri) = %{rubymmtver}

%description ri
ri is a command line tool that displays descriptions of built-in
Ruby methods, classes and modules. For methods, it shows you the calling
sequence and a description. For classes and modules, it shows a synopsis
along with a list of the methods the class or module implements.

##
## ruby-static
##
%package static
Summary:    Static libraries for Ruby
Group:      Applications/System
Requires:   %{name} = %{version}-%{release}
Requires:   %{name}-devel = %{version}-%{release}
Provides:   %{name}-libs-static = %{version}-%{release}

%description static
Static libraries for Ruby

##
## ruby-tcltk
##
%package tcltk
Summary:    Tcl/Tk interface for scripting language Ruby
Group:      Development/Languages
Requires:   %{name}-libs = %{version}-%{release}

%description tcltk
Tcl/Tk interface for the object-oriented scripting language Ruby.

%prep
%setup -q -n ruby-%{arcver}

%patch0 -p1
%patch1 -p1
# Again these two patches belong together
%patch2 -p1
%patch3 -p1
%if 0%{?rhel} > 0
%patch100 -p1
%endif

%build
for i in config.sub config.guess; do
    test -f %{_datadir}/libtool/$i && cp %{_datadir}/libtool/$i .
done
autoconf

rb_cv_func_strtod=no
export rb_cv_func_strtod
CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"
export CFLAGS
%configure \
    --with-sitedir='%{ruby_sitelib}' \
    --with-sitearchdir='%{ruby_sitearch}' \
    --with-vendordir='%{ruby_vendorlib}' \
    --with-vendorarchdir='%{ruby_vendorarch}' \
    --program-suffix='%{?_compatsuffix}' \
    --with-rubyhdrdir='%{_includedir}/ruby%{?_compatsuffix}' \
    --enable-shared \
    --enable-pthread \
    --disable-rpath \
    --with-ruby-version=full

make COPY="cp -p"

%install
rm -rf %{buildroot}

# installing binaries ...
make DESTDIR=%{buildroot} install

mkdir -p %{buildroot}/%{ruby_sitelib_191} \
        %{buildroot}/%{ruby_sitearch_191} \
        %{buildroot}/%{ruby_vendorlib_191} \
        %{buildroot}/%{ruby_vendorarch_191}

# generate ri doc
rm -rf .ext/rdoc
LD_LIBRARY_PATH=%{buildroot}%{_libdir} RUBYLIB=%{buildroot}%{ruby_vendorarch} make DESTDIR=%{buildroot} install-doc

# Find files with a shebang that do not have executable permissions
for script in `find %{buildroot}/%{ruby_sitelib} -type f ! -perm /a+x -name "*.rb"`; do
    [ ! -z "`head -n 1 $script | grep \"^#!/\"`" ] && chmod -v 755 $script
done

# Fix shebang
for script in `find %{buildroot}/%{ruby_sitelib} -type f -name "*.rb"`; do
    sed -r -i -e 's|(.*)/bin/ruby|%{_bindir}/ruby%{?_compatsuffix}|g' $script
done

if [ ! -d %{buildroot}/%{_includedir}/ruby%{?_compatsuffix}/ ]; then
    mv %{buildroot}/%{_includedir}/ruby%{?_compatsuffix}-*/ %{buildroot}/%{_includedir}/ruby%{?_compatsuffix}/
fi

%clean
rm -rf %{buildroot}

%post
%{_sbindir}/alternatives --install %{_bindir}/ruby ruby %{_bindir}/ruby%{?_compatsuffix} 90 \
    --slave %{_bindir}/erb ruby-erb %{_bindir}/erb%{?_compatsuffix} \
    --slave %{_bindir}/gem ruby-gem %{_bindir}/gem%{?_compatsuffix} \
    --slave %{_bindir}/rake ruby-rake %{_bindir}/rake%{?_compatsuffix} \
    --slave %{_bindir}/testrb ruby-testrb %{_bindir}/testrb%{?_compatsuffix} \
    --slave %{_mandir}/man1/ruby.1.gz rubyman %{_mandir}/man1/ruby%{?_compatsuffix}.1.gz \
    --slave %{_mandir}/man1/erb.1.gz ruby-erbman %{_mandir}/man1/erb%{?_compatsuffix}.1.gz \
    --slave %{_mandir}/man1/rake.1.gz ruby-rakeman %{_mandir}/man1/rake%{?_compatsuffix}.1.gz

%preun
if [ $1 = 0 ]; then
    %{_sbindir}/alternatives --remove ruby %{_bindir}/ruby%{?_compatsuffix}
fi

%post irb
%{_sbindir}/alternatives --install %{_bindir}/irb ruby-irb %{_bindir}/irb%{?_compatsuffix} 90 \
    --slave %{_mandir}/man1/irb.1.gz ruby-irbman %{_mandir}/man1/irb%{?_compatsuffix}.1.gz

%preun irb
if [ $1 = 0 ]; then
    %{_sbindir}/alternatives --remove ruby-irb %{_bindir}/irb%{?_compatsuffix}
fi

%post rdoc
%{_sbindir}/alternatives --install %{_bindir}/rdoc ruby-rdoc %{_bindir}/rdoc%{?_compatsuffix} 90

%preun rdoc
if [ $1 = 0 ]; then
    %{_sbindir}/alternatives --remove ruby-rdoc %{_bindir}/rdoc%{?_compatsuffix}
fi

%post ri
%{_sbindir}/alternatives --install %{_bindir}/ri ruby-ri %{_bindir}/ri%{?_compatsuffix} 90 \
    --slave %{_mandir}/man1/ri.1.gz ruby-riman %{_mandir}/man1/ri%{?_compatsuffix}.1.gz

%preun ri
if [ $1 = 0 ]; then
    %{_sbindir}/alternatives --remove ruby-ri %{_bindir}/ri%{?_compatsuffix}
fi

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%files
%defattr(-, root, root, -)
%doc COPYING*
%doc ChangeLog
%doc GPL
%doc LEGAL
%doc LGPL
%doc NEWS
%doc README
%doc ToDo
%doc doc/ChangeLog-*
%doc doc/NEWS-*
%{_bindir}/erb%{?_compatsuffix}
%{_bindir}/gem%{?_compatsuffix}
%{_bindir}/rake%{?_compatsuffix}
%{_bindir}/ruby%{?_compatsuffix}
%{_bindir}/testrb%{?_compatsuffix}
%{_mandir}/man1/erb%{?_compatsuffix}.1*
%{_mandir}/man1/rake%{?_compatsuffix}.1*
%{_mandir}/man1/ruby%{?_compatsuffix}.1*

%files devel
%defattr(-, root, root, -)
%doc COPYING*
%doc ChangeLog
%doc GPL
%doc LEGAL
%doc LGPL
%doc README.EXT
%{_includedir}/ruby%{?_compatsuffix}
%{_libdir}/libruby%{?_compatsuffix}.so

%files irb
%defattr(-, root, root, -)
%{_bindir}/irb%{?_compatsuffix}
%{ruby_vendorlib_191}/irb.rb
%{ruby_vendorlib_191}/irb
%{_mandir}/man1/irb%{?_compatsuffix}.1*

%files libs
%defattr(-, root, root, -)
%doc README
%doc COPYING*
%doc ChangeLog
%doc GPL
%doc LEGAL
%doc LGPL
%dir %{_datadir}/ruby
%dir %{ruby_sitelib_191}
%dir %{ruby_sitearch_191}
%dir %{ruby_vendorlib_191}
%{ruby_vendorarch_191}
# The following files should go into the ruby-irb package.
%exclude %{ruby_vendorlib_191}/irb.rb
%exclude %{ruby_vendorlib_191}/irb
# The following files should go into the ruby-rdoc package.
%exclude %{ruby_vendorlib_191}/rdoc
# The following files should go into the ruby-tcltk package.
%exclude %{ruby_vendorlib_191}/*tk.rb
%exclude %{ruby_vendorlib_191}/tcltk.rb
%exclude %{ruby_vendorlib_191}/tk
%exclude %{ruby_vendorlib_191}/tk*.rb
%exclude %{ruby_vendorlib_191}/tkextlib
%exclude %{ruby_vendorarch_191}/tcltklib.so
%exclude %{ruby_vendorarch_191}/tkutil.so
# files in ruby-libs from here
%{ruby_vendorlib_191}/*.rb
%{ruby_vendorlib_191}/bigdecimal
%{ruby_vendorlib_191}/cgi
%{ruby_vendorlib_191}/date
%{ruby_vendorlib_191}/digest
%{ruby_vendorlib_191}/dl
%{ruby_vendorlib_191}/drb
%{ruby_vendorlib_191}/rubygems
%{ruby_vendorlib_191}/io
%{ruby_vendorlib_191}/json
%{ruby_vendorlib_191}/minitest
%{ruby_vendorlib_191}/net
%{ruby_vendorlib_191}/openssl
%{ruby_vendorlib_191}/optparse
%{ruby_vendorlib_191}/racc
%{ruby_vendorlib_191}/rake
%{ruby_vendorlib_191}/rbconfig
%{ruby_vendorlib_191}/rexml
%{ruby_vendorlib_191}/rinda
%{ruby_vendorlib_191}/ripper
%{ruby_vendorlib_191}/rss
%{ruby_vendorlib_191}/shell
%{ruby_vendorlib_191}/test
%{ruby_vendorlib_191}/uri
%{ruby_vendorlib_191}/webrick
%{ruby_vendorlib_191}/xmlrpc
%{ruby_vendorlib_191}/yaml
%{_libdir}/libruby%{?_compatsuffix}.so.*

%files mode
%defattr(-, root, root, -)
#%{_datadir}/emacs/site-lisp/ruby-mode
#%{_datadir}/emacs/site-lisp/site-start.d/ruby-mode-init.el

%files rdoc
%defattr(-, root, root, -)
%{_bindir}/rdoc%{?_compatsuffix}
%{ruby_vendorlib_191}/rdoc

%files ri
%defattr(-, root, root, -)
%{_bindir}/ri%{?_compatsuffix}
%{_datadir}/ri%{?_compatsuffix}
%{_mandir}/man1/ri%{?_compatsuffix}.1*

%files static
%defattr(-, root, root, -)
%{_libdir}/libruby%{?_compatsuffix}-static.a

%files tcltk
%defattr(-, root, root, -)
%{ruby_vendorlib_191}/*-tk.rb
%{ruby_vendorlib_191}/tcltk.rb
%{ruby_vendorlib_191}/tk
%{ruby_vendorlib_191}/tk*.rb
%{ruby_vendorlib_191}/tkextlib
%{ruby_vendorarch_191}/tcltklib.so
%{ruby_vendorarch_191}/tkutil.so

%changelog
* Mon Dec 28 2009 Jeroen van Meeuwen <j.van.meeuwen@ogd.nl> - 1.9.1-376-11
- Add Provides ruby(devel)
- Fix Provides ruby(irb)

* Thu Dec 24 2009 Jeroen van Meeuwen <j.van.meeuwen@ogd.nl> - 1.9.1-376-10
- Remove -devel requirement for -static
- Fix header directory (Ben Shakal)
- Fix gem_prelude.rb (Ben Shakal)

* Mon Dec 21 2009 Jeroen van Meeuwen <j.van.meeuwen@ogd.nl> - 1.9.1-376-6
- New upstream version
