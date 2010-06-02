# rubygem-daemons polisher registration

project :name => 'rubygem-daemons' do |daemons|
  daemons.add_gem :name => 'daemons', :uri => 'http://rubygems.org/gems/daemons-%{version}.gem', :primary_source => true

  daemons.version "*", :depends_on => project(:name => 'ruby')

  daemons.on_version "*", "download sources"

  daemons.on_version "*", "create rpm package", :spec => "#{@project_dir}/template.spec", :mock => @stable_mock_env
  daemons.on_version "*", "update yum repo",    :repo => "#{@artifacts_dir}/repos/stable", :delete_rpms => true

  # TODO uncomment when ruby 1.8.7 is setup in maintenance repo
  #daemons.on_version "*", "create rpm package", :spec => "#{@project_dir}/template.spec", :mock => @maintenance_mock_env
  #daemons.on_version "*", "update yum repo",    :repo => "#{@artifacts_dir}/repos/maintenance", :delete_rpms => true

  daemons.on_version "*", "create rpm package", :spec => "#{@project_dir}/template.spec", :mock => @devel_mock_env
  daemons.on_version "*", "update yum repo",    :repo => "#{@artifacts_dir}/repos/devel", :delete_rpms => true

  daemons.on_version "*", "update yum repo", :repo => "#{@artifacts_dir}/repos/rawhide"
end
