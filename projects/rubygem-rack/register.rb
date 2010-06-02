# rubygem-rack polisher registration

project :name => 'rubygem-rack' do |rack|
  rack.add_gem :name => 'rack', :uri => 'http://rubygems.org/gems/rack-%{version}.gem', :primary_source => true

  rack.on_version "*",          "download sources"
  rack.on_version "=", "1.1.0", "create rpm package", :spec => "#{@project_dir}/template.spec", :mock => @stable_mock_env
  rack.on_version "=", "1.1.0", "update yum repo",    :repo => "#{@artifacts_dir}/repos/stable", :delete_rpms => true

  # TODO uncomment when ruby 1.8.7 is setup in maintenance repo
  #rack.on_version "*",          "create rpm package", :spec => "#{@project_dir}/template.spec", :mock => @maintenance_mock_env
  #rack.on_version "*",          "update yum repo",    :repo => "#{@artifacts_dir}/repos/maintenance", :delete_rpms => true

  rack.on_version "*",          "create rpm package", :spec => "#{@project_dir}/template.spec", :mock => @devel_mock_env
  rack.on_version "*",          "update yum repo",    :repo => "#{@artifacts_dir}/repos/devel"

  rack.on_version "*",          "update yum repo",    :repo => "#{@artifacts_dir}/repos/rawhide"
end
