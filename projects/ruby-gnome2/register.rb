# ruby-gnome2 polisher registration

project :name => 'ruby-gnome2' do |rg2|
  rg2.add_archive :name => 'ruby-gnome2', :uri => 'http://downloads.sourceforge.net/ruby-gnome2/ruby-gnome2-all-%{version}.tar.gz', :primary_source => true
  rg2.add_patch   :name => 'ruby-gnome2-0.17.0-rc1-script', :uri => "#{@fedora_cvs}/ruby-gnome2-0.17.0-rc1-script.patch?view=co"
  rg2.add_patch   :name => 'ruby-gnome2-0.19.3-crash-moving-cursor-bz2865895', :uri => "#{@fedora_cvs}/ruby-gnome2-0.19.3-crash-moving-cursor-bz2865895.patch?view=co"
  rg2.add_patch   :name => 'ruby-gnome2-0.19.3-xul192', :uri => "#{@fedora_cvs}/ruby-gnome2-0.19.3-xul192.patch?view=co"

  rg2.on_version "*",             "create rpm package", "#{@project_dir}/template.spec"
  rg2.on_version "*",             "update yum repo",    "#{@artifacts_dir}/repos/rawhide"
  rg2.on_version "=",   "0.19.3", "update yum repo",    "#{@artifacts_dir}/repos/stable"
  rg2.on_version ">=",  "0.19.3", "update yum repo",    "#{@artifacts_dir}/repos/maintenance"
  rg2.on_version ">=",  "0.19.3", "update yum repo",    "#{@artifacts_dir}/repos/devel"
end
