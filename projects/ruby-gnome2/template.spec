%{!?ruby_sitelib: %define ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")}
%{!?ruby_sitearch: %define ruby_sitearch %(ruby -rrbconfig -e "puts Config::CONFIG['sitearchdir']")}

%define         xulrunner_still_beta   1
#%%define         betaver                svn3690_trunk

#
# When changing release number, please make it sure that
# the new EVR won't be higher than the one of higher branch!!
#
%define         mainrel                3

# Note
# Currently this spec file does not support libgda module.
# libgda-2 is needed, API change for libgda-3 needs investigation
# - Mamoru Tasaka

Name:           <%= name %>
Version:        <%= version %>
#
# When changing release number, please make it sure that
# the new EVR won't be higher than the one of higher branch!!
#
Release:        %{mainrel}%{?dist}
Summary:        Ruby binding of libgnome/libgnomeui-2.x

Group:          System Environment/Libraries

License:        LGPLv2
URL:            http://ruby-gnome2.sourceforge.jp/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-all-%{version}.tar.gz
#Source0:        %{name}-all-%{version}-%{betaver}.tar.gz
# Currently Fedora specific patch
# Fix shebang on sample files
Patch0:         ruby-gnome2-0.17.0-rc1-script.patch

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  ruby ruby-devel gtk2-devel libgnome-devel libgnomeui-devel
BuildRequires:  ruby(abi)

Requires:       ruby(abi)
Requires:       ruby(gnomecanvas2) = %{version}-%{release}

Provides:       ruby(gnome2) =  %{version}-%{release}


%description
Ruby/GNOME2 is a Ruby binding of libgnome/libgnomeui-2.x.

%package devel
Summary:        Development libraries and header files for ruby-gnome2
Group:          Development/Libraries

Requires:       ruby(gnome2) = %{version}-%{release}
Requires:       pkgconfig
Provides:       ruby(gnome2-devel) = %{version}-%{release}

%description devel
Ruby/GNOME2 is a Ruby binding of libgnome/libgnomeui-2.x.
This package provides libraries and header files for ruby-gnome2

%package -n ruby-atk
Summary:        Ruby binding of ATK-1.0.x or later
Group:          System Environment/Libraries

BuildRequires:  ruby ruby-devel glib2-devel atk-devel 
#BuildRequires:  ruby(glib2-devel) = %{version}

Requires:       ruby(abi) ruby(glib2) = %{version}-%{release}

Provides:       ruby(atk) = %{version}-%{release}

%description -n ruby-atk
Ruby/ATK is a Ruby binding of ATK-1.0.x or later.

%package -n ruby-atk-devel
Summary:        Development libraries and header files for ruby-atk
Group:          Development/Libraries

Requires:       ruby-devel ruby(atk) = %{version}-%{release} 
Requires:       ruby(glib2-devel) = %{version}-%{release}
Requires:       atk-devel
Requires:       pkgconfig

Provides:       ruby(atk-devel) = %{version}-%{release}

%description -n ruby-atk-devel
Ruby/ATK is a Ruby binding of ATK-1.0.x or later.
This package provides libraries and header files for ruby-atk

%package -n ruby-bonobo2
Summary:        Ruby binding of libbonobo-2.x
Group:          System Environment/Libraries

BuildRequires:  ruby ruby-devel
BuildRequires:  libbonoboui-devel

Requires:       ruby(abi) ruby(gtk2) = %{version}-%{release}

Provides:       ruby(bonobo2) = %{version}-%{release}

%description -n ruby-bonobo2
Ruby/Bonobo2 is a Ruby binding of libbonobo-2.x.

%package -n ruby-bonobo2-devel
Summary:        Development libraries and header files for ruby-bonobo2
Group:          Development/Libraries

Requires:       ruby(bonobo2) = %{version}-%{release}
Requires:       pkgconfig
Provides:       ruby(bonobo2-devel) = %{version}-%{release}

%description -n ruby-bonobo2-devel
Ruby/Bonobo2 is a Ruby binding of libbonobo-2.x.
This package provides libraries and header files for ruby-bonobo2

%package -n ruby-bonoboui2
Summary:        Ruby binding of libbonoboui-2.x
Group:          System Environment/Libraries

BuildRequires:  ruby ruby-devel
BuildRequires:  libbonoboui-devel libgnomeui-devel

Requires:       ruby(abi) ruby(gnome2) = %{version}-%{release}

Provides:       ruby(bonoboui2) = %{version}-%{release}

%description -n ruby-bonoboui2
Ruby/BonoboUI2 is a Ruby binding of libbonoboui-2.x.

%package -n ruby-bonoboui2-devel
Summary:        Development libraries and header files for ruby-bonoboui2
Group:          Development/Libraries

Requires:       ruby(bonoboui2) = %{version}-%{release}
Requires:       pkgconfig
Provides:       ruby(bonoboui2-devel) = %{version}-%{release}

%description -n ruby-bonoboui2-devel
Ruby/BonoboUI2 is a Ruby binding of libbonoboui-2.x.
This package provides libraries and header files for ruby-bonoboui2

%package -n ruby-gconf2
Summary:        Ruby binding of GConf-2.x
Group:          System Environment/Libraries

BuildRequires:  ruby ruby-devel GConf2-devel

Requires:       ruby(abi) ruby(glib2) = %{version}-%{release}

Provides:       ruby(gconf2) =  %{version}-%{release}

%description -n ruby-gconf2
Ruby/GConf2 is a Ruby binding of GConf-2.x.

%package -n ruby-gconf2-devel
Summary:        Development libraries and header files for ruby-gconf2
Group:          Development/Libraries

Requires:       ruby(gconf2) = %{version}-%{release}
Requires:       pkgconfig
Provides:       ruby(gconf2-devel) = %{version}-%{release}

%description -n ruby-gconf2-devel
Ruby/GConf2 is a Ruby binding of GConf-2.x.
This package provides libraries and header files for ruby-gconf2

%package -n ruby-gdkpixbuf2
Summary:        Ruby binding of GdkPixbuf-2.x
Group:          System Environment/Libraries

BuildRequires:  ruby ruby-devel gtk2-devel ruby-cairo-devel
#BuildRequires:  ruby(glib2-devel) = %{version} ruby(gtk2-devel) = %{version}

Requires:       ruby(abi)
Requires:       ruby(glib2) = %{version}-%{release} ruby(cairo)

Provides:       ruby(gdkpixbuf2) =  %{version}-%{release}

%description -n ruby-gdkpixbuf2
Ruby/GdkPixbuf2 is a Ruby binding of GdkPixbuf-2.x.

%package -n ruby-gdkpixbuf2-devel
Summary:        Development libraries and header files for ruby-gdkpixbuf2
Group:          Development/Libraries

Requires:       ruby(gdkpixbuf2) = %{version}-%{release}
Requires:       pkgconfig
Provides:       ruby(gdkpixbuf2-devel) = %{version}-%{release}

%description -n ruby-gdkpixbuf2-devel
Ruby/GdkPixbuf2 is a Ruby binding of GdkPixbuf-2.x.
This package provides libraries and header files for ruby-gdkpixbuf2

%package -n ruby-glib2
Summary:        Ruby binding of GLib-2.x
Group:          System Environment/Libraries

BuildRequires:  ruby ruby-devel glib2-devel

Requires:       ruby(abi)

Provides:       ruby(glib2) =  %{version}-%{release}

%description -n ruby-glib2
Ruby/GLib2 is a Ruby binding of GLib-2.x.

%package -n ruby-glib2-devel
Summary:        Development libraries and header files for ruby-glib2
Group:          Development/Libraries

Requires:       ruby(glib2) =  %{version}-%{release}
Requires:       ruby-devel glib2-devel
Requires:       pkgconfig

Provides:       ruby(glib2-devel) =  %{version}-%{release}

%description -n ruby-glib2-devel
Ruby/GLib2 is a Ruby binding of GLib-2.x.
This package provides libraries and header files for ruby-glib2

%package -n ruby-gnomecanvas2
Summary:        Ruby binding of GnomeCanvas-2.x
Group:          System Environment/Libraries

BuildRequires:  ruby ruby-devel gtk2-devel libgnomecanvas-devel

Requires:       ruby(abi)
Requires:       ruby(gtk2) = %{version}-%{release} 
Requires:       ruby(libart2) = %{version}-%{release}

Provides:       ruby(gnomecanvas2) =  %{version}-%{release}

%description -n ruby-gnomecanvas2
Ruby/GnomeCanvas2 is a Ruby binding of GnomeCanvas-2.x.

%package -n ruby-gnomecanvas2-devel
Summary:        Development libraries and header files for ruby-gnomecanvas2
Group:          Development/Libraries

Requires:       ruby(gnomecanvas2) = %{version}-%{release}
Requires:       pkgconfig
Provides:       ruby(gnomecanvas2-devel) = %{version}-%{release}

%description -n ruby-gnomecanvas2-devel
Ruby/GnomeCanvas2 is a Ruby binding of GnomeCanvas-2.x.
This package provides libraries and header files for ruby-gnomecanvas2

%package -n ruby-gnomeprint2
Summary:        Ruby binding of libgnomeprint
Group:          System Environment/Libraries

BuildRequires:  ruby ruby-devel libgnomeprint22-devel
#BuildRequires:  ruby(glib2-devel) = %{version} ruby(pango-devel) = %{version} 
#BuildRequires:  ruby(libart2-devel) = %{version}

Requires:       ruby(abi)
Requires:       ruby(glib2) = %{version}-%{release} ruby(pango) = %{version}-%{release}
Requires:       ruby(libart2) = %{version}-%{release}

Provides:       ruby(gnomeprint2) =  %{version}-%{release}

%description -n ruby-gnomeprint2
Ruby/GnomePrint is a Ruby binding of libgnomeprint. 

%package -n ruby-gnomeprint2-devel
Summary:        Development libraries and header files for ruby-gnomeprint2
Group:          Development/Libraries

Requires:       ruby(gnomeprint2) = %{version}-%{release}
Requires:       pkgconfig
Provides:       ruby(gnomeprint2-devel) = %{version}-%{release}

%description -n ruby-gnomeprint2-devel
Ruby/GnomePrint is a Ruby binding of libgnomeprint.
This package provides libraries and header files for ruby-gnomeprint2

%package -n ruby-gnomeprintui2
Summary:        Ruby binding of libgnomeprintui
Group:          System Environment/Libraries

BuildRequires:  ruby ruby-devel libgnomeprintui22-devel
#BuildRequires:  ruby(gtk2-devel) = %{version}

Requires:       ruby(abi)
Requires:       ruby(gtk2) = %{version}-%{release} ruby(gnomeprint2) = %{version}-%{release}

Provides:       ruby(gnomeprintui2) =  %{version}-%{release}

%description -n ruby-gnomeprintui2
Ruby/GnomePrintUI is a Ruby binding of libgnomeprintui.

%package -n ruby-gnomeprintui2-devel
Summary:        Development libraries and header files for ruby-gnomeprintui2
Group:          Development/Libraries

Requires:       ruby(gnomeprintui2) = %{version}-%{release}
Requires:       pkgconfig
Provides:       ruby(gnomeprintui2-devel) = %{version}-%{release}

%description -n ruby-gnomeprintui2-devel
Ruby/GnomePrintUI is a Ruby binding of libgnomeprintui.
This package provides libraries and header files for ruby-gnomeprintui2

%package -n ruby-gnomevfs
Summary:        Ruby binding of GnomeVFS-2.0.x
Group:          System Environment/Libraries

BuildRequires:  ruby ruby-devel gnome-vfs2-devel

Requires:       ruby(abi)
Requires:       ruby(glib2) = %{version}-%{release}

Provides:       ruby(gnomevfs) =  %{version}-%{release}

%description -n ruby-gnomevfs
Ruby/GnomeVFS is a Ruby binding of GnomeVFS-2.0.x.

%package -n ruby-gnomevfs-devel
Summary:        Development libraries and header files for ruby-gnomevfs
Group:          Development/Libraries

Requires:       ruby(gnomevfs) = %{version}-%{release}
Requires:       pkgconfig
Provides:       ruby(gnomevfs-devel) = %{version}-%{release}

%description -n ruby-gnomevfs-devel
Ruby/GnomeVFS is a Ruby binding of GnomeVFS-2.0.x.
This package provides libraries and header files for ruby-gnomevfs

%package -n ruby-goocanvas
Summary:        Ruby binding of Goocanvas.
Group:          System Environment/Libraries

BuildRequires:  ruby ruby-devel goocanvas-devel

Requires:       ruby(abi)
Requires:       ruby(glib2) = %{version}-%{release}

Provides:       ruby(goocanvas) =  %{version}-%{release}

%description -n ruby-goocanvas
Ruby/Goocanvas is a Ruby binding of Goocanvas

%package -n ruby-goocanvas-devel
Summary:        Development libraries and header files for ruby-goocanvas
Group:          Development/Libraries

Requires:       ruby(goocanvas) = %{version}-%{release}
Requires:       pkgconfig
Provides:       ruby(goocanvas-devel) = %{version}-%{release}

%description -n ruby-goocanvas-devel
Ruby/Goocanvas is a Ruby binding of Goocanvas
This package provides libraries and header files for ruby-gnomecanvas

%package -n ruby-gstreamer
Summary:        Ruby binding of GStreamer
Group:          System Environment/Libraries

BuildRequires:  ruby ruby-devel
BuildRequires:  gstreamer-devel gstreamer-plugins-base-devel

Requires:       ruby(abi)
Requires:       ruby(glib2) = %{version}-%{release}

Provides:       ruby(gstreamer) = %{version}-%{release}

%description -n ruby-gstreamer
Ruby/GStreamer is a Ruby binding for GStreamer

%package -n ruby-gstreamer-devel
Summary:        Development libraries and header files for ruby-gstreamer
Group:          Development/Libraries

Requires:       ruby(gstreamer) = %{version}-%{release}
Requires:       pkgconfig
Provides:       ruby(gstreamer-devel) = %{version}-%{release}

%description -n ruby-gstreamer-devel
Ruby/GStreamer is a Ruby binding for GStreamer
This package provides libraries and header files for ruby-gstreamer

%package -n ruby-gtk2
Summary:        Ruby binding of GTK+-2.0.x
Group:          System Environment/Libraries

BuildRequires:  ruby gtk2-devel ruby-cairo-devel
#BuildRequires:  ruby(glib2-devel) = %{version} ruby(pango-devel) = %{version}

Requires:       %{_bindir}/env
Requires:       ruby(abi)
Requires:       ruby(glib2) = %{version}-%{release} ruby(atk) = %{version}-%{release}
Requires:       ruby(pango) =  %{version}-%{release} ruby(cairo)
Requires:       ruby(gdkpixbuf2) =  %{version}-%{release}

Provides:       ruby(gtk2) = %{version}-%{release}

%description -n ruby-gtk2
Ruby/GTK2 is a Ruby binding of GTK+-2.0.x.

%package -n ruby-gtk2-devel
Summary:        Development libraries and header files for ruby-gtk2
Group:          Development/Libraries

Requires:       ruby(gtk2) =  %{version}-%{release}
Requires:       gtk2-devel ruby-devel ruby(glib2-devel) = %{version}-%{release}
Requires:       pkgconfig

Provides:       ruby(gtk2-devel) = %{version}-%{release}

%description -n ruby-gtk2-devel
Ruby/GTK2 is a Ruby binding of GTK+-2.0.x.
This package provides libraries and header files for ruby-gtk2

%package -n ruby-gtkglext
Summary:        Ruby binding of GtkGLExt
Group:          System Environment/Libraries

BuildRequires:  ruby ruby-devel gtk2-devel gtkglext-devel
#BuildRequires:  ruby(glib2-devel) = %{version} ruby(gtk2-devel) = %{version}

Requires:       ruby(abi)
Requires:       ruby(opengl)
Requires:       ruby(gtk2) = %{version}-%{release}

Provides:       ruby(gtkglext) = %{version}-%{release}

%description -n ruby-gtkglext
Ruby/GtkGLExt is a Ruby binding of GtkGLExt.

%package -n ruby-gtkglext-devel
Summary:        Development libraries and header files for ruby-gtkglext
Group:          Development/Libraries

Requires:       ruby(gtkglext) = %{version}-%{release}
Requires:       pkgconfig
Provides:       ruby(gtkglext-devel) = %{version}-%{release}

%description -n ruby-gtkglext-devel
Ruby/GtkGLExt is a Ruby binding of GtkGLExt.
This package provides libraries and header files for ruby-gtkglext

%package -n ruby-gtkhtml2
Summary:        Ruby binding of GtkHtml2
Group:          System Environment/Libraries

BuildRequires:  ruby ruby-devel gtk2-devel gtkhtml2-devel

Requires:       ruby(abi)
Requires:       ruby(gtk2) = %{version}-%{release}

Provides:       ruby(gtkhtml2) = %{version}-%{release}

%description -n ruby-gtkhtml2
Ruby/GtkHtml2 is a Ruby binding of GtkHtml2

%package -n ruby-gtkhtml2-devel
Summary:        Development libraries and header files for ruby-gtkhtml2
Group:          Development/Libraries

Requires:       ruby(gtkhtml2) = %{version}-%{release}
Requires:       pkgconfig
Provides:       ruby(gtkhtml2-devel) = %{version}-%{release}

%description -n ruby-gtkhtml2-devel
Ruby/GtkHtml2 is a Ruby binding of GtkHtml2
This package provides libraries and header files for ruby-gtkhtml2

%package -n ruby-gtkmozembed
Summary:        Ruby binding of GtkMozEmbed
Group:          System Environment/Libraries

BuildRequires:  ruby ruby-devel gtk2-devel pango-devel 

BuildRequires:  gecko-devel >= 1.9
BuildRequires:  gecko-devel-unstable >= 1.9
Requires:       gecko-libs >= 1.9

Requires:       ruby(abi)
Requires:       ruby(gtk2) = %{version}-%{release} 

Provides:       ruby(gtkmozembed) = %{version}-%{release}

%description -n ruby-gtkmozembed
Ruby/GtkMozEmbed is a Ruby binding of GtkMozEmbed a widget embedding a
Mozilla Gecko renderer.

%package -n ruby-gtkmozembed-devel
Summary:        Development libraries and header files for ruby-gtkmozembed
Group:          Development/Libraries

Requires:       ruby(gtkmozembed) = %{version}-%{release}
Requires:       pkgconfig
Provides:       ruby(gtkmozembed-devel) = %{version}-%{release}

%description -n ruby-gtkmozembed-devel
Ruby/GtkMozEmbed is a Ruby binding of GtkMozEmbed a widget embedding a
Mozilla Gecko renderer.
This package provides libraries and header files for ruby-gtkmozembed

%package -n ruby-gtksourceview
Summary:        Ruby binding of gtksourceview-1.0.x
Group:          System Environment/Libraries

BuildRequires:  ruby ruby-devel gtksourceview-devel
#BuildRequires:  ruby(gnome2) = %{version}

Requires:       ruby(abi)
Requires:       ruby(gtk2) = %{version}-%{release}

Provides:       ruby(gtksourceview) = %{version}-%{release}

%description -n ruby-gtksourceview
Ruby/GtkSourceView is a Ruby binding of gtksourceview-1.0.x.

%package -n ruby-gtksourceview-devel
Summary:        Development libraries and header files for ruby-gtksourceview
Group:          Development/Libraries

Requires:       ruby(gtksourceview) = %{version}-%{release}
Requires:       pkgconfig
Provides:       ruby(gtksourceview-devel) = %{version}-%{release}

%description -n ruby-gtksourceview-devel
Ruby/GtkSourceView is a Ruby binding of gtksourceview-1.0.x.
This package provides libraries and header files for ruby-gtksourceview

%package -n ruby-gtksourceview2
Summary:        Ruby binding of gtksourceview-2.x
Group:          System Environment/Libraries

BuildRequires:  ruby ruby-devel gtksourceview2-devel
#BuildRequires:  ruby(gnome2) = %{version}

Requires:       ruby(abi)
Requires:       ruby(gtk2) = %{version}-%{release}

Provides:       ruby(gtksourceview2) = %{version}-%{release}

%description -n ruby-gtksourceview2
Ruby/GtkSourceView2 is a Ruby binding of gtksourceview-2.x.

%package -n ruby-gtksourceview2-devel
Summary:        Development libraries and header files for ruby-gtksourceview2
Group:          Development/Libraries

Requires:       ruby(gtksourceview2) = %{version}-%{release}
Requires:       pkgconfig
Provides:       ruby(gtksourceview2-devel) = %{version}-%{release}

%description -n ruby-gtksourceview2-devel
Ruby/GtkSourceView2 is a Ruby binding of gtksourceview-2.x.
This package provides libraries and header files for ruby-gtksourceview2

%package -n ruby-libart2
Summary:        Ruby binding of Libart_lgpl
Group:          System Environment/Libraries

BuildRequires:  ruby ruby-devel libart_lgpl-devel libpng-devel libjpeg-devel
#BuildRequires:  ruby(glib2-devel) = %{version}

Requires:       ruby(abi)

Provides:       ruby(libart2) = %{version}-%{release}

%description -n ruby-libart2
Ruby/Libart2 is a Ruby binding of Libart_lgpl. 

%package -n ruby-libart2-devel
Summary:        Development libraries and header files for ruby-libart2
Group:          Development/Libraries

Requires:       ruby(libart2) = %{version}-%{release}
Requires:       libart_lgpl-devel ruby-devel
Requires:       pkgconfig

Provides:       ruby(libart2-devel) = %{version}-%{release}

%description -n ruby-libart2-devel
Ruby/Libart2 is a Ruby binding of Libart_lgpl. 
This package provides libraries and header files for ruby-libart2


%package -n ruby-libglade2
Summary:        Ruby bindings of Libglade2
Group:          System Environment/Libraries

BuildRequires:  ruby ruby-devel gtk2-devel libgnome-devel libglade2-devel
#BuildRequires:  ruby(glib2-devel) = %{version} ruby(gnome2) = %{version}

Requires:       ruby(abi)
Requires:       ruby(gtk2) = %{version}-%{release}
Requires:       ruby(gnome2) = %{version}-%{release}

Provides:       ruby(libglade2) = %{version}-%{release}

%description -n ruby-libglade2
Ruby/Libglade2 is a Ruby bindings of Libglade2.
This provides a very simple interface to the libglade library,
to load interfaces dynamically from a glade file.

%package -n ruby-libglade2-devel
Summary:        Development libraries and header files for ruby-libglade2
Group:          Development/Libraries

Requires:       ruby(libglade2) = %{version}-%{release}
Requires:       pkgconfig
Provides:       ruby(libglade2-devel) = %{version}-%{release}

%description -n ruby-libglade2-devel
Ruby/Libglade2 is a Ruby bindings of Libglade2.
This package provides libraries and header files for ruby-libglade2

%package -n ruby-panelapplet2
Summary:        Ruby binding of libpanel-applet-2.6.x
Group:          System Environment/Libraries

BuildRequires:  ruby ruby-devel gtk2-devel gnome-panel-devel libgnome-devel 
BuildRequires:  libgnomeui-devel 
#BuildRequires:  ruby(glib2-devel) = %{version} ruby(gtk2-devel) = %{version}

Requires:       %{_bindir}/env
Requires:       %{_bindir}/ruby
Requires:       ruby(abi)
Requires:       ruby(gnome2) = %{version}-%{release}

Provides:       ruby(panelapplet2) = %{version}-%{release}

%description -n ruby-panelapplet2
Ruby/PanelApplet2 is a Ruby binding of libpanel-applet-2.6.x.

%package -n ruby-panelapplet2-devel
Summary:        Development libraries and header files for ruby-panelapplet2
Group:          Development/Libraries

Requires:       ruby(panelapplet2) = %{version}-%{release}
Requires:       pkgconfig
Provides:       ruby(panelapplet2-devel) = %{version}-%{release}

%description -n ruby-panelapplet2-devel
Ruby/PanelApplet2 is a Ruby binding of libpanel-applet-2.6.x.
This package provides libraries and header files for ruby-panelapplet2

%package -n ruby-pango
Summary:        Ruby binding of pango-1.x
Group:          System Environment/Libraries

BuildRequires:  ruby ruby-devel glib2-devel pango-devel cairo-devel ruby-cairo-devel
#BuildRequires:  ruby(glib2-devel) = %{version}

Requires:       ruby(abi)
Requires:       ruby(glib2) = %{version}-%{release} ruby(cairo)

Provides:       ruby(pango) = %{version}-%{release}

%description -n ruby-pango
Ruby/Pango is a Ruby binding of pango-1.x.

%package -n ruby-pango-devel
Summary:        Development libraries and header files for ruby-pango
Group:          Development/Libraries

Requires:       ruby(pango) = %{version}-%{release} 
Requires:       pango-devel ruby-devel ruby(glib2-devel) = %{version}-%{release}
Requires:       ruby-cairo-devel
Requires:       pkgconfig

Provides:       ruby(pango-devel) = %{version}-%{release}

%description -n ruby-pango-devel
Ruby/Pango is a Ruby binding of pango-1.x.
This package provides libraries and header files for ruby-pango

%package -n ruby-poppler
Summary:        Ruby binding of poppler-glib
Group:          System Environment/Libraries

BuildRequires:  ruby ruby-devel poppler-devel cairo-devel ruby-cairo-devel
%if 0%{?fedora} >= 9
BuildRequires:  poppler-glib-devel
%endif
#BuildRequires:  ruby(glib2-devel) = %{version} ruby(gdkpixbuf2) = %{version}

Requires:       %{_bindir}/env
Requires:       ruby(abi)
Requires:       ruby(gdkpixbuf2) = %{version}-%{release}
Requires:       ruby(gtk2) = %{version}-%{release} ruby(cairo)

Provides:       ruby(poppler) = %{version}-%{release}

%description -n ruby-poppler
Ruby/Poppler is a Ruby binding of poppler-glib.

%package -n ruby-poppler-devel
Summary:        Development libraries and header files for ruby-poppler
Group:          Development/Libraries

Requires:       ruby(poppler) = %{version}-%{release}
Requires:       pkgconfig
Provides:       ruby(poppler-devel) = %{version}-%{release}

%description -n ruby-poppler-devel
Ruby/Poppler is a Ruby binding of poppler-glib.
This package provides libraries and header files for ruby-poppler

%package -n ruby-rsvg
Summary:        Ruby binding of librsvg
Group:          System Environment/Libraries

BuildRequires:  ruby ruby-devel librsvg2-devel ruby-cairo-devel
#BuildRequires:  ruby(glib2-devel) = %{version} ruby(gdkpixbuf2) = %{version}

Requires:       %{_bindir}/env
Requires:       ruby(abi)
Requires:       ruby(gdkpixbuf2) = %{version}-%{release}
Requires:       ruby(cairo)

Provides:       ruby(rsvg) = %{version}-%{release}

%description -n ruby-rsvg
Ruby/RSVG is a Ruby binding of librsvg.

%package -n ruby-rsvg-devel
Summary:        Development libraries and header files for ruby-rsvg
Group:          Development/Libraries

Requires:       ruby(rsvg) = %{version}-%{release}
Requires:       pkgconfig
Provides:       ruby(rsvg-devel) = %{version}-%{release}

%description -n ruby-rsvg-devel
Ruby/RSVG is a Ruby binding of librsvg.
This package provides libraries and header files for ruby-rsvg

%package -n ruby-vte
Summary:        Ruby binding of VTE
Group:          System Environment/Libraries

BuildRequires:  ruby ruby-devel vte-devel
#BuildRequires:  ruby(gtk2-devel) = %{version}

Requires:       %{_bindir}/env
Requires:       ruby(abi)
Requires:       ruby(gtk2) = %{version}-%{release}

Provides:       ruby(vte) = %{version}-%{release}

%description -n ruby-vte
Ruby/VTE is a Ruby binding of VTE.

%package -n ruby-vte-devel
Summary:        Development libraries and header files for ruby-vte
Group:          Development/Libraries

Requires:       ruby(vte) = %{version}-%{release}
Requires:       pkgconfig
Provides:       ruby(vte-devel) = %{version}-%{release}

%description -n ruby-vte-devel
Ruby/VTE is a Ruby binding of VTE.
This package provides libraries and header files for ruby-vte


%prep
%setup -q -n %{name}-all-%{version}
#%%setup -q -n %{name}-all-%{version}-%{betaver}
%patch0 -p1

# Keep timestamps as much as possible
find . -type f -name depend | xargs sed -i -e 's|-m 0644 -v|-m 0644 -p -v|'

# Fix the attributes of some files
# suppress lots of messages..
set +x
find . -name \*.rb -or -name \*.c | while read f ; do
        chmod 0644 $f
done
set -x

# cleanup
# find . -type d -path '*/sample/*.svn' | sort -r | xargs rm -rf

%build
ruby extconf.rb
export CFLAGS="$RPM_OPT_FLAGS"

make %{?_smp_mflags} -k

%install
rm -rf $RPM_BUILD_ROOT

# Already fixed in rev 3682
mkdir -p $RPM_BUILD_ROOT%{_libdir}/pkgconfig

make install DESTDIR=$RPM_BUILD_ROOT INSTALL="%{__install} -p"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc gnome/README gnome/ChangeLog gnome/COPYING.LIB gnome/sample
%doc AUTHORS NEWS
%{ruby_sitelib}/gnome2.rb
%{ruby_sitearch}/gnome2.so

%files devel
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/ruby-gnome2.pc

%files -n ruby-atk
%defattr(-,root,root,-)
%doc atk/ChangeLog atk/COPYING.LIB atk/README
%{ruby_sitelib}/atk.rb
%{ruby_sitearch}/atk.so

%files -n ruby-atk-devel
%defattr(-,root,root,-)
%{ruby_sitearch}/rbatk.h
%{ruby_sitearch}/rbatkversion.h
%{_libdir}/pkgconfig/ruby-atk.pc

%files -n ruby-bonobo2
%defattr(-,root,root,-)
%doc bonobo/ChangeLog bonobo/COPYING.LIB bonobo/README
%{ruby_sitelib}/bonobo2.rb
%{ruby_sitearch}/bonobo2.so

%files -n ruby-bonobo2-devel
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/ruby-bonobo2.pc

%files -n ruby-bonoboui2
%defattr(-,root,root,-)
%doc bonoboui/ChangeLog bonoboui/COPYING.LIB bonoboui/README
%{ruby_sitelib}/bonoboui2.rb
%{ruby_sitearch}/bonoboui2.so

%files -n ruby-bonoboui2-devel
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/ruby-bonoboui2.pc

%files -n ruby-gconf2
%defattr(-,root,root,-)
%doc gconf/ChangeLog gconf/COPYING.LIB gconf/README gconf/sample
%{ruby_sitelib}/gconf2.rb
%{ruby_sitearch}/gconf2.so

%files -n ruby-gconf2-devel
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/ruby-gconf2.pc

%files -n ruby-gdkpixbuf2
%defattr(-,root,root,-)
%doc gdkpixbuf/ChangeLog gdkpixbuf/COPYING.LIB gdkpixbuf/README gdkpixbuf/sample
%{ruby_sitelib}/gdk_pixbuf2.rb
%{ruby_sitearch}/gdk_pixbuf2.so

%files -n ruby-gdkpixbuf2-devel
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/ruby-gdkpixbuf2.pc

%files -n ruby-glib2
%defattr(-,root,root,-)
%doc glib/ChangeLog glib/COPYING.LIB glib/README glib/sample
%{ruby_sitelib}/glib2.rb
%{ruby_sitelib}/glib-mkenums.rb
%{ruby_sitelib}/mkmf-gnome2.rb
%{ruby_sitelib}/pkg-config.rb
%{ruby_sitearch}/glib2.so

%files -n ruby-glib2-devel
%defattr(-,root,root,-)
%{ruby_sitearch}/rbgcompat.h
%{ruby_sitearch}/rbglib.h
%{ruby_sitearch}/rbgobject.h
%{ruby_sitearch}/rbgutil.h
%{ruby_sitearch}/glib-enum-types.h
%{_libdir}/pkgconfig/ruby-glib2.pc

%files -n ruby-gnomecanvas2
%defattr(-,root,root,-)
%doc gnomecanvas/ChangeLog gnomecanvas/COPYING.LIB gnomecanvas/README gnomecanvas/sample
%{ruby_sitelib}/gnomecanvas2.rb
%{ruby_sitearch}/gnomecanvas2.so

%files -n ruby-gnomecanvas2-devel
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/ruby-gnomecanvas2.pc

%files -n ruby-gnomeprint2
%defattr(-,root,root,-)
%doc gnomeprint/ChangeLog gnomeprint/COPYING.LIB gnomeprint/README gnomeprint/sample
%{ruby_sitelib}/gnomeprint2.rb
%{ruby_sitearch}/gnomeprint2.so

%files -n ruby-gnomeprint2-devel
%defattr(-,root,root,-)
%{ruby_sitearch}/rblibgnomeprintversion.h
%{_libdir}/pkgconfig/ruby-gnomeprint2.pc

%files -n ruby-gnomeprintui2
%defattr(-,root,root,-)
%doc gnomeprintui/ChangeLog gnomeprintui/COPYING.LIB gnomeprintui/README gnomeprintui/sample
%{ruby_sitelib}/gnomeprintui2.rb
%{ruby_sitearch}/gnomeprintui2.so

%files -n ruby-gnomeprintui2-devel
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/ruby-gnomeprintui2.pc

%files -n ruby-gnomevfs
%defattr(-,root,root,-)
%doc gnomevfs/ChangeLog gnomevfs/COPYING.LIB gnomevfs/README
%{ruby_sitelib}/gnomevfs.rb
%{ruby_sitearch}/gnomevfs.so

%files -n ruby-gnomevfs-devel
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/ruby-gnomevfs.pc

%files -n ruby-goocanvas
%defattr(-,root,root,-)
%doc goocanvas/ChangeLog goocanvas/README goocanvas/sample
%{ruby_sitelib}/goocanvas.rb
%{ruby_sitearch}/goocanvas.so

%files -n ruby-goocanvas-devel
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/ruby-goocanvas.pc

%files -n ruby-gstreamer
%defattr(-,root,root,-)
%doc gstreamer/ChangeLog gstreamer/COPYING.LIB gstreamer/README
%{ruby_sitelib}/gst.rb
%{ruby_sitearch}/gst.so

%files -n ruby-gstreamer-devel
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/ruby-gstreamer.pc

%files -n ruby-gtk2
%defattr(-,root,root,-)
%doc gtk/ChangeLog gtk/COPYING.LIB gtk/README gtk/sample
%attr(755, root, root) %{ruby_sitelib}/gtk2.rb
#%{ruby_sitelib}/gtk2.rb
%dir %{ruby_sitelib}/gtk2
%attr(755, root, root) %{ruby_sitelib}/gtk2/base.rb
#%{ruby_sitelib}/gtk2/base.rb
%{ruby_sitearch}/gtk2.so

%files -n ruby-gtk2-devel
%defattr(-,root,root,-)
%{ruby_sitearch}/rbgdk.h
%{ruby_sitearch}/rbgdkconversions.h
%{ruby_sitearch}/rbgtk.h
%{ruby_sitearch}/rbgtkconversions.h
%{ruby_sitearch}/rbgtkmacros.h
%{_libdir}/pkgconfig/ruby-gtk2.pc

%files -n ruby-gtkglext
%defattr(-,root,root,-)
%doc gtkglext/ChangeLog COPYING.LIB gtkglext/README gtkglext/README.rbogl gtkglext/sample
%{ruby_sitelib}/gtkglext.rb
%{ruby_sitearch}/gtkglext.so

%files -n ruby-gtkglext-devel
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/ruby-gtkglext.pc

%files -n ruby-gtkhtml2
%defattr(-,root,root,-)
%doc gtkhtml2/ChangeLog gtkhtml2/COPYING.LIB gtkhtml2/README gtkhtml2/sample
%{ruby_sitelib}/gtkhtml2.rb
%{ruby_sitearch}/gtkhtml2.so

%files -n ruby-gtkhtml2-devel
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/ruby-gtkhtml2.pc

%files -n ruby-gtkmozembed
%defattr(-,root,root,-)
%doc gtkmozembed/ChangeLog gtkmozembed/COPYING.LIB gtkmozembed/README gtkmozembed/sample
%{ruby_sitelib}/gtkmozembed.rb
%{ruby_sitearch}/gtkmozembed.so

%files -n ruby-gtkmozembed-devel
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/ruby-gtkmozembed.pc

%files -n ruby-gtksourceview
%defattr(-,root,root,-)
%doc gtksourceview/ChangeLog gtksourceview/COPYING.LIB gtksourceview/README gtksourceview/sample
%{ruby_sitelib}/gtksourceview.rb
%{ruby_sitearch}/gtksourceview.so

%files -n ruby-gtksourceview-devel
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/ruby-gtksourceview.pc

%files -n ruby-gtksourceview2
%defattr(-,root,root,-)
%doc gtksourceview2/ChangeLog gtksourceview2/COPYING.LIB gtksourceview2/README gtksourceview2/sample
%{ruby_sitelib}/gtksourceview2.rb
%{ruby_sitearch}/gtksourceview2.so

%files -n ruby-gtksourceview2-devel
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/ruby-gtksourceview2.pc

%files -n ruby-libart2
%defattr(-,root,root,-)
%doc libart/ChangeLog libart/COPYING.LIB libart/README libart/sample
%{ruby_sitelib}/libart2.rb
%{ruby_sitearch}/libart2.so

%files -n ruby-libart2-devel
%defattr(-,root,root,-)
%{ruby_sitearch}/rbart.h
%{_libdir}/pkgconfig/ruby-libart2.pc

%files -n ruby-libglade2
%defattr(-,root,root,-)
%doc libglade/ChangeLog libglade/COPYING.LIB libglade/README libglade/sample
%{_bindir}/ruby-glade-create-template
#%{ruby_sitelib}/libglade2.rb
%attr(755, root, root) %{ruby_sitelib}/libglade2.rb
%{ruby_sitearch}/libglade2.so

%files -n ruby-libglade2-devel
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/ruby-libglade2.pc

%files -n ruby-panelapplet2
%defattr(-,root,root,-)
%doc panel-applet/ChangeLog panel-applet/COPYING.LIB panel-applet/README panel-applet/sample
%{ruby_sitelib}/panelapplet2.rb
%{ruby_sitearch}/panelapplet2*.so

%files -n ruby-panelapplet2-devel
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/ruby-panelapplet2.pc

%files -n ruby-pango
%defattr(-,root,root,-)
%doc pango/ChangeLog pango/COPYING.LIB pango/README pango/sample
%{ruby_sitelib}/pango.rb
%{ruby_sitearch}/pango.so

%files -n ruby-pango-devel
%defattr(-,root,root,-)
%{ruby_sitearch}/rbpango.h
%{ruby_sitearch}/rbpangoversion.h
%{_libdir}/pkgconfig/ruby-pango.pc

%files -n ruby-poppler
%defattr(-,root,root,-)
%doc poppler/ChangeLog poppler/COPYING.LIB poppler/README poppler/sample
%{ruby_sitelib}/poppler.rb
%{ruby_sitearch}/poppler.so

%files -n ruby-poppler-devel
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/ruby-poppler.pc

%files -n ruby-rsvg
%defattr(-,root,root,-)
%doc rsvg/ChangeLog rsvg/COPYING.LIB rsvg/README rsvg/sample
%{ruby_sitelib}/rsvg2.rb
%{ruby_sitearch}/rsvg2.so

%files -n ruby-rsvg-devel
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/ruby-rsvg2.pc

%files -n ruby-vte
%defattr(-,root,root,-)
%doc vte/ChangeLog vte/COPYING.LIB vte/README vte/sample
%{ruby_sitelib}/vte.rb
%{ruby_sitearch}/vte.so

%files -n ruby-vte-devel
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/ruby-vte.pc


%changelog
* Wed May 25 2010 Mo Morsi <mmorsi@redhat.com> - 0.19.4-3
- removed static ruby abi version dep, bumped version for polisher

* Fri May 7 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp>
- F-13+: rebuild

* Thu Apr 29 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.19.4-1
- Update to 0.19.4, drop all upstreamed patches

* Fri Nov 20 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.19.3-5
- Patch to compile with xulrunner 1.9.2

* Sat Nov  7 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp>
- release++

* Sun Nov  1 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp>
- release++

* Sun Sep 27 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.19.3-2
- Fix crash when moving cursor on fantasdic 1.0 beta 7
  (ruby-gnome2-Bugs-2865895)

* Fri Sep 25 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.19.3-1
- Update to 0.19.3
- Released source does not support gio yet

* Sat Sep 19 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp>
- Try rev 3690
- Massive pkgconfig files renaming
- Enable gio support

* Thu Sep 10 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp>
- release++

* Mon Aug  3 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.19.1-1
- Update to 0.19.1, drop all upstreamed patches
- Introduce many -devel subpackages containing pkgconfig file

* Sun Jul 26 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.19.0-4
- F-12: Mass rebuild

* Thu Jul 09 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.19.0-3
- Make ruby-gtkglext require ruby(opengl)

* Wed Jul 01 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.19.0-2
- Install more needed header files in ruby-gtk2-devel (bug 509035)
- Keep timestamps on installed header files

* Tue Jun 30 2009 Christopher Aillon <caillon@redhat.com>
- Rebuild against newer gecko

* Thu Jun 18 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.19.0-1
- Update to 0.19.0

* Mon Apr 27 2009 Christopher Aillon <caillon@redhat.com> - 0.18.1-7
- Rebuild against newer gecko

* Sat Mar 28 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.18.1-6
- Bump release again

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Dec 26 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> 0.18.1-3
- Bump release
- Patch to compile panel-applet
- Take care of directory owership (bug 474608)

* Thu Nov 13 2008 Allisson Azevedo <allisson@gmail.com> 0.18.1-1
- Update to 0.18.1

* Mon Oct  6 2008 Allisson Azevedo <allisson@gmail.com> 0.18.0-1
- Update to 0.18.0
- Removed ruby-gnome2-0.17.0-bz456816.patch

* Thu Sep 18 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> 0.17.0-3
- Patch from svn to fix Ruby/Glib bug (bug 456816)

* Fri Sep 12 2008 Allisson Azevedo <allisson@gmail.com> 0.17.0-2
- Rebuild against new gstreamer-devel

* Tue Sep  9 2008 Allisson Azevedo <allisson@gmail.com> 0.17.0-1
- Update to 0.17.0
- Removed ruby-gnome2-0.17.0-rc1-newgtk-021303.patch

* Sat Jul 19 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.17.0-0.4.rc1
- F-9+: relax gecko libs dependency
- F-9+: bump version to fix EVR problem between F-8 branch

* Sun Jun 15 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.17.0-0.2.rc1
- F-10: gtk/gtkfilesystem.h is removed from GTK 2.13.3+, some symbols no
  longer available (bug 451402, thanks to Matthias Clasen)

* Sun Jun  8 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.17.0-0.1.rc1
- 0.17.0 rc1
- Remove upstreamed patches - 2 patches remain
  - ruby-gnome2-0.17.0-rc1-script.patch
  - ruby-gnome2-all-0.16.0-xulrunner.patch
- Restrict ruby abi dependency to exact 1.8 version
- Fix the license (to strict LGPLv2)

* Thu Mar 20 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.16.0-28
- Workarround for poppler 0.7.2

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.16.0-27
- Autorebuild for GCC 4.3

* Wed Jan 30 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> 0.16.0-26
- Add BR: poppler-glib-devel

* Sat Jan 26 2008 Allisson Azevedo <allisson@gmail.com> 0.16.0-25
- Fix libglade2 Undefined method error (bugzilla #428781)

* Fri Jan 18 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> 0.16.0-24
- Remove workaround for ruby static archive (#428384 solved)
- Add BR: gecko-devel-unstable

* Sun Dec 30 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> 0.16.0-23
- Revert the wrong patch against src/lib/gtkmozembed.rb

* Sun Dec 30 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> 0.16.0-22
- Update xulrunner patch (#402591)
- Some misc fix for maybe glib2 >= 2.15.0
- Workarround for #226381 c11

* Fri Dec 28 2007 Alex Lancaster <alexlan@fedoraproject.org> 0.16.0-21
- Add xulrunner patch from bugzilla #402591
- Rebuild against gecko-lib 1.9 (xulrunner)

* Tue Dec  4 2007 Allisson Azevedo <allisson@gmail.com> 0.16.0-20
- Fix CVE-2007-6183, format string vulnerability (bugzilla #402871)

* Tue Dec  4 2007 Alex Lancaster <alexlan@fedoraproject.org> 0.16.0-19
- Back to building against gecko 1.8.1.10 (firefox) until #402591 is 
  fixed.

* Sun Dec  2 2007 Alex Lancaster <alexlan@fedoraproject.org> 0.16.0-18
- Rebuild against gecko-lib 1.9 (xulrunner)

* Tue Nov 27 2007 Christopher Aillon <caillon@redhat.com> 0.16.0-17
- Rebuild against newer gecko

* Tue Nov 13 2007 Alex Lancaster <alexlan@fedoraproject.org> 0.16.0-16
- Fix my typo in BuildRequires

* Tue Nov 13 2007 Alex Lancaster <alexlan@fedoraproject.org> 0.16.0-15
- Rebuild against gecko-libs and gecko-devel (firefox 2.0.0.9).

* Thu Oct 25 2007 Allisson Azevedo <allisson@gmail.com> 0.16.0-14
- Rebuild against gecko-libs and gecko-devel

* Wed Oct 24 2007 Allisson Azevedo <allisson@gmail.com> 0.16.0-13
- Rebuild against new firefox

* Thu Sep 13 2007 Allisson Azevedo <allisson@gmail.com> 0.16.0-12
- Newpoppler.patch updated for poppler 0.6

* Sat Sep  8 2007 Allisson Azevedo <allisson@gmail.com> 0.16.0-11
- Rebuild against new poppler
- Changed license to LGPLv2+

* Thu Aug  9 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> 0.16.0-10
- Adjust to GLib 2.14 API + typo fix in glib module

* Thu Aug  9 2007 Allisson Azevedo <allisson@gmail.com> 0.16.0-9
- Rebuild against new firefox

* Fri Aug  4 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> 0.16.0-8
- Apply patch extracted from CVS to build glib gtk poppler

* Fri Jul 20 2007 Jesse Keating <jkeating@redhat.com> 0.16.0-7
- Rebuild against new firefox

* Thu May 31 2007 Allisson Azevedo <allisson@gmail.com> 0.16.0-6
- New gecko engine

* Mon Apr 9 2007 Allisson Azevedo <allisson@gmail.com> 0.16.0-5
- Changed buildrequires and requires

* Mon Apr 9 2007 Allisson Azevedo <allisson@gmail.com> 0.16.0-4
- Changed buildrequires and requires

* Mon Apr 9 2007 Allisson Azevedo <allisson@gmail.com> 0.16.0-3
- Changed buildrequires and requires
- Changed license for LGPL

* Mon Apr 2 2007 Allisson Azevedo <allisson@gmail.com> 0.16.0-2
- Changed buildrequires and requires
- Changed make install for keep timestamps
- Changed package summary

* Sun Mar 24 2007 Allisson Azevedo <allisson@gmail.com> 0.16.0-1
- Initial RPM release
- Thanks Stephanos Manos for base spec
