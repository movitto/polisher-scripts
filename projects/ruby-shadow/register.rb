# ruby-shadow polisher registration

project :name => 'ruby-shadow' do |shadow|
  shadow.add_archive :name => 'shadow', :uri => 'http://ttsky.net/src/ruby-shadow-%{version}.tar.gz', :primary_source => true
  shadow.add_patch   :name => 'ruby-shadow-1.4.1-cflags', :uri => "#{@fedora_cvs}/ruby-shadow-1.4.1-cflags.patch?view=co"
  shadow.add_patch   :name => 'ruby-depend-1.4.1-cflags', :uri => "#{@fedora_cvs}/ruby-shadow-1.4.1-depend.patch?view=co"
  shadow.add_patch   :name => 'ruby-struct-1.4.1-cflags', :uri => "#{@fedora_cvs}/ruby-shadow-1.4.1-struct.patch?view=co"

  shadow.on_version "*", "create rpm package", "#{@project_dir}/template.spec"
  shadow.on_version "*", "update yum repo", "#{@artifacts_dir}/repos/rawhide"
  shadow.on_version "*", "update yum repo", "#{@artifacts_dir}/repos/stable"
  shadow.on_version "*", "update yum repo", "#{@artifacts_dir}/repos/maintenance"
  #shadow.on_version "*", "update yum repo", "#{@artifacts_dir}/repos/devel"
end
