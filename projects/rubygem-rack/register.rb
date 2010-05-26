# rubygem-rack polisher registration

project :name => 'rubygem-rack' do |rack|
  rack.add_gem :name => 'rack', :uri => 'http://rubygems.org/gems/rack-%{version}.gem', :primary_source => true

  rack.on_version "*",          "download sources"
  rack.on_version "*",          "create rpm package", :spec => "#{@project_dir}/template.spec", :mock => @system_mock_env
  rack.on_version "*",          "update yum repo",    :repo => "#{@artifacts_dir}/repos/rawhide"
  rack.on_version "=", "1.1.0", "update yum repo",    :repo => "#{@artifacts_dir}/repos/stable"
  rack.on_version "=", "1.1.0", "update yum repo",    :repo => "#{@artifacts_dir}/repos/maintenance"
  rack.on_version "*",          "update yum repo",    :repo => "#{@artifacts_dir}/repos/devel"
end
