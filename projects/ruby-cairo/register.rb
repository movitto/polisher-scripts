# ruby-cairo polisher registration

project :name => 'ruby-cairo' do |cairo|
  cairo.add_archive :name => 'ruby-cairo', :uri => 'http://cairographics.org/releases/rcairo-%{version}.tar.gz', :primary_source => true

  cairo.version "*", :depends_on => project(:name => 'ruby')

  cairo.on_version "*",           "download sources"

  cairo.on_version "=",  "1.8.1", "create rpm package", :spec => "#{@project_dir}/template.spec", :mock => @stable_mock_env
  cairo.on_version "=",  "1.8.1", "update yum repo",    :repo => "#{@artifacts_dir}/repos/stable", :delete_rpms => true

  # TODO uncomment when ruby 1.8.7 is setup in maintenance repo
  #cairo.on_version ">=", "1.8.1", "create rpm package", :spec => "#{@project_dir}/template.spec", :mock => @maintenance_mock_env
  #cairo.on_version ">=", "1.8.1", "update yum repo",    :repo => "#{@artifacts_dir}/repos/maintenance", :delete_rpms => true

  cairo.on_version ">=", "1.8.1", "create rpm package", :spec => "#{@project_dir}/template.spec", :mock => @devel_mock_env
  cairo.on_version ">=", "1.8.1", "update yum repo",    :repo => "#{@artifacts_dir}/repos/devel"

  cairo.on_version "*",           "update yum repo",     :repo =>"#{@artifacts_dir}/repos/rawhide"
end
