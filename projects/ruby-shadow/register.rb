# ruby-shadow polisher registration

project :name => 'ruby-shadow' do |shadow|
  shadow.add_archive :name => 'shadow', :uri => 'http://ttsky.net/src/ruby-shadow-%{version}.tar.gz', :primary_source => true
  shadow.add_patch   :name => 'ruby-shadow-1.4.1-cflags', :uri => "#{@fedora_cvs}/ruby-shadow-1.4.1-cflags.patch?view=co"
  shadow.add_patch   :name => 'ruby-depend-1.4.1-cflags', :uri => "#{@fedora_cvs}/ruby-shadow-1.4.1-depend.patch?view=co"
  shadow.add_patch   :name => 'ruby-struct-1.4.1-cflags', :uri => "#{@fedora_cvs}/ruby-shadow-1.4.1-struct.patch?view=co"

  shadow.version "*", :depends_on => project(:name => 'ruby')

  shadow.on_version "*",           "download sources"

  shadow.on_version "*", "create rpm package", :spec => "#{@project_dir}/template.spec",  :mock => @stable_mock_env
  shadow.on_version "*", "update yum repo",    :repo => "#{@artifacts_dir}/repos/stable", :delete_rpms => true

  # TODO uncomment when ruby 1.8.7 is setup in maintenance repo
  #shadow.on_version "*", "create rpm package", :spec => "#{@project_dir}/template.spec", :mock => @maintenance_mock_env
  #shadow.on_version "*", "update yum repo",    :repo => "#{@artifacts_dir}/repos/maintenance", :delete_rpms => true

  shadow.on_version "*", "create rpm package", :spec => "#{@project_dir}/template.spec", :mock => @devel_mock_env
  shadow.on_version "*", "update yum repo",    :repo => "#{@artifacts_dir}/repos/devel"

  shadow.on_version "*", "update yum repo", :repo => "#{@artifacts_dir}/repos/rawhide"
end
